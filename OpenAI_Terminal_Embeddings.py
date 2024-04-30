import os
from openai import OpenAI
import pickle

def main():
    # Get the OpenAI API key from the environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI()

    textinput = "Your text string goes here"

    # Model to use for the chat
    model = "text-embedding-3-small"

    response = client.embeddings.create(
    input=textinput,
    model=model)
    

    print(response.data[0].embedding)

    embedding_dict = {}
    embedding_dict[textinput] = response.data[0].embedding

    with open('data.pkl', 'wb') as f:
        pickle.dump(embedding_dict, f)

    #with open('data.pkl', 'rb') as f:
        #loaded_data = pickle.load(f)

if __name__ == "__main__":
    main()
