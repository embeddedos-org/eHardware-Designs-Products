# ⚡ eMeshGrid — Concept Datasheet

> **Status:** Concept (control loop + safety interlocks TBD)
> **Category:** Infrastructure & Frontier
> **EmbeddedOS components:** eos (real-time kernel), eAI (load forecast + fault detection), eIPC (fleet ops + remote support), eBoot (verified field updates)

## Tagline

Off-grid micro-grid controller for community solar + battery + inverter.

## Why this exists (donor pitch)

770 million people live without electricity. eMeshGrid is the brain of a community-scale solar + battery system — load forecasting, fault detection, and OTA-updatable behaviour from a single industrial-grade box. One controller can light a village.

## Target users

Off-grid community energy projects, NGO energy-access programs, refugee-camp utilities.

## Suggested donor tier

$25 K — fund one controller + 30 kWh battery + solar array for a 200-person village.

## Hardware sketch

- AMD Kintex-7 FPGA (real-time PWM + safety interlocks)
- Apollo4 Plus Cortex-M4 host MCU
- 3-phase contactor stack (40 A per phase, motorised)
- Isolated voltage / current sense (HCPL-7510, ACS758)
- Hall-effect DC current sensors on each battery string
- Quectel BG95 LTE-M for fleet telemetry
- IP65 industrial enclosure, DIN-rail mountable
- Hardware emergency stop + hardware reverse-current fuse

## EmbeddedOS stack

- eos (real-time kernel)
- eAI (load forecast + fault detection)
- eIPC (fleet ops + remote support)
- eBoot (verified field updates)

## BOM target

~$1,200 (controller only)

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eMeshGrid] graduate to draft`.
2. Stand up `kicad/emeshgrid_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
