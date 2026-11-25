"""The Tired Dark Lord: a 100-word villain monologue.

Writes the monologue to /output/entry.txt (UTF-8, 1-600 characters).
"""

import os

ENTRY = (
    "Ah. The hero. Come in \u2014 mind the third step; the rot took it in the spring, "
    "and the carpenter... left. Three hundred years I have held this tower, and what "
    "do they remember? The taxes. Not the eclipse I hung over the valley. Not the "
    "river I turned to glass. The taxes. Sit. The tea's cold again \u2014 it always "
    "is, by the time I pour it. You came to end me? Then take the crown. It's on the "
    "hook. The vault word is 'swordfish', the moat needs dredging, and the ravens... "
    "the ravens can wait. They have waited this long."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
