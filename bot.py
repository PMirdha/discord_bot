import os
from client import client
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('DISCORD_TOKEN')
client.run(token)
