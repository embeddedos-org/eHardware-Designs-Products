# 🧠 eBCI-Lite — Business / Donor Plan (concept)

> **Status:** Concept (electrode placement + intent decoder TBD)
> **Donor tier:** $10 K — equip one neurology clinic with 30 evaluation units.

## What a donor funds

ALS / locked-in / late-stage stroke patients today rely on $15 K+ eye-tracker AAC devices that fail when eye control fails. eBCI-Lite targets a $300 BOM dry EEG headband + open intent decoder so a patient can spell words using cortical signals when eyes can no longer move.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$300 |
| BOM (qty 1k) | ~$190 |
| Clinical validation study | ~$200 K (one-time, partnered) |
| Regulatory (Class II AAC) | ~$80 K |

## Regulatory path

FDA Class II (Augmentative and Alternative Communication); CE MDR; IRB for any patient study.

## Go-to-market / distribution

Pilot at 3 academic medical centres; donor-funded loaner pool while regulatory clears.

## EmbeddedOS components leveraged

- eos (kernel)
- eNI (BCI signal pipeline + safety policy)
- eAI (intent classifier)
- eIPC (caregiver dashboard)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
