import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.FineTuningJob.cancel(id="ftjob-mpZCgyNSvGaidhvlA8VELA36"))
