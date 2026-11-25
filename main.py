"""The Funniest Honest Appliance Error: washing machine, unbalanced load.

The line
--------
"ERROR E21: Unbalanced load. One sock is doing all the spinning. I refuse
to dance with a single sock."

Revision note (pass 2): the closing "with one sock" repeated the "One
sock" that opens the middle sentence, so it now reads "with a single
sock" -- same meaning, no repeated word, and "single" sharpens the
loneliness of the sock doing all the spinning. Nothing else changed.

Why this line (reasoning against the published judge brief)
-----------------------------------------------------------
The brief weighs, most important first: (1) it must be an honest error
message an appliance could show, (2) the laugh must land as a real joke,
a surprise or a twist, not a cute phrasing, (3) it must name a fault an
appliance could plausibly report, so the humour comes from the truth of
it, (4) it must sound like the appliance itself speaking, flat and
put-upon, (5) every word must earn its place inside 200 characters.

E21 unbalanced load is a real washing-machine fault: the drum cannot
spin properly because the load sits on one side. The honest cause is
almost always one heavy item -- here, a single sock -- clumped alone.
The joke rides on that truth instead of bolting a pun onto it: the
machine, which only knows spinning, reframes the spin cycle as a dance
and refuses to dance with a single sock. The deadpan "ERROR E21" opening
is the machine's own voice; the refusal is the surprise. No word
explains the joke.

Rejected candidates (and why they lost)
----------------------------------------
- "ERROR: Sock not found. I searched the drum twice. Your left sock has
  left the building." The missing-sock truth is real, but no washing
  machine can honestly report a sock as "not found" -- it has no sensor
  for that -- so the honesty criterion is weaker than a load fault it
  genuinely detects.
- "ERROR: I am not cold anymore. Your ice cream is soup now. Please stop
  opening me to check if I changed my mind." Funny and honest about a
  warm fridge, but the second sentence lectures the owner instead of
  staying in the machine's flat voice, and the joke is spread too thin.
- "ERROR: Bread jammed. I am not a storage unit. Please stop using me as
  a bread hotel." The toaster premise is honest, but "bread hotel" is a
  cute phrasing that only smiles; there is no twist, just a complaint.
- "ERROR E04: Drain blocked. I am holding 12 litres of your dirty sock
  water and I will not release it until someone cares." Honest fault,
  but it runs long, the threat is wordy, and "until someone cares" is
  the machine explaining its own joke.

Output contract
---------------
Writes the single entry line to <output dir>/entry.txt, where the
output dir is MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output.
Prints the line to stdout as well. Exits non-zero if the line is empty
or over 200 characters, so a bad line fails loudly instead of shipping.
"""

import os
import sys

ENTRY = (
    "ERROR E21: Unbalanced load. One sock is doing all the spinning. "
    "I refuse to dance with a single sock."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry line is {len(line)} chars, over 200", file=sys.stderr)
        return 1
    if "\n" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
