# Hello World CrewAI

Welcome to the HelloWorldCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Prerequisites

- Python 3.13.x installed on your system
- The [py launcher](https://docs.python.org/3/using/windows.html#launcher) (see the main project README for installation instructions)

## How to Run the CrewAI Example

Follow these steps to set up and run the CrewAI example using a virtual environment in the project root:

1. **Create a virtual environment in the project root with py:**

   ```sh
   py -3.13 -m venv .venv
   ```

2. **Install requirements.txt in CrewAI/hello_world_crew:**

   ```sh
   .venv\Scripts\pip.exe install -r CrewAI/hello_world_crew/requirements.txt
   ```

3. **Install other dependencies with crewai:**

   ```sh
   ..\..\.venv\Scripts\crewai.exe install
   ```

   Run this command from the `CrewAI/hello_world_crew` directory.

4. **Fill the environment variables in the .env file:**

   - Edit or create the `.env` file in `CrewAI/hello_world_crew/src/hello_world_crew/` and add your environment parameters (e.g., API keys).

5. **Run crewai:**
   ```sh
   .venv\Scripts\crewai.exe run
   ```
   Run this command from the `CrewAI/hello_world_crew` directory.

---

## Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/hello_world_crew/config/agents.yaml` to define your agents
- Modify `src/hello_world_crew/config/tasks.yaml` to define your tasks
- Modify `src/hello_world_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/hello_world_crew/main.py` to add custom inputs for your agents and tasks

## Understanding Your Crew

The hello_world_crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the HelloWorldCrew Crew or crewAI.

- Visit [documentation](https://docs.crewai.com)
- Reach out through [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)
