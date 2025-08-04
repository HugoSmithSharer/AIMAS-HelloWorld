from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class HelloWorldCrew():
    """HelloWorldCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    
    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def developer(self) -> Agent:
        return Agent(
            config=self.agents_config['developer'], # type: ignore[index]
            verbose=True
        )

    @task
    def feature_decompose(self) -> Task:
        return Task(
            config=self.tasks_config['feature_decompose'], # type: ignore[index]
        )
    
    @task
    def task_development(self) -> Task:
        return Task(
            config=self.tasks_config['task_development'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the HelloWorldCrew crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential, # Another option: hierarchical https://docs.crewai.com/how-to/Hierarchical/
            verbose=True,
        )
