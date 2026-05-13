# 👓 eVision — Concept Datasheet

> **Status:** Concept (datasheet draft, KiCad schematic TBD)
> **Category:** Health, Accessibility, Dignity
> **EmbeddedOS components:** eos (kernel + HAL), eAI (on-device object recognition), eIPC (companion-app sync)

## Tagline

Wearable obstacle-detection band for blind and low-vision users.

## Why this exists (donor pitch)

285 million visually-impaired people globally. Commercial obstacle-detection wearables sit at $4 K and up. eVision targets a $200 BOM with the same core capability, paired with an open hardware design so any local repair shop can service it.

## Target users

Blind and low-vision users, mobility trainers, occupational therapists, NGOs distributing assistive tech.

## Suggested donor tier

$5 K — sponsor 25 production units for a school for the blind.

## Hardware sketch

- STM32H7 host MCU (Cortex-M7, 480 MHz, FPU)
- 4× VL53L7CX time-of-flight ranging sensors (front-quadrant 90° FOV)
- BNO086 9-DOF IMU (dead-reckoning + heading)
- 8× LRA haptic actuators on a wristband (DRV2605L driver)
- Bone-conduction speaker (SPI8 4 W class-D)
- 3.7 V / 1500 mAh LiPo + USB-C PD charging
- BLE 5.3 (nRF52840 module) for companion-app pairing

## EmbeddedOS stack

- eos (kernel + HAL)
- eAI (on-device object recognition)
- eIPC (companion-app sync)

## BOM target

~$200

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eVision] graduate to draft`.
2. Stand up `kicad/evision_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
