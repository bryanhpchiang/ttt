import os
import openai
from IPython import embed

f = openai.File.create(
    file=open("mistakes-final-train.jsonl", "rb"), purpose="fine-tune"
)
val_f = openai.File.create(
    file=open("mistakes-final-val.jsonl", "rb"), purpose="fine-tune"
)

job = openai.FineTuningJob.create(
    training_file=f["id"],
    validation_file=val_f["id"],
    model="gpt-3.5-turbo",
    hyperparameters={"n_epochs": 1},
)
print(job)
embed()
