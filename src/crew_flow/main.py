# Simple Flow with CrewAI

from crewai.flow.flow import Flow, start, listen
from crew_flow.crews.blog_crew.blog_crew import BlogCrew
from dotenv import load_dotenv
from litellm import completion
from pydantic import BaseModel
import os

load_dotenv()
API_KEY=os.getenv('GEMINI_API_KEY')

class CrewBase(BaseModel):
    topic: str = ""
    content: str = ""

class CrewFlow(Flow[CrewBase]):

    @start()
    def generate_topic(self):
        topic = (
            BlogCrew()
            .crew()
            .kickoff(inputs={"category":"AI"})
        )

        print(f"--Trending Topics-- \n", topic.raw)
        self.state.topic = topic
        # return self.state.topic
    
    @listen(generate_topic)
    def generate_content(self):

        content = (
            BlogCrew()
            .crew()
            .kickoff(inputs={"category":"AI"})
        )

        print(f"--Content-- \n", content.raw)
        self.state.content = content.raw


    @listen(generate_content)
    def display(self):
        return {"Topic": self.state.topic, "Content": self.state.content, "Author":"Shamoon"}


def kickoff():
    crewflow = CrewFlow()
    crewflow.kickoff()

def plot():
    crewplot = CrewFlow()
    crewplot.plot()