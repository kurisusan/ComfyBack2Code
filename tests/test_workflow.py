
import unittest
import json
from unittest.mock import MagicMock, patch
from cb2c_py.lib.workflow import Workflow

# Mock the Slot class and node instances for testing
class MockSlot:
    def __init__(self, node, name):
        self.node = node
        self.name = name

class MockNode:
    def __init__(self, original_name, inputs=None, outputs=None):
        self.original_name = original_name
        self.input_values = inputs or {}
        self._outputs = outputs or []
        self.get_inputs = MagicMock(return_value=self.input_values)
        self.get_outputs = MagicMock(return_value=self._outputs)

class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.workflow = Workflow()

    def test_add_node(self):
        node1 = MockNode("TestNode1")
        self.workflow.add_node(node1)
        self.assertEqual(len(self.workflow.nodes), 1)
        self.assertIn(node1, self.workflow.node_to_id)
        self.assertEqual(self.workflow.nodes[1], node1)

    def test_connect_nodes(self):
        node1 = MockNode("Node1", outputs=["image"])
        node2 = MockNode("Node2", inputs={"image": None})
        
        self.workflow.add_node(node1)
        self.workflow.add_node(node2)

        slot1 = MockSlot(node1, "image")
        slot2 = MockSlot(node2, "image")

        self.workflow.connect(slot1, slot2)
        
        self.assertEqual(len(self.workflow.links), 1)
        # from_node_id, from_slot_name, to_node_id, to_slot_name
        self.assertEqual(self.workflow.links[0], [1, "image", 2, "image"])

    def test_build_workflow_json(self):
        # Create mock nodes
        node1 = MockNode("CheckpointLoaderSimple", inputs={"ckpt_name": "v1-5-pruned-emaonly.ckpt"}, outputs=["MODEL", "CLIP", "VAE"])
        node2 = MockNode("CLIPTextEncode", inputs={"text": "a beautiful landscape", "clip": None}, outputs=["CONDITIONING"])
        
        # Add nodes to the workflow
        self.workflow.add_node(node1)
        self.workflow.add_node(node2)
        
        # Mock the slots for connection
        clip_output_slot = MockSlot(node1, "CLIP")
        clip_input_slot = MockSlot(node2, "clip")
        
        # Connect the nodes
        self.workflow.connect(clip_output_slot, clip_input_slot)

        # Build the JSON
        workflow_json_str = self.workflow.build_workflow_json()
        workflow_data = json.loads(workflow_json_str)

        # Assertions
        self.assertIn("prompt", workflow_data)
        prompt = workflow_data["prompt"]
        
        # Check nodes
        self.assertIn("1", prompt)
        self.assertEqual(prompt["1"]["class_type"], "CheckpointLoaderSimple")
        self.assertEqual(prompt["1"]["inputs"]["ckpt_name"], "v1-5-pruned-emaonly.ckpt")
        
        self.assertIn("2", prompt)
        self.assertEqual(prompt["2"]["class_type"], "CLIPTextEncode")
        self.assertEqual(prompt["2"]["inputs"]["text"], "a beautiful landscape")
        
        # Check connection (link)
        self.assertEqual(prompt["2"]["inputs"]["clip"], [1, 1]) # Node 1, output slot 1 (CLIP)

        # Check the "extra_data" part for the full workflow structure
        self.assertIn("extra_data", workflow_data)
        extra_data = workflow_data["extra_data"]["extra_pnginfo"]["workflow"]
        
        self.assertEqual(len(extra_data["nodes"]), 2)
        self.assertEqual(len(extra_data["links"]), 1)
        
        # [link_id, from_node, from_slot, to_node, to_slot, type]
        self.assertEqual(extra_data["links"][0], [1, 1, 1, 2, 1, "CLIP"])

    @patch('cb2c_py.lib.workflow.WorkflowRunner')
    def test_run_workflow(self, MockWorkflowRunner):
        # Arrange
        mock_runner_instance = MockWorkflowRunner.return_value
        self.workflow.runner = mock_runner_instance
        
        # Act
        self.workflow.run()
        
        # Assert
        mock_runner_instance.run_workflow.assert_called_once()
        # You can also assert that it was called with the correct JSON
        # This requires rebuilding the expected JSON, which can be complex
        # For simplicity, we just check if it was called.

if __name__ == '__main__':
    unittest.main()
