
import unittest
from unittest.mock import patch, MagicMock, mock_open
import json
import uuid
from pathlib import Path
from cb2c_py.lib.workflow_runner import WorkflowRunner

class TestWorkflowRunner(unittest.TestCase):

    def setUp(self):
        self.runner = WorkflowRunner(comfyui_server_address="test.server:1234")
        self.workflow_json = json.dumps({
            "prompt": {
                "1": {"class_type": "TestNode", "inputs": {}}
            }
        })
        self.client_id = str(uuid.uuid4())

    @patch('uuid.uuid4')
    @patch('websocket.WebSocket')
    @patch('cb2c_py.lib.workflow_runner.WorkflowRunner._get_outputs')
    @patch('builtins.open', new_callable=mock_open)
    @patch('pathlib.Path.mkdir')
    def test_run_workflow_success(self, mock_mkdir, mock_file_open, mock_get_outputs, mock_ws, mock_uuid):
        # Arrange
        fixed_uuid = "test-client-id"
        mock_uuid.return_value = fixed_uuid
        
        # We need to re-initialize the runner to use the patched uuid
        runner = WorkflowRunner(comfyui_server_address="test.server:1234")

        mock_get_outputs.return_value = [
            (b"imagedata1", "image1.png"),
            (b"imagedata2", "image2.png")
        ]
        
        # Act
        runner.run_workflow(self.workflow_json)
        
        # Assert
        mock_mkdir.assert_called_once_with(exist_ok=True)
        
        # Check that files were "written"
        self.assertEqual(mock_file_open.call_count, 2)
        mock_file_open.assert_any_call(Path("outputs/image1.png"), "wb")
        mock_file_open.assert_any_call(Path("outputs/image2.png"), "wb")
        
        handle = mock_file_open()
        handle.write.assert_any_call(b"imagedata1")
        handle.write.assert_any_call(b"imagedata2")

        # Check that websocket was connected and closed
        mock_ws_instance = mock_ws.return_value
        # The client_id is generated inside run_workflow, so we use the fixed_uuid
        mock_ws_instance.connect.assert_called_once_with(f"ws://{runner.comfyui_server_address}/ws?clientId={fixed_uuid}")
        mock_ws_instance.close.assert_called_once()

    @patch('urllib.request.Request')
    @patch('urllib.request.urlopen')
    def test_queue_prompt(self, mock_urlopen, mock_request):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"prompt_id": "123"}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        prompt_data = json.loads(self.workflow_json)

        # Act
        result = self.runner._queue_prompt(prompt_data, self.client_id)
        
        # Assert
        self.assertEqual(result, {"prompt_id": "123"})
        
        # Check the request
        mock_request.assert_called_once()
        args, kwargs = mock_request.call_args
        self.assertEqual(args[0], f"http://{self.runner.comfyui_server_address}/prompt")
        sent_data = json.loads(kwargs['data'])
        self.assertEqual(sent_data['client_id'], self.client_id)
        self.assertEqual(sent_data['prompt'], prompt_data['prompt'])


    @patch('urllib.request.urlopen')
    def test_get_file(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value = b"file_content"
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        # Act
        result = self.runner._get_file("test.png", "test_sub", "output")
        
        # Assert
        self.assertEqual(result, b"file_content")
        mock_urlopen.assert_called_once_with('http://test.server:1234/view?filename=test.png&subfolder=test_sub&type=output')

    @patch('urllib.request.urlopen')
    def test_get_history(self, mock_urlopen):
        # Arrange
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({"prompt1": {}}).encode('utf-8')
        mock_urlopen.return_value.__enter__.return_value = mock_response
        
        # Act
        result = self.runner._get_history("prompt1")
        
        # Assert
        self.assertEqual(result, {"prompt1": {}})
        mock_urlopen.assert_called_once_with('http://test.server:1234/history/prompt1')

if __name__ == '__main__':
    unittest.main()
