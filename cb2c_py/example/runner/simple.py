#!/usr/bin/env python3

# back2code/runner-example.py

from cb2c_py.example.workflow.simple_image import simple_image_workflow
from cb2c_py.lib.progress_handler import ComfyUIProgressHandler

def main():
    """
    Main function to build the workflow and execute it.
    """
    print("Building workflow...")
    image_workflow = simple_image_workflow(
        prompt="a cute baby blue panda in a forest",
        negative_prompt="blurry, bad quality"
    )

    # Run the workflow with the progress callback
    image_workflow.run(
        progress_callback=ComfyUIProgressHandler(name="Image Generation")
    )

if __name__ == "__main__":
    main()