# world-news-20261120

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/wafiq8/world-news-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/wafiq8/world-news-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

A self-contained Python program that sums up the world's news of **Friday, 20 November 2026** in one image. It draws a newspaper front page — "THE WORLD TODAY" — with the day's lead stories: the first Trump–Xi–Putin three-way summit in Shenzhen and its joint peace declaration, the ICJ ruling that Myanmar committed genocide against the Rohingya, Russia's massive strike on Kyiv, the Houthi missile that damaged Riyadh's PIF tower, the deepening AI sell-off (Nikkei −4.8%), the COP31 draft dropping the fossil-fuel phase-out, the EU–UK Brexit reset, Kenya's last Ebola patient going home, Cyclone Akvan's landfall in Odisha, and the first Gaza incursion since the truce — plus a markets ticker and an obituary line for Fiona the hippo.

The day's news is embedded in the program as data (gathered from the day's reporting) and the poster is rendered with Pillow. The program needs no network and is fully deterministic: every run writes byte-identical output.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.png` (1024×1024 PNG, under 1 MiB). Set `OUTPUT_PATH` to write somewhere else. Requires Python 3.13 with Pillow and the DejaVu fonts.

---

<sub>Entered on [make.fun](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>
