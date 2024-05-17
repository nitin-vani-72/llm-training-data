import assemblyai as aai
import csv

# Replace with your API key
aai.settings.api_key = "80d867835b734cef9fa0f91c0594b0b9"

config = aai.TranscriptionConfig(speaker_labels=True,speakers_expected= 2)
transcriber = aai.Transcriber()

def transcribe_func(FILE_URL):
  transcript = transcriber.transcribe(
    FILE_URL,
    config=config
  )
  return transcript

# Write the transcript to a file
filename = 'Batch_1.csv'

with open(filename, 'r') as csvfile:
    data = csv.reader(csvfile)

    next(data)

    for row in data:
        transcript = transcribe_func(str(row[2]))

        with open(row[0].split(".")[0] + "_transcript.txt", "w") as file:
          for utterance in transcript.utterances:
            file.write(f"Speaker {utterance.speaker}: {utterance.text}\n")