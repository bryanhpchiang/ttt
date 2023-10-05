import json
import tiktoken  # for token counting
import numpy as np
from collections import defaultdict
import utils as u

dataset = u.load("mistakes-final.jsonl")

train_size = int(0.6 * len(dataset))
np.random.shuffle(dataset)
train_dataset = dataset[:train_size]
val_dataset = dataset[train_size:]

u.dump(train_dataset, "mistakes-final-train.jsonl")
u.dump(val_dataset, "mistakes-final-val.jsonl")
