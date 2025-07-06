#!/usr/bin/env python3

# back2code/runner-example.py

from cb2c_py.example.workflow.simple_image import simple_image_workflow

def main():
    """
    Main function to build the workflow and execute it.
    """
    print("Building workflow...")
    image_workflow = simple_image_workflow(
        prompt="a cute baby panda",
        negative_prompt="blurry, bad quality"
    )
    
    # Run the workflow
    image_workflow.run()

if __name__ == "__main__":
    main()