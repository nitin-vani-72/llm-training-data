import os
import jsonlines

# Path to the "Transcripts" folder
transcripts_folder = "C:\\Users\\welcom\\Documents\\Coding\\Python\\vaani task\\Transcripts In-Process"

assistant = "Speaker A"
user = "Speaker B"

# Get a list of all files in the "Transcripts" folder
transcript_files = os.listdir(transcripts_folder)

try:
  # Iterate over each file in the list
  for transcript_file in transcript_files:
    # Create the full path to the current file
    transcript_txt = os.path.join(transcripts_folder, transcript_file)

    json_template = {
    "messages":[
        {
          "role": "system",
          "content": "You are a english communication coach named 'Vani'. You are having a conversation with learner to find out about his job profile and analyze the answers that learner provides and ask more questions"
        }
      ]
    }

    whole_jsonl = []

    with open(transcript_txt, 'r') as transcript:
      for line in transcript:
        # print(line)

        if (line == "\n"):
          whole_jsonl.append(json_template)

          json_template = {
            "messages":[
                {
                  "role": "system",
                  "content": "You are a english communication coach named 'Vani'. You are having a conversation with learner to find out about his job profile and analyze the answers that learner provides and ask more questions"
                }
              ]
            }

          continue

        role_user = {
          "role": "user",
          "content": ""
        }

        role_assistant = {
          "role": "assistant",
          "content": ""
        }

        speaker = line.split(": ")[0]
        content = line.split(": ")[1].rstrip("\n")
        # print(transcript_file + " " + speaker + " " + content)

        if(speaker == user):
          role_user["content"] = content
          json_template["messages"].append(role_user)

        if(speaker == assistant):
          role_assistant["content"] = content
          json_template["messages"].append(role_assistant)

      whole_jsonl.append(json_template)

      with jsonlines.open("Batch_1.jsonl", mode='a') as jsonl_file:
        jsonl_file.write_all(whole_jsonl)

      jsonl_file.close()
    transcript.close()

except Exception as e:
  print("Error: " + str(e))

print("Conversion completed!")