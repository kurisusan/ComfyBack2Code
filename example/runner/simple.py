#!/usr/bin/env python3

# comfyui/back2code/runner-example.py

from comfyui.back2code.example.workflow.simple import build_simple_workflow

def main():
    """
    Main function to build the workflow and execute it.
    """
    print("Building workflow...")
    workflow = build_simple_workflow()
    
    # Run the workflow
    workflow.run()

if __name__ == "__main__":
    main()