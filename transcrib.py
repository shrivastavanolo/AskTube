from openai import OpenAI
from secret import openaiapi
import pytube as pt
import os

os.environ["OPENAI_API_KEY"]=openaiapi
client = OpenAI()

def get_vid(url):
    try:
      try:
        yt = pt.YouTube(url)
        t=  yt.streams.filter(only_audio=True)
        t[0].download(f"audio_files\\{yt.title}")
        print("Vid downloaded")
      except Exception as e:
         print(e)
        
      for filename in os.listdir(f"audio_files\\{yt.title}"):
          f = f"audio_files\\{yt.title}\\"+filename
          "Vid ret"
          return f,filename
    except Exception as e:
      print(e)
      return None


def transcribe(url):
  try:
    audio_path, file_path=get_vid(url)
    if os.path.exists("txt_files\\"+file_path[:-4].replace(" ","_")+".txt"):
      return "txt_files/"+file_path[:-4].replace(" ","_")+".txt"
    audio_file = open(audio_path, "rb")
    print("Transcribing")
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=audio_file, 
      response_format="text"
    )
    print(transcription)
    with open("txt_files\\"+file_path[:-4].replace(" ","_")+".txt","w") as file:
      file.write(transcription)
      print("File written")
      return "txt_files\\"+file_path[:-4].replace(" ","_")+".txt"
  except Exception as e:
     print(e)
     return None