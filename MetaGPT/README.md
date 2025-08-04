# Hello World MetaGPT

## Prerequisites

- Python 3.13.x installed on your system
- The [py launcher](https://docs.python.org/3/using/windows.html#launcher) (see the main project README for installation instructions)

## How to Run the MetaGPT Example

Follow these steps to set up and run the MetaGPT example:

1. **Create a virtual environment with Python 3.11 using py:**

   ```sh
   py -3.11 -m venv .venv
   ```

2. **Activate the virtual environment:**

   - **Windows (PowerShell):**
     ```sh
     .venv\Scripts\Activate
     ```
   - **macOS/Linux:**
     ```sh
     source .venv/bin/activate
     ```

3. **Install dependencies:**

   ```sh
   pip install -r .\MetaGPT\requirements.txt
   ```

4. **Install extra packages:**

   ```sh
   pip install --upgrade pip setuptools
   pip install --no-deps metagpt==0.8.2
   pip install google-api-core==2.11.0
   pip install google-generativeai==0.4.1 --no-deps
   pip install google-ai-generativelanguage==0.4.0 --no-deps
   pip install proto-plus==1.22.3
   ```

5. **Create the config file for LLM:**

   The configuration file for LLM settings is located at:

   ```
   ~/.metagpt/config2.yaml
   ```

   This file will be created automatically when you run the following command:

   - **On Windows:**
     ```sh
     ./.venv/Scripts/metagpt.exe --init-config
     ```
   - **On macOS/Linux:**
     ```sh
     ./.venv/bin/metagpt --init-config
     ```

   You can edit `config2.yaml` to customize your LLM and other MetaGPT settings.

   Refer to [LLM API Configuration](https://docs.deepwisdom.ai/main/en/guide/get_started/configuration/llm_api_configuration.html) for configuration for different APIs.

   For Azure Open AI, here is an example:

   ```
   llm:
     api_type: "azure" # Must be "azure" for Azure OpenAI
     base_url: "https://<azure-openai-project-name>.openai.azure.com/"
     api_key: "azure api key"
     api_version: "the api version can be retrieved from full api endpoint url"
     model: "deployment name, not model name!"
   ```

6. **Run the example:**

   ```sh
   python ./MetaGPT/hello_world_main.py
   ```

This will start the MetaGPT example and display output in your terminal.

---

## Additional Notes

- Always activate your virtual environment before running MetaGPT scripts.
- To deactivate the virtual environment, simply run:
  ```sh
  deactivate
  ```
