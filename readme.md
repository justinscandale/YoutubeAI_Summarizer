# YouTube Transcript to Detailed Note Converter

This Streamlit web application allows users to input a YouTube video URL, extract its transcript, and generate a detailed summary of the video. Additionally, users can ask questions related to the video, and the AI will answer based on the transcript.

## Features

- **Extract Transcript**: Automatically fetches the transcript of the YouTube video.
- **Generate Summary**: Summarizes the video transcript into concise, important points.
- **Ask Questions**: Allows users to ask questions related to the video, with answers based on the transcript content.


## Installation

1. **Clone the Repository**  
   If you haven't already, clone the repository to your local machine:  
   git clone https://github.com/your-username/youtube-transcript-summary.git  
   cd youtube-transcript-summary  

2. **Set up the Environment**  
   It's recommended to use a virtual environment for the setup. You can create a new virtual environment using the following commands:  
   python -m venv venv  
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`  

3. **Install Required Dependencies**  
   Install the necessary Python dependencies using `pip`:  
   pip install -r requirements.txt  

4. **Set Up Environment Variables**  
   This app uses the **Google Gemini API** to generate summaries and answers. You'll need to set up an API key for the `google.generativeai` package.  
   - Create a `.env` file in the root directory of the project.  
   - Add the following line to the `.env` file, replacing `YOUR_GOOGLE_API_KEY` with your actual API key:  
   GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY  

5. **Install Required Libraries**  
   If you don't have a `requirements.txt` file, you'll need to manually install the dependencies:  
   pip install streamlit google-generativeai python-dotenv youtube-transcript-api  

6. **Run the Application**  
   After everything is set up, you can run the Streamlit app using the following command:  
   streamlit run app.py  

   This will launch the app in your web browser, where you can input a YouTube video URL, view its transcript, ask questions, and receive AI-generated answers based on the transcript.
