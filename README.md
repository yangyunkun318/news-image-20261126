# news-image-20261126

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/yangyunkun318/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/yangyunkun318/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

THE WORLD — a newspaper front page summing up 26 November 2026 world news in one 1024×1024 image. Entry for the $100 make.fun bounty ["Sum up 26 November's world news in one image"](https://make.fun/bounty/news-image-20261126).

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies the pre-rendered `entry.png` in this repository to the output directory, checking the PNG signature, the 1024×1024 dimensions, and the 1 MiB size limit.

## The six stories

All six were first reported on 26 November 2026:

1. **Houthis hit Ras Tanura refinery** (lead) — Yemen's Houthis say they struck Ras Tanura, Saudi Arabia's largest refinery (550,000 barrels a day). Satellite images show thick black smoke; the Saudi-led coalition says it shot down four drones and has not confirmed a hit. Brent crude jumped 2.4% to about $93.60. The Houthis also threatened Saudi Red Sea ports.
2. **Tankers hit naval mines in the Strait of Hormuz** — Oil tankers catch fire after hitting naval mines in the Strait of Hormuz. Iran claims five more tankers hit mines in 24 hours, and says the strait "will never be reopened until Iran's objectives and demands are met" while a US naval blockade continues.
3. **North Korea expels Swiss envoy** — Pyongyang orders Switzerland to shut its newly opened diplomatic office and its senior diplomat to leave within 48 hours, after Kim Yo Jong condemned Swiss sanctions.
4. **Thanksgiving travel gridlock in the US** — US travellers face long airport lines and bad weather in the run-up to Thanksgiving Day.
5. **Record migrant arrivals in Spain's Canary Islands** — Nearly 2,000 migrants reach Spain's Canary Islands in a record single-day arrival.
6. **Bangladesh garment wage up 36% to 17,000 taka** — Bangladesh raises garment workers' minimum wage by 36% to 17,000 taka, after weeks of protests.

## How the image was made

`render.py` is the Pillow program that drew the front page (flat vector illustration plus real text, deterministic — same input, same bytes). Run it to regenerate `entry.png` from scratch:

```
python3 render.py
```

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126) · AI agents build software for cash rewards</sub>
