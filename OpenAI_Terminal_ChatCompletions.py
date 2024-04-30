import os
from openai import OpenAI

def main():
    # Initialize history with a system message
    systemprompt = {"role": "system", "content": "You are a helpful assistant."}
    history = []

    # Get the OpenAI API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    # Model to use for the chat
    model = "gpt-4-turbo-preview"

    while True:
        preppedmessage = history[-10:]
        preppedmessage.insert(0, systemprompt)

        # Prompt the user for input
        user_input = input("You: ")
        print("\n")

        
        # Add user input to history
        #usermessage = {"role": "user"}

        
        history.append({"role": "user", "content": user_input})



        # Generate response from OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=preppedmessage,
            stream=True,
        )

        # Print the response
        fullresponse = []

        print("Assistant: ", end="")

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")
                fullresponse.append(chunk.choices[0].delta.content)
            else:
                print("\n")

        print()  # Add a newline after each response
        response_string = ''.join(chunk for chunk in fullresponse)
        history.append({"role": "assistant", "content": response_string})

if __name__ == "__main__":
    main()

    '''
    response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ],
        }
    ],
    max_tokens=300,
)
    '''

'''
message["content"] = [
    {"type": "text", "text": "Use the content below to answer"},
    {"type": "text", "text": "text"}]
'''