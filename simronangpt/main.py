from dotenv import load_dotenv
from simronangpt.discord import client

def main():
    load_dotenv()
    client.run()
