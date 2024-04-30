from typing_extensions import override
from openai import OpenAI, AssistantEventHandler

client = OpenAI()

class EventHandler(AssistantEventHandler):    
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)

  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)

empty_thread = client.beta.threads.create()


messages=[]

while True:
  userinput = input("User: ")


  if userinput.lower() =="exit":
    break

  thread_message = client.beta.threads.messages.create(
      thread_id = empty_thread.id,
      role="user",
      content=userinput,
  )

  with client.beta.threads.runs.stream(
    thread_id=empty_thread.id,
    assistant_id="asst_n8C6iIKXZEfjytLwouhQTtrI",
    instructions="Only answer questions about the document and remind the user if needed. The user has advanced mathematical background, so mathematical rigor is preferred where applicable.",
    event_handler=EventHandler(),
  ) as stream:
    stream.until_done()
  
  print("\n")



# file = client.files.create(
#   file=open("rref.pdf", "rb"),
#   purpose="assistants"
# )

# my_assistant = client.beta.assistants.create(
#     instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
#     name="Math Tutor",
#     tools=[{"type": "code_interpreter"}],
#     model="gpt-4-turbo",
#     file_ids=[file.id]
# )

#
#run = client.beta.threads.runs.create_and_poll(
#  thread_id=empty_thread.id,
#  assistant_id="asst_n8C6iIKXZEfjytLwouhQTtrI",
#  instructions="The user has advanced mathematical background, so mathematical rigor is preferred where applicable.",
#)



# if run.status == 'completed': 
#   messages = client.beta.threads.messages.list(thread_id=empty_thread.id)
#   print(messages.data[0].content[0].text.value)
# else:
#   print(run.status)


#messagedata = json.loads(messages.model_dump_json())

#store = {}

# for count, message in enumerate(messagedata['data']):
#     print(count, "Message ID:", message['id'])
#     print(count,"Assistant ID:", message['assistant_id'])
#     print(count,"Content:", message['content'][0]['text']['value'])
#     print(count,"Role:", message['role'])
#     print(count,"Created At:", message['created_at'])
#     print(count,"Thread ID:", message['thread_id'])
#     print("-----------------------")
#     store[count] = message['content'][0]['text']['value']


# for key, value in store.items():
#    print(key, value)
   
'''

run_steps = client.beta.threads.runs.steps.list(
    thread_id=empty_thread.id,
    run_id=run.id
)

print(run_steps)

'''


#print(my_assistant.model_dump_json)

#assistant_data = json.loads(my_assistant.model_dump_json())



