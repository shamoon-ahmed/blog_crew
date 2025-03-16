from crewai import Agent, Task, Crew, Process
from crewai.project import agent, task, crew, CrewBase
from dotenv import load_dotenv
import os

load_dotenv()
# API_KEY = os.getenv('GEMINI_API_KEY')

@CrewBase
class BlogCrew:
    """Blog Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def topic_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["topic_generator"],
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"],
        )

    @task
    def generate_topic(self) -> Task:
        return Task(
            config=self.tasks_config["generate_topic"],
        )

    @task
    def write_blog(self) -> Task:
        return Task(
            config=self.tasks_config["write_blog"],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            # verbose=True,
        )