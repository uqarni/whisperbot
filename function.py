from pytube import YouTube
import openai 
from pydub import AudioSegment
import os

def yt_to_transcript(yt_url):

    yt = YouTube(yt_url)
    random_hex = hex(random.randrange(16**8))[2:].upper().zfill(8)
    audiofilename = "audio-" + random_hex + ".mp3"
    audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(output_path='', filename=audiofilename)

    audio_file= open("audiofiles"+audiofilename, "rb")
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format = "text")

    transcriptfilename = "transcript-"+random_hex+".txt"
    with open("transcripts/"+transcriptfilename, 'w') as file:
        file.write(transcript)
    
    return transcriptfilename



