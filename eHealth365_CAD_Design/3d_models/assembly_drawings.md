# eHealth365 — Assembly & System Integration

## Two-Device System Layout

```
         HUMAN BODY — SENSOR PLACEMENT

              ┌─────────┐
              │  HEAD    │
              └────┬─────┘
                   │
         ┌────────┼────────┐
         │  LEFT  │  RIGHT │
    ┌────┤  ARM   │  ARM   ├────┐
    │    │        │        │    │
    │    │   🩹   │        │    │   🩹 = Smart Patch Pro
    │    │ PATCH  │        │    │       (back of upper arm)
    │    │        │        │    │
    │    └───┬────┴───┬────┘    │
    │        │        │         │
    💍       │        │         │   💍 = Smart Ring Pro
   RING      │        │         │       (any finger, dominant hand)
    │        │        │         │
    └────────┴────────┴─────────┘
```

## Data Flow Architecture

```
   SENSE              EDGE COMPUTE          SYNC              AI ENGINE
   ─────              ────────────          ────              ─────────

  💍 Ring              Ring MCU             BLE 5.3           📱 App
  ┌─────┐            ┌──────────┐         ┌──────┐         ┌──────────┐
  │PPG  ├───────────►│ Filter   ├────────►│ 15-  ├────────►│ Digital  │
  │Accel│            │ noise    │         │ min  │         │ Twin     │
  │Temp │            │ extract  │         │ sync │         │          │
  │EDA  │            │ features │         │      │         │ Combine  │
  │Gas  │            └──────────┘         └──────┘         │ Chemical │
  └─────┘                                                  │ +Physical│
                                                           │ data     │
  🩹 Patch            Patch MCU            BLE 5.3         │          │
  ┌─────┐            ┌──────────┐         ┌──────┐        │ Generate │
  │CGM  ├───────────►│ Glucose  ├────────►│ 15-  ├───────►│ insights │
  │Sweat│            │ algo     │         │ min  │        │ + alerts │
  │BioZ │            │ ISE cal  │         │ sync │        │          │
  │pH   │            │ impedance│         │      │        │ Share    │
  │Cart.│            └──────────┘         └──────┘        │ w/doctor │
  └─────┘                                                 └──────────┘
```

## Packaging — What Ships in the Box

```
┌─────────────────────────────────────────────┐
│                 eHealth365                   │
│             ┌───────────────┐               │
│             │  💍 Smart     │               │
│             │  Ring Pro     │               │
│             │  + Charger    │               │
│             └───────────────┘               │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │  🩹 Smart Patch Pro Starter Kit     │   │
│  │  • 4× weekly patches               │   │
│  │  • 1× monthly blood cartridge      │   │
│  │  • Application tool                 │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────┐  ┌─────────────────┐      │
│  │ Quick Start │  │ Sizing Kit      │      │
│  │ Guide       │  │ (Ring sizes)    │      │
│  └─────────────┘  └─────────────────┘      │
└─────────────────────────────────────────────┘
```
