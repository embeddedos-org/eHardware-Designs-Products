# 🤖 eHand — Business / Donor Plan (concept)

> **Status:** Concept (mechanical sketch + EMG decoder algorithm TBD)
> **Donor tier:** $2 K — fund one full eHand build for a single recipient.

## What a donor funds

65 million amputees worldwide. Commercial myoelectric hands cost $30–60 K. eHand targets a $1.5 K BOM with comparable degrees of freedom, 3D-printable socket, and a published surgeon-fitting guide — turning a multi-decade insurance fight into a weekend clinic.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$1,500 |
| BOM (qty 100) | ~$1,000 |
| Per-recipient fitting | ~$200 (clinic time) |
| Regulatory + clinical study | ~$120 K (one-time) |

## Regulatory path

Class II medical device (FDA), CE MDR. Long path; eHand released as research/educational hardware first, clinic-grade variant later.

## Go-to-market / distribution

Partnership with university prosthetics programs; clinic-of-record per region; no per-unit licence fee.

## EmbeddedOS components leveraged

- eos (kernel)
- eNI (EMG signal pipeline)
- eAI (gesture intent classifier)
- eBoot (firmware updates)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
