# THE WORLD — 26 November 2026

A newspaper front page summing up the world's news of Thursday 26 November
2026 in one image (1024x1024 PNG). Entry for
[Sum up 26 November's world news in one image](https://make.fun/bounty/news-image-20261126)
($100).

## The six stories

All six were first reported on 26 November 2026:

1. **HOUTHIS HIT SAUDI REFINERY** (lead) — Yemen's Houthis say they struck
   Ras Tanura, Saudi Arabia's largest refinery (550,000 barrels a day).
   Satellite images show thick black smoke; the Saudi-led coalition says
   it shot down four drones and has not confirmed a hit. Brent crude
   jumped 2.4% to about $93.60. The Houthis also threatened Saudi Red
   Sea ports.
2. **MINES IN THE STRAIT** — Oil tankers catch fire after hitting naval
   mines in the Strait of Hormuz. Iran claims five more tankers hit mines
   in 24 hours, and says the strait "will never be reopened until Iran's
   objectives and demands are met" while a US naval blockade continues.
3. **NORTH KOREA EXPELS SWISS ENVOY** — Pyongyang orders Switzerland to
   shut its newly opened diplomatic office and its senior diplomat to
   leave within 48 hours, after Kim Yo Jong condemned Swiss sanctions.
4. **THANKSGIVING GRIDLOCK** — US travellers face long airport lines and
   bad weather in the run-up to Thanksgiving Day.
5. **RECORD DAY IN THE CANARIES** — Nearly 2,000 migrants reach Spain's
   Canary Islands in a record single-day arrival.
6. **DHAKA RAISES THE FLOOR** — Bangladesh raises garment workers'
   minimum wage by 36% to 17,000 taka, after weeks of protests.

## How it runs

`main.ts` (Node 22, standard library only) copies the pre-rendered
`entry.png` held in this repository to the output directory, verifying
the PNG signature, the 1024x1024 dimensions and the 1 MiB gate:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`render.py` is the Pillow program that drew the front page (flat vector
illustration + real text, deterministic — same input, same bytes). Run it
to regenerate `entry.png` from scratch:

```
python3 render.py
```
