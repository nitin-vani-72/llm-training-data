import jsonlines

transcript_txt = "C:\\Users\\welcom\\Documents\\Coding\\Python\\vaani task\\Transcripts\\GMT20190420-054510_Pratishtha_640x360_transcript.txt"

assistant = "Speaker A"
user = "Speaker B"

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

    if(speaker == user):
      role_user["content"] = content
      json_template["messages"].append(role_user)

    if(speaker == assistant):
      role_assistant["content"] = content
      json_template["messages"].append(role_assistant)

  whole_jsonl.append(json_template)

  with jsonlines.open("data_to_feed_1.jsonl", mode='w') as jsonl_file:
    jsonl_file.write_all(whole_jsonl)

  jsonl_file.close()
transcript.close()