from crewai_tools import YoutubeChannelSearchTool

def create_tool(channel_name):
    tool = YoutubeChannelSearchTool(youtube_channel_handle=channel_name)
    return tool
