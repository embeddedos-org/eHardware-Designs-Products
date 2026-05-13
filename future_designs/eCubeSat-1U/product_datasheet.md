# 🛰️ eCubeSat-1U — Concept Datasheet

> **Status:** Concept (radiation budget + magnetorquer control law TBD)
> **Category:** Infrastructure & Frontier
> **EmbeddedOS components:** eos (real-time kernel), eBoot (rad-tolerant A/B updates), eIPC (telemetry framing), eAI (on-board image classification)

## Tagline

1U CubeSat reference design with EmbeddedOS as flight software.

## Why this exists (donor pitch)

A foundation-funded student satellite ride-share launch starts at ~$30 K. eCubeSat-1U is the open hardware + flight-software stack that gets a class — or a country — to orbit. Magnetorquer ADCS, rad-tolerant A/B firmware updates, on-board image classification.

## Target users

Universities, secondary-school space clubs, national space agencies in emerging space programs.

## Suggested donor tier

$30 K — sponsor one student-built satellite from build to launch.

## Hardware sketch

- 1U aluminium 6061 CubeSat frame (10×10×10 cm)
- AMD Kintex Ultrascale rad-tolerant FPGA
- Apollo4 Plus radiation-hardened-by-design MCU
- 4× GaAs deployable solar wings (~7 W EOL)
- 3× magnetorquer rods + 3-axis MEMS magnetometer (ADCS)
- RFM95 + custom UHF amateur-band transceiver (435 MHz)
- 2 MP camera (visible + filter wheel optional)
- Li-ion 4-cell battery pack with redundant cell-balancing
- Watchdog + hardware reset + redundant comm path

## EmbeddedOS stack

- eos (real-time kernel)
- eBoot (rad-tolerant A/B updates)
- eIPC (telemetry framing)
- eAI (on-board image classification)

## BOM target

~$8,000 (flight hardware)

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eCubeSat-1U] graduate to draft`.
2. Stand up `kicad/ecubesat_1u_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
