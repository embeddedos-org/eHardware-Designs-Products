# 🐝 eHive — Business / Donor Plan (concept)

> **Status:** Concept (acoustic classifier dataset + microphone placement TBD)
> **Donor tier:** $500 — equip a 5-hive community apiary for two years.

## What a donor funds

One in three bites of food depends on bee pollination, and managed honeybee colony losses run 30–40 % per year. eHive listens to the hive — a $90 monitor that classifies “healthy / queenless / swarming / collapsing” from the sound spectrum and texts the beekeeper before a colony is lost.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$95 |
| BOM (qty 5k) | ~$58 |
| Acoustic dataset / model training | ~$30 K (partnered with Cornell Bee Lab) |
| Mobile alerts | Reuse existing eOffice mail / Twilio (zero marginal) |

## Regulatory path

No regulatory restrictions (passive monitoring); FCC/CE for radios.

## Go-to-market / distribution

Partner with The Bee Conservancy, Project Apis m., university apiculture programs; hive-cooperative purchase model.

## EmbeddedOS components leveraged

- eos (low-power kernel)
- eAI (acoustic classifier on-device)
- eIPC (LoRa or LTE-M telemetry)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
