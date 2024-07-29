from crewai import Crew, Process
from agents import create_agents_and_tools
from tasks import research_task, write_task

def get_crew_tool(channel_name):
    YT_Agent, blog_writer_Agent, yt_tool = create_agents_and_tools(channel_name)
    crew_tool = Crew(
        agents=[YT_Agent, blog_writer_Agent],
        tasks=[research_task(yt_tool, YT_Agent), write_task(yt_tool, blog_writer_Agent)],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )
    return crew_tool

