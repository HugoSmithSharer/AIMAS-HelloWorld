# Hello World LangGraph

This guide explains how to set up and run the LangGraph example in this directory.

## Prerequisites

- Python 3.13.x installed on your system
- The [py launcher](https://docs.python.org/3/using/windows.html#launcher) (see the main project README for installation instructions)

## How to Run the LangGraph Example

Follow these steps to set up and run the LangGraph example:

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
   pip install -r .\LangGraph\requirements.txt
   ```

3. **Fill in the environment variables in the .env file:**

   - Edit or create the `.env` file in the `LangGraph` directory and add your environment parameters (e.g., API keys).

4. **Run the example:**

   ```sh
   python .\LangGraph\hello_world_main.py
   ```

This will start the LangGraph example and display output in your terminal.

---

For any issues, ensure you are using Python 3.13 and that your virtual environment is activated before installing packages or running the script.
