from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(model = "gpt-4o-mini", input = "Write me a 100 word story on Demonte-The Rap God Dragon")

print(response.output_text)