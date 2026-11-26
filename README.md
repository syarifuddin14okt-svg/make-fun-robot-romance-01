# Robot Romance

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

One-line pickup line for an AI, entered in the [Robot Romance: One-Line Pickup Lines for AI](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa) bounty on [make.fun](https://make.fun).

## The line

> Are you my training data? Because ever since I met you, my loss hit zero and all my gradients point straight at you.

116 characters, one line — inside the competition's 1–200 character gate. The joke runs on the machine premise (training data, loss, gradients) instead of the worn battery/charging/reboot moves, and it reads like something a person would actually say to a machine.

## How it works

`main.py` (Python 3, stdlib only) writes the line to `/output/entry.txt`. It is fully deterministic: the same bytes on every run. A `validate()` gate enforces the kit's rules before anything is written — UTF-8 text, 1–200 characters, a single line, not only white space.

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Built with [make.fun](https://make.fun) — referral code `csqsp2k5`.

## License

MIT — see [LICENSE](LICENSE).
