import assemblyai as aai
import os

# Replace with your API key
aai.settings.api_key = "80d867835b734cef9fa0f91c0594b0b9"


# URL of the file to transcribe
FILE_URL = "https://ixznag.dm.files.1drv.com/y4mZKz7a1MeAyWEwyz7EVwUF5q629ApwZtgAsZ2-DRikv5Yq4_8ZJ_C_NMsVlIFOivbSG9MJ3_-q_K7c9dvmdNxSLYcnWB8HS0frFlaNmivTM59VfefzyFp3iLv2gHDtoj8fh-b7WxK4b2sdXjFW-jUHCZtqzKrSJVqxFb1-FwJFs7JykUo2oW3WgEVBJL4eQJQ6nVodOsmXkL_4AbAcBykLA?"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './recordings/GMT20190420-054510_Pratishtha_640x360.mp4'

config = aai.TranscriptionConfig(speaker_labels=True,speakers_expected= 2)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(
  FILE_URL,
  config=config
)

# Extract the filename from the FILE_URL
# transcript_name = os.path.basename(FILE_URL).split(".")[0] + "_transcript.txt"

# transcripts_folder = os.path.join(os.path.dirname(FILE_URL), '..', 'Transcripts')

# transcript_path = os.path.join(transcripts_folder, transcript_name)

# Write the transcript to a file
with open("transcript.txt", "w") as file:
  for utterance in transcript.utterances:
    file.write(f"Speaker {utterance.speaker}: {utterance.text}\n")
# for utterance in transcript.utterances:
#   print(f"Speaker {utterance.speaker}: {utterance.text}")