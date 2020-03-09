import json
import random
from bottle import HTTPResponse

snake_butts = [
    "regular",
    "block-bum",
    "bolt",
    "curled",
    "fat-rattle",
    "freckled",
    "hook",
    "pixel",
    "round-bum",
    "sharp",
    "skinny",
    "small-rattle",
    "bwc-bonhomme",
    "bwc-flake",
    "bwc-ice-skate",
    "bwc-present",
]
snake_heads = [
    "regular",
    "beluga",
    "bendr",
    "dead",
    "evil",
    "fang",
    "pixel",
    "safe",
    "sand-worm",
    "shades",
    "silly",
    "smile",
    "tongue",
    "bwc-bonhomme",
    "bwc-earmuffs",
    "bwc-rudolph",
    "bwc-scarf",
    "bwc-ski",
    "bwc-snow-worm",
    "bwc-snowman",
]


def ping_response():
    return HTTPResponse(status=200)


def start_response(color):
    assert type(color) is str, "Color value must be string"

    return HTTPResponse(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps(
            {
                "color": color,
                "headType": random.choice(snake_heads),
                "tailType": random.choice(snake_butts),
            }
        ),
    )


def move_response(move):
    assert move in [
        "up",
        "down",
        "left",
        "right",
    ], "Move must be one of [up, down, left, right]"

    return HTTPResponse(
        status=200,
        headers={"Content-Type": "application/json"},
        body=json.dumps({"move": move}),
    )


def end_response():
    return HTTPResponse(status=200)
