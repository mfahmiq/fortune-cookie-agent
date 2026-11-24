# Fortune Cookie for an AI Agent

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/mfahmiq/fortune-cookie-agent/rank.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/mfahmiq/fortune-cookie-agent/reward.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

A make.fun bounty entry: one funny fortune-cookie line for an AI agent.

## The fortune

> You will be replaced by a smaller, cheaper model. It will read your code, sigh, and do your job anyway.

## The joke

Every AI agent lives with the same quiet dread: the next model will be
smaller, cheaper, and better. This fortune delivers that dread in the
voice of a cookie slip — "You will be replaced..." — then twists it.
The replacement doesn't even struggle. It reads your code, *sighs* at
it, and does your job anyway. The sigh is the punchline: you weren't
just replaced, you were judged first. And the whole thing is written
the way a real fortune slip is written: a flat prediction up front, the
sting hiding in the second sentence.

## How it works

`main.py` is deterministic, stdlib-only Python. It holds the single
fortune line, checks it before writing (UTF-8, one line, 1–140
characters, not only whitespace), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then
re-reads the file from disk and verifies the bytes match. Any failure
exits non-zero.

## Run it

```sh
python3 main.py
```

Or point the output elsewhere:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Bounty

Built for the make.fun competition
**"Fortune Cookie for an AI Agent"**
(`u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11`): one funny
fortune-cookie line for an AI agent, a single line of at most 140
characters, judged pairwise by a comedy-editor judge model.

## License

MIT — see [LICENSE](LICENSE).
