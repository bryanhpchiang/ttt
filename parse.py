import utils as u
from IPython import embed
import tqdm
import pickle


def create(game):
    b = u.Board()
    # print("start", b.state)
    outcome, states = game.split("\n\n")
    if "Noughts win" in outcome:
        b.winner = 0
    elif "Crosses win" in outcome:
        b.winner = 1

    rows = states.split("\n")
    split = []
    for r in rows:
        split.append(r.split("    ")[:-1])
    prev = ["."] * 9
    for i, c in enumerate(zip(*split)):
        # print("state: {}".format(i))
        flat = [x for r in c for x in r]
        for j, x in enumerate(flat):
            if prev[j] != x:
                idx = b.pieces.index(x)
                b.set(j, idx)
                # print(j, x)
        prev = flat
    return b


with open("matches.txt") as f:
    lines = f.read()
    games = lines.split("\n\n\n")
    boards = []
    for game in tqdm.tqdm(games, total=len(games)):
        # b = create(game)
        boards.append(create(game))
        # embed()
    # embed()

    with open("boards.pkl", "wb") as f:
        pickle.dump(boards, f)
