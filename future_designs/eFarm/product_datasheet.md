# 🌾 eFarm — Concept Datasheet

> **Status:** Concept (sensor stack + LoRa mesh topology TBD)
> **Category:** Climate, Food, Water
> **EmbeddedOS components:** eos (low-power kernel), eAI (crop-stress + drought prediction), eIPC (LoRa mesh transport)

## Tagline

Solar-powered LoRaWAN soil/crop sensor mesh for smallholder farmers.

## Why this exists (donor pitch)

Half a billion smallholder farmers feed a third of the world. They lose 20–40 % of yield to drought, disease, and timing decisions made without data. eFarm puts a $40 sensor under each acre and sends crop-stress and irrigation alerts to a phone via LoRaWAN — no cell tower required.

## Target users

Smallholder farmers in Sub-Saharan Africa, South Asia, Andean / Latin America; agronomy NGOs.

## Suggested donor tier

$1 K — equip a 25-acre cooperative farm.

## Hardware sketch

- STM32WL55 (built-in LoRa SX126x, ultra-low-power Cortex-M4)
- Capacitive soil moisture + EC sensor (waterproof, IP68)
- SHT41 air T/RH; BH1750 light; SCD41 NDIR CO₂
- E-paper 2.13" status display (low duty cycle)
- 0.5 W solar panel + 18650 LiFePO4 cell + TI BQ24074 charger
- IP67 enclosure with M12 sensor stub
- Optional gateway: RAK7268V2 LoRaWAN concentrator

## EmbeddedOS stack

- eos (low-power kernel)
- eAI (crop-stress + drought prediction)
- eIPC (LoRa mesh transport)

## BOM target

~$40 per node + shared $120 gateway

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eFarm] graduate to draft`.
2. Stand up `kicad/efarm_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
