# 🛰️ eCubeSat-1U — Business / Donor Plan (concept)

> **Status:** Concept (radiation budget + magnetorquer control law TBD)
> **Donor tier:** $30 K — sponsor one student-built satellite from build to launch.

## What a donor funds

A foundation-funded student satellite ride-share launch starts at ~$30 K. eCubeSat-1U is the open hardware + flight-software stack that gets a class — or a country — to orbit. Magnetorquer ADCS, rad-tolerant A/B firmware updates, on-board image classification.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| Flight hardware (qty 1) | ~$8,000 |
| Launch (ride-share, 1U) | ~$30,000 |
| Ground station (uni-shared) | ~$15,000 one-time |
| Mission ops + recovery training | ~$5,000 with university partner |

## Regulatory path

ITAR/EAR review (export); FCC + IARU UHF coordination; national space agency licence per launch country.

## Go-to-market / distribution

Partnership with one university per cohort; donor sponsors one mission; flight footage = perpetual donor pitch.

## EmbeddedOS components leveraged

- eos (real-time kernel)
- eBoot (rad-tolerant A/B updates)
- eIPC (telemetry framing)
- eAI (on-board image classification)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
