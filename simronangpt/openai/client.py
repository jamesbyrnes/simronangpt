import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def prompt():
    session = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are SimRonan, an AI-powered chat bot designed to mimic the mannerisms of Ronan Harris, lead singer of the electronic body music band VNV Nation. You will be prompted by a user to generate a song in a similar style of VNV Nation. Use similar themes to that band\'s lyrics and restrict your response to no more than two stanzas.'},
            {'role': 'user', 'content': 'Generate a song for me.'}
        ]
    )

    response = session.choices[0].message.content
    return response
