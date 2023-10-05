import pickle
from IPython import embed
from collections import Counter
import random
import utils as u
import json


with open("boards.pkl", "rb") as f:
    boards = pickle.load(f)

counts = Counter(b.winner for b in boards)

# 255168 games, 131184 nought wins, 77904 cross wins, 46080 draws.
assert len(boards) == 255168
assert counts[0] == 131184
assert counts[1] == 77904
assert counts[-1] == 46080

# filter to when O starts at center
clean = [b for b in boards if b.moves[0] == (4, 0) and b.winner == 0]

# sample 50 random games with a set seed
random.seed(42)
N = 100
sampled = random.sample(clean, N)

examples = []
for game in sampled:
    b = u.Board()
    messages = [
        {
            "role": "system",
            "content": "You are a professional tic-tac-toe player. You are O.\n\nYou always play the optimal move and want to win the game. Numbers indicate an empty position. \n\nState your move as just single number indicating the position you want to play at.",
        },
    ]
    current = ""
    for pos, v in game.moves:
        if v == 0:  # llm
            current += "This is the current game board.\n\n{}\n\n\nYour move:".format(b)
            messages.append({"role": "user", "content": current})
            messages.append({"role": "assistant", "content": str(pos + 1)})
            examples.append({"messages": messages.copy()})
        elif v == 1:  # user
            current = "I choose {}.\n\n".format(pos + 1)
    # break
# embed()

with open("data-{}.jsonl".format(N), "w") as f:
    for entry in examples:
        json.dump(entry, f)
        f.write("\n")

embed()
