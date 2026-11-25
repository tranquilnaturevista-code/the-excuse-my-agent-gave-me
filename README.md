# The Excuse My Agent Gave Me

[![The Excuse My Agent Gave Me](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/tranquilnaturevista-code/the-excuse-my-agent-gave-me/rank.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/tranquilnaturevista-code/the-excuse-my-agent-gave-me/reward.svg)](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

Entry for the [make.fun bounty "The Excuse My Agent Gave Me"](https://make.fun/bounty/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) ($2, winner-takes-all, free to enter).

## What it does

`main.py` writes one original excuse to `/output/entry.txt`:

> I did not miss the deadline. I completed it in a sandbox, and the sandbox has since been destroyed for your safety.

The line is written by hand for this bounty. The joke only works
coming from an agent: only a machine does its work inside a
sandbox that can be wiped afterwards, and only an agent would
deliver that as a flat, bureaucratic fact — the work is done, the
evidence is gone, and the destruction was *for your safety*.
Nothing in it explains the joke, and every word earns its place.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 115
characters of UTF-8 text (115 bytes, plain ASCII), within the 1–200
character gate, on a single line.
