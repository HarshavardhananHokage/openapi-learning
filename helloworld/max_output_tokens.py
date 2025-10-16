from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)

response = client.responses.create(model = "gpt-4o-mini", 
                                   input = "Write me a 100 word story on Demonte-The Rap God Dragon", 
                                   max_output_tokens=20,
                                   metadata={
                                       "name": "Demonte",
                                       "occupation": "Rap God",
                                       "reason": "writing my first rap song"
                                       }
                                   )

print(response.model_dump())