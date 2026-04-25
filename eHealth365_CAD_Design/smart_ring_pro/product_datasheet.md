# Smart Ring Pro — Product Datasheet

## Overview

The Smart Ring Pro is the "Vitality Hub" of the eHealth365 system. Worn continuously on the finger, it monitors the autonomic nervous system, movement, and respiratory metabolites through a compact titanium/ceramic chassis.

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Ring — sizes 6-13 (US) |
| **Chassis material** | Grade 5 Titanium (outer) / Ceramic (inner variant) |
| **Inner band** | Medical-grade silicone with sensor windows |
| **Weight** | 4g (titanium) / 3.8g (ceramic) |
| **Width** | 8mm |
| **Thickness** | 2.5mm |
| **Water resistance** | IP68 — 100m / 10 ATM |
| **Operating temp** | 0°C to 45°C |
| **Display** | None (haptic-only feedback) |

## 3D Model Specifications

### Outer Shell
- **Geometry**: Toroidal ring with chamfered edges
- **Material**: Titanium Grade 5 (Ti-6Al-4V) — density 4.43 g/cm³
- **Surface finish**: PVD coating (Black, Silver, Gold options)
- **Tolerance**: ±0.05mm CNC machined

### Inner Sensor Band
- **Material**: Liquid silicone rubber (LSR), Shore A 40
- **Sensor windows**: 3x optical windows (sapphire glass, 2mm diameter)
- **Electrode pads**: 2x gold-plated EDA electrodes for skin conductance
- **Breath port**: 1x micro-channel (0.5mm bore) for ketone sampling

### PCB Assembly
- **PCB type**: 4-layer rigid-flex (0.3mm total thickness)
- **Shape**: Curved arc, 220° wrap around ring interior
- **Dimensions**: 22mm × 5mm × 0.3mm (varies by ring size)

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **MCU** | Nordic nRF5340 (dual-core ARM Cortex-M33 @ 128MHz + M33 @ 64MHz) |
| **Flash** | 1MB internal + 4MB external QSPI NOR |
| **RAM** | 512KB |
| **Wireless** | BLE 5.3 (Long Range, 2 Mbps) |
| **Battery** | 3.7V LiPo, 22mAh (custom form factor) |
| **Charging** | Qi wireless, 5V/100mA |
| **Battery life** | 4-5 days (standard mode) |

## Sensor Specifications

### Optical PPG (Heart Rate + SpO₂)
| Parameter | Value |
|-----------|-------|
| **Sensor** | ams OSRAM AS7058 (3-channel PPG) |
| **LEDs** | Green (525nm) × 2, Red (660nm) × 1, IR (940nm) × 1 |
| **Photodiodes** | 3x silicon PD, 0.5mm² each |
| **Sample rate** | 25 Hz (standard), 100 Hz (sleep/workout) |
| **HR accuracy** | ±2 BPM (resting), ±5 BPM (exercise) |
| **SpO₂ accuracy** | ±2% (70-100% range) |
| **HRV metrics** | RMSSD, SDNN, pNN50, LF/HF ratio |

### Temperature
| Parameter | Value |
|-----------|-------|
| **Sensor** | Melexis MLX90632 (medical-grade IR thermometer) |
| **Accuracy** | ±0.1°C |
| **Range** | 25°C – 45°C |
| **Sample rate** | 1 Hz continuous |

### Accelerometer
| Parameter | Value |
|-----------|-------|
| **Sensor** | Bosch BMA456 (3-axis MEMS) |
| **Range** | ±2g / ±4g / ±8g / ±16g |
| **Resolution** | 16-bit |
| **Sample rate** | 50 Hz (activity), 25 Hz (sleep) |
| **Step accuracy** | ±3% |

### Skin Conductance (EDA)
| Parameter | Value |
|-----------|-------|
| **Electrodes** | 2x gold-plated dry electrodes |
| **Measurement** | AC impedance, 1 kHz excitation |
| **Range** | 0.01 – 100 µS |
| **Application** | Hydration estimation, stress arousal detection |

### Breath Port (Ketones)
| Parameter | Value |
|-----------|-------|
| **Sensor** | SGX Sensortech MiCS-6814 (MOX gas sensor) |
| **Target gases** | Acetone (ketone marker), humidity |
| **Detection range** | 0.1 – 50 ppm acetone |
| **Sampling** | User exhales near ring, 2x daily |

## Pin Assignments (nRF5340)

| Pin | Function | Peripheral |
|-----|----------|-----------|
| P0.04 | PPG_LED_GREEN_1 | PWM |
| P0.05 | PPG_LED_GREEN_2 | PWM |
| P0.06 | PPG_LED_RED | PWM |
| P0.07 | PPG_LED_IR | PWM |
| P0.08-10 | PPG_PD_1/2/3 | SAADC |
| P0.11 | TEMP_SDA | TWIM0 |
| P0.12 | TEMP_SCL | TWIM0 |
| P0.13 | ACCEL_SDA | TWIM1 |
| P0.14 | ACCEL_SCL | TWIM1 |
| P0.15 | ACCEL_INT1 | GPIOTE |
| P0.16 | EDA_EXCITE | PWM |
| P0.17 | EDA_SENSE | SAADC |
| P0.18 | GAS_HEATER | GPIO |
| P0.19 | GAS_SENSE | SAADC |
| P0.20 | HAPTIC_EN | PWM |
| P0.21 | CHG_STATUS | GPIO |
| P0.22 | QSPI_SCK | QSPI |
| P0.23 | QSPI_CSN | QSPI |
| P0.24-27 | QSPI_D0-D3 | QSPI |

## Power Budget

| Mode | Current | Duration | Daily Energy |
|------|---------|----------|-------------|
| Sleep tracking | 45 µA | 8 hr | 360 µAh |
| Idle (HR only) | 80 µA | 10 hr | 800 µAh |
| Active sensing | 1.2 mA | 4 hr | 4,800 µAh |
| BLE transmit | 5.5 mA | 2 hr | 11,000 µAh |
| Breath sample | 8 mA | 30 sec × 2 | 133 µAh |
| **Total daily** | | | **~17.1 mAh** |
| **Battery** | | | **22 mAh** |
| **Estimated life** | | | **~4.5 days** |
