from crewai import Task

def research_task(yt_tool, YT_Agent):
    return Task(
        description=(
            "Identify the Video {topic} and get the detailed information about the video from the channel"
        ),
        expected_output="Create a comprehensive neatly formatted blog that is extremely professional and perspicacious and educative about the topic: {topic}",
        tools=[yt_tool],
        agent=YT_Agent
    )

def write_task(yt_tool, blog_writer_Agent):
    return Task(
        description=(
            "get the info from the youtube channel on the topic {topic} using the transcripts and create the content for a blog"
        ),
        expected_output='summarize the info from the youtube channel idea on the topic {topic}',
        tools=[yt_tool],
        agent=blog_writer_Agent,
        async_execution=False,
        output_file='new-blog-post.md'
    )
