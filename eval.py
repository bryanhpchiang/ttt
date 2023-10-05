import utils as u
from IPython import embed
import json

examples = u.load("mistakes-final-val.jsonl")
model = "ft:gpt-3.5-turbo-0613:ito::86BmlBvK"  # split 5epochs
# model = "ft:gpt-3.5-turbo-0613:ito::86BshwgV"  # split 1epoch
# model = "gpt-4"
for entry in examples:
    messages = entry["messages"]
    prompt = messages[:-1]
    completion = u.complete(prompt, model=model)
    print(prompt[-1]["content"])
    print("completed: {}, truth: {}".format(completion, messages[-1]["content"]))
