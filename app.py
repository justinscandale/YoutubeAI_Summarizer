import streamlit as st
from dotenv import load_dotenv
load_dotenv() #load all enviorment variables
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# get summary based on prompt and transcipt from google gemini
def generate_gemini_content(transcipt_text):

    prompt = f"""You are a youtube video summarizer.  
    You will be taking the transcipt text and summarizing the entire video 
    and providing the important summary points within 250 words 
    the transcipt text will be appended here: {transcipt_text}"""
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(transcipt_text)
    return response.text

# get transcipt data from youtube video
def extract_transcipt_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for line in transcript_text:
            transcript += " " + line["text"]
        
        return transcript
    
    except Exception as e:
        raise e

# get response for the user's question based on the transcript
def generate_answer_to_question(transcript_text, question):
    model = genai.GenerativeModel("gemini-pro")
    # Modify the prompt to include the question and the transcript
    question_prompt = f"""
    You are an AI assistant that answers questions based on the transcript of a YouTube video.
    The transcript is provided below, and the user will ask a question about it.
    Answer the user's question in a concise and relevant manner based on the video content.

    Transcript: {transcript_text}
    
    User's Question: {question}
    Answer:
    """
    response = model.generate_content(question_prompt)
    return response.text

st.title("Youtube Transcipt to Detailed Note Converter")
youtube_link = st.text_input("Enter your youtube video link:")
# Store transcript, summary, and user question in session state
if "transcript_text" not in st.session_state:
    st.session_state.transcript_text = ""

if "summary" not in st.session_state:
    st.session_state.summary = ""

if "transcript_available" not in st.session_state:
    st.session_state.transcript_available = False

if "user_question" not in st.session_state:
    st.session_state.user_question = ""

# If YouTube link is provided
if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# Get detailed notes for the video
if st.button("Get Detailed Notes"):
    st.session_state.transcript_text = extract_transcipt_details(youtube_link)

    if st.session_state.transcript_text:
        st.session_state.summary = generate_gemini_content(st.session_state.transcript_text)
        st.session_state.transcript_available = True  # Mark transcript as available
        st.markdown("## DETAILED NOTES:")
        st.write(st.session_state.summary)

    else:
        st.error("Could not extract transcript text. Please make sure the video is transcribed.")

# Conditionally show the question input after transcript is available
if st.session_state.transcript_available:
    user_question = st.text_input("Ask a question about the video:", key="question_input")

    # Store the user's question
    if user_question:
        st.session_state.user_question = user_question

    # Answer the user's question
    if st.session_state.user_question:
        answer = generate_answer_to_question(st.session_state.transcript_text, st.session_state.user_question)
        st.markdown("## Answer to Your Question:")
        st.write(answer)