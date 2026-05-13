# 🧠 eBCI-Lite — Concept Datasheet

> **Status:** Concept (electrode placement + intent decoder TBD)
> **Category:** Health, Accessibility, Dignity
> **EmbeddedOS components:** eos (kernel), eNI (BCI signal pipeline + safety policy), eAI (intent classifier), eIPC (caregiver dashboard)

## Tagline

Affordable 8-channel dry-electrode EEG headband + AAC keyboard.

## Why this exists (donor pitch)

ALS / locked-in / late-stage stroke patients today rely on $15 K+ eye-tracker AAC devices that fail when eye control fails. eBCI-Lite targets a $300 BOM dry EEG headband + open intent decoder so a patient can spell words using cortical signals when eyes can no longer move.

## Target users

ALS / locked-in / late-stage stroke / cerebral palsy patients; speech-language pathologists.

## Suggested donor tier

$10 K — equip one neurology clinic with 30 evaluation units.

## Hardware sketch

- nRF5340 dual-core BLE 5.3 MCU
- ADS1299 8-channel 24-bit EEG front-end (dry electrodes)
- 8× passive dry electrodes (gold-plated spring contacts)
- BNO086 IMU for motion-artefact rejection
- 600 mAh LiPo + USB-C charging
- On-device beep/LED feedback; no display
- Companion tablet app: AAC keyboard with row-column scanning

## EmbeddedOS stack

- eos (kernel)
- eNI (BCI signal pipeline + safety policy)
- eAI (intent classifier)
- eIPC (caregiver dashboard)

## BOM target

~$300

> Full BOM placeholder lives at [`bom.csv`](bom.csv). Schematics will be
> added under `kicad/` when the design graduates from concept to draft.

## Status

This page is a **concept-stage placeholder**. It exists so that donors,
contributors, and curators can browse the design as a real GitHub URL
before any silicon is committed.

To take this design to draft:

1. Open an issue on
   [embeddedos-org/eCAD-Hardware-Products](https://github.com/embeddedos-org/eCAD-Hardware-Products/issues/new)
   titled `[future_designs/eBCI-Lite] graduate to draft`.
2. Stand up `kicad/ebci_lite_schematic.kicad_sch` and start filling in
   the BOM at [`bom.csv`](bom.csv).
3. Cross-reference the eFab manifest if a curated stack profile makes
   sense (e.g. `eai-edge` for designs that lean on ENI + EIPC + eAI).

See the org-wide guide at
[`embeddedos-org/.github/CONTRIBUTING.md`](https://github.com/embeddedos-org/.github/blob/main/CONTRIBUTING.md).
