import os
from dotenv import load_dotenv
from openai import OpenAI
from simronangpt.openai import prompts

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def _make_prompt(prompt):
    session = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=prompt
    )

    response = session.choices[0].message.content
    return response

def prompt_simple_lyric():
    prompt = prompts.simple_lyric_generation()
    return _make_prompt(prompt)

def prompt_topical_lyric(topic: str):
    prompt = prompts.topical_lyric_generation(topic)
    return _make_prompt(prompt)
