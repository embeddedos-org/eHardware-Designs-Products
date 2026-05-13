# ⚡ eMeshGrid — Business / Donor Plan (concept)

> **Status:** Concept (control loop + safety interlocks TBD)
> **Donor tier:** $25 K — fund one controller + 30 kWh battery + solar array for a 200-person village.

## What a donor funds

770 million people live without electricity. eMeshGrid is the brain of a community-scale solar + battery system — load forecasting, fault detection, and OTA-updatable behaviour from a single industrial-grade box. One controller can light a village.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$1,250 |
| BOM (qty 100) | ~$870 |
| Battery + solar (per village deployment) | $15-22 K |
| Site engineering + commissioning | ~$3 K per site |

## Regulatory path

IEC 61508 SIL-2 control; UL 1741 grid-tie (where grid-tied); local utility permit per region.

## Go-to-market / distribution

Partner with Practical Action, ENGIE Energy Access, Solar Sister; donor sponsors a village; community owns the controller.

## EmbeddedOS components leveraged

- eos (real-time kernel)
- eAI (load forecast + fault detection)
- eIPC (fleet ops + remote support)
- eBoot (verified field updates)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
