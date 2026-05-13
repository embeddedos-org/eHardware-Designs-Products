# 👓 eVision — Business / Donor Plan (concept)

> **Status:** Concept (datasheet draft, KiCad schematic TBD)
> **Donor tier:** $5 K — sponsor 25 production units for a school for the blind.

## What a donor funds

285 million visually-impaired people globally. Commercial obstacle-detection wearables sit at $4 K and up. eVision targets a $200 BOM with the same core capability, paired with an open hardware design so any local repair shop can service it.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | TBD (target sub-$200) |
| BOM (qty 1k) | TBD (target sub-$120) |
| Tooling (mould + jig) | TBD (~$25 K one-time) |
| Certification (CE / FCC) | TBD (~$15 K) |

## Regulatory path

CE Class I medical device (assistive); FCC Part 15 (BLE); RoHS.

## Go-to-market / distribution

Direct grant-funded distribution via NGO partners; open hardware so local repair networks can sustain it.

## EmbeddedOS components leveraged

- eos (kernel + HAL)
- eAI (on-device object recognition)
- eIPC (companion-app sync)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
