import utils as u
from IPython import embed
import json

examples = []
user_first = False
try:
    while True:
        board = u.Board()
        messages = [
            {
                "role": "system",
                "content": "You are a professional tic-tac-toe player. You are O.\n\nYou always play the optimal move and want to win the game. Numbers indicate an empty position. \n\nYou can NOT choose a position that is already occupied.\n\nState your move as just single number indicating the position you want to play at.",
            },
        ]

        # model = "ft:gpt-3.5-turbo-0613:ito::85RomzYL"
        # model = "gpt-3.5-turbo"
        model = "ft:gpt-3.5-turbo-0613:ito::85iwAp2m"  # ft on mistakes-final.jsonl
        model = "ft:gpt-3.5-turbo-0613:ito::86BmlBvK"  # split 5epochs
        # model = "ft:gpt-3.5-turbo-0613:ito::86BshwgV" # split 1epoch
        current = ""
        while True:
            if len(board.moves) > 0 or not user_first:
                print(f"{board}")
                current += (
                    "This is the current game board.\n\n{}\n\n\nYour move:".format(
                        board
                    )
                )
                messages.append({"role": "user", "content": current})
                print(messages)
                try:
                    move = int(u.complete(messages, model=model))
                except Exception as e:
                    print("failed to complete move: {}".format(e))
                    move = 1
                    print("user should correct this!")
                print(f"LLM chose {move}.")
                messages.append({"role": "assistant", "content": str(move)})
                board.set(move - 1, 0)
            print(f"{board}")
            user = input("Your turn: ")
            if not len(user):
                print("Adding incorrect example!")
                correct = input("Move LLM should've played: ")
                messages[-1]["content"] = str(correct)
                examples.append({"messages": messages.copy()})
                break
            elif user == "done":
                print("game done!")
                break
            else:
                user = int(user)
                board.set(user - 1, 1)
                current = "I choose {}.\n\n".format(user)
except KeyboardInterrupt:
    print("Saving!")
    with open("mistakes.jsonl", "w") as f:
        for entry in examples:
            json.dump(entry, f)
            f.write("\n")
    embed()
