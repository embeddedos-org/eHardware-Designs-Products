# Smart Patch Pro — 3D Model Specifications

## Exploded View

```
        ┌──────────────────────────────┐
  ①     │   ABS/TPU Top Shell (dome)   │  Skin-tone, matte finish
        │   ┌──────────┐               │
        │   │CARTRIDGE │ ◄── Side slot │  Slide-dock for monthly cartridge
        │   │  SLOT    │               │
        │   └──────────┘               │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ②     │   Flex PCB (circular)        │  2-layer polyimide, 30mm Ø
        │   ┌─────────────────────┐    │
        │   │ nRF52840  AD5940   │    │  MCU + Analog AFE
        │   │ ADS1292R  LMP91000 │    │  CGM ADC + Potentiostat
        │   │ TMP117   Cart.Ctrl │    │  Temp + Cartridge
        │   └─────────────────────┘    │
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ③     │   Silver Oxide Battery       │  65mAh, non-rechargeable
        │   (coin cell, custom shape)  │  Replaced with weekly patch
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ④     │   Sensor Array Substrate     │  Flexible sensor platform
        │   ╔═══╗ ╔═══╗ ╔═══╗ ╔═══╗  │
        │   ║Na⁺║ ║K⁺ ║ ║Mg²║ ║Zn²║  │  4× ISE sweat electrodes
        │   ╚═══╝ ╚═══╝ ╚═══╝ ╚═══╝  │
        │   [BioZ] [BioZ] [BioZ] [BZ] │  4× bioimpedance electrodes
        │         ┌─────┐              │
        │         │ CGM │              │  CGM micro-needle array
        │         │needle│              │
        │         └─────┘              │
        │         [pH ISFET]           │  pH sensor
        └──────────┬───────────────────┘
                   │
        ┌──────────▼───────────────────┐
  ⑤     │   Medical Adhesive Backing   │  3M 2477P hydrogel
        │   (breathable, hypoallergenic)│  7-day wear, easy peel
        └──────────────────────────────┘
```

## CAD Dimensions

| Component | Diameter | Thickness | Notes |
|-----------|----------|-----------|-------|
| **Top shell** | 35mm | 4.0mm (dome height) | Injection molded ABS+TPU |
| **Cartridge slot** | 8mm × 3mm opening | 2.5mm deep | Side-access |
| **Flex PCB** | 30mm | 0.2mm | All SMD bottom-mount |
| **Battery** | 28mm | 1.5mm | Custom coin shape |
| **Sensor substrate** | 30mm | 0.5mm | Includes micro-needles |
| **Adhesive** | 40mm (overhang) | 0.3mm | Extends beyond shell |
| **Total patch** | 35mm body / 40mm adhesive | 5.5mm peak | 8.5g without adhesive |

## Skin-Tone Color Variants

| Variant | Pantone | Hex Code | Target Demographic |
|---------|---------|----------|-------------------|
| Porcelain | 7527 C | #D4C5B0 | Fair |
| Sand | 7508 C | #C4A77D | Light-medium |
| Caramel | 7516 C | #99724A | Medium |
| Mocha | 7518 C | #7A5C4F | Medium-dark |
| Espresso | 7519 C | #5C4033 | Dark |

## 3D Printing Prototyping

| Stage | Method | Material | Resolution |
|-------|--------|----------|-----------|
| Form check | FDM | TPU 95A | 0.2mm |
| Fit + comfort | SLA | Flexible Resin | 0.05mm |
| Sensor mockup | Multi-material | Rigid + Flex | 0.05mm |
| Pre-production | Injection mold | ABS + TPU overmold | Production-grade |
