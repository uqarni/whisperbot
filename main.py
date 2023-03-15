from pytube import YouTube
import openai 
from pydub import AudioSegment
import os
import requests

# Define the Streamlit app
def main():
    # Set the title of the app
    st.title("Youtube to .txt transcript")

    # Add a text input for the user to input the URL
    url = st.text_input("Enter a URL")

    if st.button("Generate transcript"):
        processed_data = yt_to_transcript(url)
        
    # Add a download button to start the processing
    if st.download_button("Download Now", "transcripts"+processed_data):
        # Call the process_url function with the user's URL



# Run the app
if __name__ == "__main__":
    main()