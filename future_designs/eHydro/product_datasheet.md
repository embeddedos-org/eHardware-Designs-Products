# 💧 eHydro — Concept Datasheet

> **Status:** Concept (sensor calibration + public dashboard TBD)
> **Category:** Climate, Food, Water
> **EmbeddedOS components:** eos (low-power kernel), eAI (anomaly = contamination spike), eIPC (cell + LoRa fallback)

## Tagline

Community-deployed water-quality monitoring buoy + public dashboard.

## Why this exists (donor pitch)

2.2 billion people lack safely-managed drinking water. Most contamination events go undetected for days. eHydro is a $250 solar-powered buoy that streams live pH / turbidity / conductivity / temperature to a public dashboard — turning every river, well, and reservoir into a citizen-science sentinel.

## Target users

Community water committees, environmental NGOs, municipal water authorities, citizen scientists.

## Suggested donor tier

$3 K — deploy a 10-buoy mesh on a contested river basin for one year.

## Hardware sketch

- STM32U5 (ultra-low-power Cortex-M33)
- Atlas Scientific industrial pH probe (kit)
- DFRobot SEN0189 turbidity probe
- Atlas Scientific conductivity (EC) probe
- DS18B20 waterproof temperature probe
- Quectel BG95 LTE-M modem (with LoRa fallback)
- 5 W solar panel + 6 Ah LiFePO4 + MPPT charger
- Marine-grade buoy housing (UV-stable PE), tethered float

## EmbeddedOS stack

- eos (low-power kernel)
- eAI (anomaly = contamination spike)
- eIPC (cell + LoRa fallback)

## BOM target

~$250

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eHydro] graduate to draft`.
2. Stand up `kicad/ehydro_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
