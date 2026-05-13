# 💧 eHydro — Business / Donor Plan (concept)

> **Status:** Concept (sensor calibration + public dashboard TBD)
> **Donor tier:** $3 K — deploy a 10-buoy mesh on a contested river basin for one year.

## What a donor funds

2.2 billion people lack safely-managed drinking water. Most contamination events go undetected for days. eHydro is a $250 solar-powered buoy that streams live pH / turbidity / conductivity / temperature to a public dashboard — turning every river, well, and reservoir into a citizen-science sentinel.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$280 |
| BOM (qty 1k) | ~$165 |
| Cell-data subscription | ~$3/buoy/month (pooled SIM) |
| Public dashboard | Reuse embeddedos-org.github.io stack (zero marginal) |

## Regulatory path

No medical or potability claims (advisory data only); cell-modem regional certification per market.

## Go-to-market / distribution

Partner with WaterAid, EarthEcho International, local water committees; public open data licence (CC0).

## EmbeddedOS components leveraged

- eos (low-power kernel)
- eAI (anomaly = contamination spike)
- eIPC (cell + LoRa fallback)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
