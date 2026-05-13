# 🤖 eHand — Concept Datasheet

> **Status:** Concept (mechanical sketch + EMG decoder algorithm TBD)
> **Category:** Health, Accessibility, Dignity
> **EmbeddedOS components:** eos (kernel), eNI (EMG signal pipeline), eAI (gesture intent classifier), eBoot (firmware updates)

## Tagline

Open-source 6-DOF myoelectric prosthetic hand with EMG control.

## Why this exists (donor pitch)

65 million amputees worldwide. Commercial myoelectric hands cost $30–60 K. eHand targets a $1.5 K BOM with comparable degrees of freedom, 3D-printable socket, and a published surgeon-fitting guide — turning a multi-decade insurance fight into a weekend clinic.

## Target users

Below-elbow amputees, prosthetists, rehabilitation clinics in low/middle-income countries.

## Suggested donor tier

$2 K — fund one full eHand build for a single recipient.

## Hardware sketch

- STM32H7 motor-control MCU
- 6× brushless servos (Dynamixel-XL or equivalent) for finger joints
- 8× surface-EMG channels (ADS1299 24-bit ADC, IEC 60601 isolated front-end)
- 6-DOF IMU + force-sensing fingertips (FSR402)
- CAN-FD between MCU and limb-controller for low-latency motion
- 3D-printable thermoplastic socket (custom per recipient)
- 7.4 V / 2200 mAh LiPo + battery management (BQ40Z80)

## EmbeddedOS stack

- eos (kernel)
- eNI (EMG signal pipeline)
- eAI (gesture intent classifier)
- eBoot (firmware updates)

## BOM target

~$1,500

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eHand] graduate to draft`.
2. Stand up `kicad/ehand_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
