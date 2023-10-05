import openai
from dataclasses import dataclass, field
import numpy as np
import json


@dataclass
class Board:
    state: np.array = field(default_factory=lambda: np.full(9, -1))
    moves: list = field(default_factory=list)
    pieces = ["O", "X"]
    winner = -1

    def set(self, pos, value):
        # O = 0
        # X = 1
        self.state[pos] = value
        self.moves.append((pos, value))

    def __str__(self):
        return """{} | {} | {} \n---------\n{} | {} | {} \n---------\n{} | {} | {} """.format(
            *[i + 1 if x < 0 else self.pieces[x] for i, x in enumerate(self.state)]
        )

    def print(self):
        print(str(self))

    def finished(self):
        return len(self.moves) == 9


def load(data_path):
    # data_path = "mistakes-final.jsonl"
    with open(data_path, "r", encoding="utf-8") as f:
        # for line in f:
        #     print("new!")
        #     print(line)
        dataset = [json.loads(line) for line in f]
        return dataset


def dump(examples, path):
    with open(path, "w") as f:
        for entry in examples:
            json.dump(entry, f)
            f.write("\n")


def complete(
    messages,
    model="gpt-3.5-turbo",
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    return response["choices"][0]["message"]["content"].strip()
    # breakpoint()


if __name__ == "__main__":
    print(complete([{"role": "user", "content": "Why is the sky blue?"}]))
