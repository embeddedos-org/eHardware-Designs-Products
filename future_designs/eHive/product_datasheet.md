# 🐝 eHive — Concept Datasheet

> **Status:** Concept (acoustic classifier dataset + microphone placement TBD)
> **Category:** Climate, Food, Water
> **EmbeddedOS components:** eos (low-power kernel), eAI (acoustic classifier on-device), eIPC (LoRa or LTE-M telemetry)

## Tagline

Acoustic + climate beehive monitor for pollinator conservation.

## Why this exists (donor pitch)

One in three bites of food depends on bee pollination, and managed honeybee colony losses run 30–40 % per year. eHive listens to the hive — a $90 monitor that classifies “healthy / queenless / swarming / collapsing” from the sound spectrum and texts the beekeeper before a colony is lost.

## Target users

Smallholder beekeepers, pollinator-conservation NGOs, university apiology programs.

## Suggested donor tier

$500 — equip a 5-hive community apiary for two years.

## Hardware sketch

- ESP32-S3 (built-in Wi-Fi/BLE + I²S microphone interface)
- INMP441 MEMS microphone (omnidirectional, 24-bit I²S)
- HX711 + 200 kg load-cell (hive total weight)
- SHT41 internal hive T/RH probe
- Quectel BG95 LTE-M (or RFM95 LoRa) for cellular-free regions
- 2 W solar panel + 18650 cell + TP4056 charge IC
- IP55 weather-resistant enclosure mountable under hive lid

## EmbeddedOS stack

- eos (low-power kernel)
- eAI (acoustic classifier on-device)
- eIPC (LoRa or LTE-M telemetry)

## BOM target

~$90

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eHive] graduate to draft`.
2. Stand up `kicad/ehive_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
