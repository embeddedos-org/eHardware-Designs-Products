# 🌾 eFarm — Business / Donor Plan (concept)

> **Status:** Concept (sensor stack + LoRa mesh topology TBD)
> **Donor tier:** $1 K — equip a 25-acre cooperative farm.

## What a donor funds

Half a billion smallholder farmers feed a third of the world. They lose 20–40 % of yield to drought, disease, and timing decisions made without data. eFarm puts a $40 sensor under each acre and sends crop-stress and irrigation alerts to a phone via LoRaWAN — no cell tower required.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM per node (qty 1) | ~$65 |
| BOM per node (qty 10k) | ~$32 |
| Gateway (RAK7268V2) | ~$120 each, covers ~10 km radius |
| Mobile app + dashboard | Reuse eOffice + eAI (zero marginal) |

## Regulatory path

LoRaWAN regional bands (EU868, US915, AS923, IN865); RoHS; no medical claims.

## Go-to-market / distribution

Partner with FAO, One Acre Fund, Digital Green; donor sponsors a cooperative; subscription-free for smallholders.

## EmbeddedOS components leveraged

- eos (low-power kernel)
- eAI (crop-stress + drought prediction)
- eIPC (LoRa mesh transport)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
