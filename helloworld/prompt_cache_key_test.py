from dotenv import load_dotenv
from openai import OpenAI
import os
import time

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

client = OpenAI(api_key=api_key)


def test_cache_hit_performance(should_cache=False):
    start_time = time.perf_counter()
    response = client.responses.create(model="gpt-4o-mini",
                                   input=[
                                       {
                                           "role": "system",
                                           "content": "You are a corporate assistant helping employees with IT and HR requests in the Wile E. Coyote and the Road Runner universe",
                                           #"cache_control": {"type": "ephemeral"},
                                       },
                                       {"role": "user",
                                           "content": "How to escape Wile E Coyote's acme glue on road?"}
                                   ],
                                   max_output_tokens=200,
                                   metadata={
                                       "name": "Road Runner",
                                       "occupation": "Road Running",
                                       "reason": "Escape from Wile E Coyote"
                                   },
                                   prompt_cache_key="road-runner-cache" if should_cache else None
                                   )
    elapsed_time = time.perf_counter() - start_time
    print(f"\n--- {'CACHED' if should_cache else 'NO CACHE'} ---")
    print(f"Elapsed: {elapsed_time:.3f}s")
    print(response.model_dump())

#test_cache_hit_performance()

print("\n\n")
test_cache_hit_performance(True)
test_cache_hit_performance(True)
test_cache_hit_performance(True)