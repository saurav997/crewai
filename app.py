import streamlit as st
from dotenv import load_dotenv
from crew import get_crew_tool
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(
    page_title="YouTube Channel Blog Generator",
    page_icon="📝",
    layout="wide"
)

st.title("YouTube Channel Blog Generator")
col1, col2 = st.columns(2)

with col1:
    channel_name = st.text_input("Enter YouTube Channel Name")
    topic = st.text_input("Enter Topic for Research")
    generate_button = st.button("Generate Blog Post")

with col2:
    if generate_button and topic and channel_name:
        crew_tool = get_crew_tool(channel_name)
        result = crew_tool.kickoff(inputs={'topic': topic})
        st.subheader("Generated Blog Post")
        st.write(result)
    else:
        st.subheader("Enter a topic and channel name to create a blog!")
        st.write("Blog post will appear here!!")
