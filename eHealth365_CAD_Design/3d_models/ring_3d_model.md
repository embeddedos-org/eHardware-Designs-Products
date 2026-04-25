# Smart Ring Pro — 3D Model Specifications

## Exploded View

```
        ┌──────────────────────────────┐
  ①     │   Titanium Outer Shell       │  CNC machined, PVD coated
        │   (toroidal, chamfered)      │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ②     │   Qi Wireless Charging Coil  │  Flat segment, bonded to shell
        │   (15mm × 5mm, 10 turns)     │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ③     │   Rigid-Flex PCB Assembly    │  4-layer, 220° arc
        │   ┌─────────────────────┐    │
        │   │ nRF5340  AS7058     │    │  MCU + PPG AFE
        │   │ BMA456   MLX90632  │    │  Accel + Temp
        │   │ MiCS6814 BQ25125   │    │  Gas + Charger
        │   │ DRV2603            │    │  Haptic driver
        │   └─────────────────────┘    │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ④     │   LiPo Battery (22mAh)      │  Custom curved form factor
        │   (arc-shaped pouch cell)    │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ⑤     │   Silicone Inner Band        │  Medical-grade LSR, Shore A 40
        │   ┌───┐ ┌───┐ ┌───┐        │
        │   │PPG│ │PPG│ │PPG│        │  3× sapphire optical windows
        │   └───┘ └───┘ └───┘        │
        │   [EDA]       [EDA]        │  2× skin conductance electrodes
        │        ⊙                    │  1× breath micro-port
        └──────────────────────────────┘
```

## CAD Dimensions (Size 10 US)

| Component | Inner Ø | Outer Ø | Width | Thickness |
|-----------|---------|---------|-------|-----------|
| **Outer shell** | 19.8mm | 22.8mm | 8.0mm | 1.5mm wall |
| **Inner band** | 19.0mm | 19.8mm | 8.0mm | 0.4mm |
| **PCB arc** | — | 19.4mm (radius) | 5.0mm | 0.3mm |
| **Battery** | — | — | 5.0mm | 1.5mm |
| **Total ring** | 19.0mm | 22.8mm | 8.0mm | 2.6mm radial |

## Ring Size Variants

| US Size | Inner Ø | Inner Circ | PCB Arc Length |
|---------|---------|-----------|----------------|
| 6 | 16.5mm | 51.8mm | 31.7mm |
| 7 | 17.3mm | 54.3mm | 33.2mm |
| 8 | 18.1mm | 56.9mm | 34.8mm |
| 9 | 18.9mm | 59.4mm | 36.3mm |
| 10 | 19.8mm | 62.2mm | 38.0mm |
| 11 | 20.6mm | 64.7mm | 39.6mm |
| 12 | 21.4mm | 67.2mm | 41.1mm |
| 13 | 22.2mm | 69.7mm | 42.6mm |

## Material Specifications

| Component | Material | Properties |
|-----------|----------|-----------|
| Outer shell | Ti-6Al-4V (Grade 5) | Density 4.43 g/cm³, yield 880 MPa, biocompatible |
| Outer shell (alt) | Yttria-stabilized zirconia (ZrO₂) | Density 6.05 g/cm³, scratch-resistant |
| Inner band | Liquid silicone rubber (LSR) | Shore A 40, USP Class VI biocompatible |
| Optical windows | Sapphire (Al₂O₃) | Mohs 9, >85% transmission at 525-940nm |
| EDA electrodes | Gold (Au) plating on Cu | 0.5µm Au over 5µm Ni |
| Breath port tube | Medical-grade PTFE | 0.5mm ID, chemically inert |

## 3D Printing Prototyping

| Prototype Stage | Method | Material | Resolution |
|----------------|--------|----------|-----------|
| Form check | FDM | PLA | 0.2mm |
| Fit check | SLA | Tough Resin | 0.05mm |
| Functional proto | SLM (metal) | Ti-6Al-4V | 0.04mm |
| Pre-production | CNC machining | Ti-6Al-4V | ±0.05mm |
