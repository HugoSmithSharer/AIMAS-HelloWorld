# Hello World Semantic Kernel

This guide explains how to set up and run the Semantic Kernel example in this directory.

## Prerequisites

- Python 3.13.x installed on your system
- The [py launcher](https://docs.python.org/3/using/windows.html#launcher) (see the main project README for installation instructions)

## How to Run the Semantic Kernel Example

Follow these steps to set up and run the Semantic Kernel example:

1. **Create and activate a virtual environment with py:**

   ```sh
   py -3.13 -m venv .venv
   ```

   - **Windows (PowerShell):**
     ```sh
     .venv\Scripts\Activate
     ```
   - **macOS/Linux:**
     ```sh
     source .venv/bin/activate
     ```

2. **Install required packages:**

   ```sh
   pip install -r .\SemanticKernel\requirements.txt
   ```

3. **Fill in the environment variables for LLM in the .env file:**

   - Edit or create the `.env` file in the `SemanticKernel` directory and add your environment parameters (e.g., API keys).

4. **Run the example:**

   ```sh
   python .\SemanticKernel\hello_world_main.py
   ```

This will start the Semantic Kernel example and display output in your terminal.

---

For any issues, ensure you are using Python 3.13 and that your virtual environment is activated before installing packages or running the script.
