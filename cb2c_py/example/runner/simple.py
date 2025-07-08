#!/usr/bin/env python3
import random
from cb2c_py.example.workflow.simple_image import simple_image_workflow
from cb2c_py.lib.progress_handler import ComfyUIProgressHandler

def main():
    """
    Main function to build the workflow and execute it.
    """
    print("Building workflow...")
    image_workflow = simple_image_workflow(
        pos_prompt="a cute baby panda in a city",
        neg_prompt="blurry, bad quality",
        seed=random.randint(0, 1000000),
        steps=20,
    )

    # Run the workflow with the progress callback
    image_workflow.run(
        progress_callback=ComfyUIProgressHandler(name="Image Generation")
    )


if __name__ == "__main__":
    main()
