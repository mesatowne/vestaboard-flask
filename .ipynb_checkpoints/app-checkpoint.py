import random
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    raw_message = request.args.get("text", "AND JUST LIKE THAT,\\nWE'RE OFF.")
    lines = raw_message.split("\\n")

    while len(lines) < 6:
        lines.append("")

    #padded_lines = [line.ljust(22)[:22] for line in lines[:6]]
    padded_lines = [line.ljust(22)[:22][:13] + line.ljust(22)[:22][14:] for line in lines[:6]]

    board = []
    for row in padded_lines:
        board_row = []
        for char in row:
            tile = {"char": char, "color": random.choice(["white", "white", "white", "red", "yellow"])}
            board_row.append(tile)
        board.append(board_row)

    return render_template("index.html", board=board)