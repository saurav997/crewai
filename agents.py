from crewai import Agent
from tools import create_tool
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def create_agents_and_tools(channel_name):
    yt_tool = create_tool(channel_name)

    YT_Agent = Agent(
        role='Blog Creator from Youtube videos',
        goal='get the relevant video content for the topic of {topic} from the YouTube Channel',
        verbose=True,
        memory=True,
        backstory=(
            '''Expert in understanding videos pertaining to {topic} 
            in the videos transcript provided along with a
            with a flair in simplifying the topics in a 
            captivating and educating manner'''
        ),
        tools=[yt_tool],
        allow_delegation=True
    )

    blog_writer_Agent = Agent(
        role='Blog Writer',
        goal='Narrate compelling tech stories about the video {topic} from the youtube channel.',
        verbose=True,
        memory=True,
        backstory=(
            '''Expert in narrating videos pertaining to {topic} 
            in the videos transcript provided along with a
            with a flair in simplifying the topics in a 
            captivating and educating manner'''
        ),
        tools=[yt_tool],
        allow_delegation=False
    )

    return YT_Agent, blog_writer_Agent, yt_tool
