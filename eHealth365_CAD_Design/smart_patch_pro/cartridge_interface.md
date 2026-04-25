# Smart Patch Pro — Cartridge Interface Specification

## Slide-Dock Mechanical Design

```
PATCH SIDE VIEW (with cartridge slot)

    ┌─────────────────────────────────┐
    │         PATCH BODY              │
    │                                 │
    │   ┌─────────────────────────┐   │
    │   │    CARTRIDGE SLOT   ◄── │ ← Slide-in from side
    │   │   [=================]   │
    │   └─────────────────────────┘   │
    │                                 │
    └─────────────────────────────────┘

CARTRIDGE (top view)
    ┌─────────────────┐
    │  Lab-on-Chip    │  10mm × 5mm × 2mm
    │  ┌───┐ ┌─────┐ │
    │  │ 🩸│ │ASIC │ │  Micro-needle lancet + analysis ASIC
    │  └───┘ └─────┘ │
    │  ▓▓▓▓▓▓        │  6-pin contact pads
    └─────────────────┘
```

## Electrical Interface

| Pin | Name | Direction | Description |
|-----|------|-----------|-------------|
| 1 | VCC | Patch → Cartridge | 3.0V power supply (max 15mA) |
| 2 | GND | Common | Ground |
| 3 | SCK | Patch → Cartridge | SPI clock (1 MHz) |
| 4 | MOSI | Patch → Cartridge | SPI data out |
| 5 | MISO | Cartridge → Patch | SPI data in / results |
| 6 | DET | Cartridge → Patch | Cartridge detect (pulled low when inserted) |

## Cartridge Protocol

### Insertion Sequence
1. User slides cartridge into slot → DET pin goes LOW
2. Patch MCU detects insertion, reads cartridge ID via SPI
3. Patch validates cartridge type and expiry date
4. App notifies user: "Cartridge detected — ready for sampling"

### Blood Sampling Sequence
1. App prompts user to confirm (safety interlock)
2. Patch sends SAMPLE command via SPI
3. Cartridge fires spring-loaded micro-lancet (28G, 1.5mm)
4. Capillary action draws 5µL blood into microfluidic channel
5. Lab-on-chip begins analysis (enzymatic + electrochemical)
6. Results streamed to patch via SPI over 2-4 hours
7. App displays full report when complete

### Cartridge Data Format

```
CARTRIDGE_ID:    4 bytes (unique serial)
TYPE:            1 byte  (0x01=Blood, 0x02=Mineral, 0x03=Full)
EXPIRY:          4 bytes (Unix timestamp)
RESULT_COUNT:    1 byte  (number of analytes)
RESULTS[]:       N × 8 bytes each:
  - ANALYTE_ID:  2 bytes (e.g., 0x0001 = Vitamin A)
  - VALUE:       4 bytes (float32, unit depends on analyte)
  - FLAGS:       2 bytes (0x0001 = in range, 0x0002 = low, 0x0004 = high)
```
