# AutoGen Framework - Hello World

This guide explains how to set up and run the AutoGen framework example in this directory.

## Prerequisites

- Python 3.13.x installed on your system
- The [py launcher](https://docs.python.org/3/using/windows.html#launcher) (see the main project README for installation instructions)

## 1. Create and Activate a Virtual Environment

Open a terminal in the `AutoGen` directory and run:

```sh
py -3.13 -m venv .venv
```

Activate the virtual environment:

- **Windows (PowerShell):**
  ```sh
  .venv\Scripts\Activate
  ```
- **macOS/Linux:**
  ```sh
  source .venv/bin/activate
  ```

## 2. Install Required Packages

With the virtual environment activated, install the dependencies:

```sh
pip install -r requirements.txt
```

## 3. Set Environment Parameters

Before running the example, you must set environment parameters for calling the LLM (such as API keys and endpoints) in a `.env` file in the `AutoGen` directory.

Example `.env` file:

```
OPENAI_API_KEY=your-openai-api-key
OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
OPENAI_API_MODEL=your-deployment-name
OPENAI_API_VERSION=2024-02-15-preview
```

Make sure to update these values with your actual credentials and endpoints.

## 4. Run the Example

Run the hello world script:

```sh
python hello_world_main.py
```

This will start the AutoGen example and display output in your terminal.

---

For any issues, ensure you are using Python 3.13 and that your virtual environment is activated before installing packages or running the script.
