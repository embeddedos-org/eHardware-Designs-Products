# Smart Patch Pro — Product Datasheet

## Overview

The Smart Patch Pro is the "Chemistry Hub" of the eHealth365 system. Worn on the upper arm as a flexible adhesive "puck," it monitors blood glucose, electrolytes, hydration, and hosts the monthly micro-blood cartridge slot for comprehensive vitamin and mineral analysis.

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Form factor** | Circular adhesive patch — "puck" design |
| **Diameter** | 35mm |
| **Thickness** | 5.5mm (sensor dome) |
| **Weight** | 8.5g (without adhesive backing) |
| **Adhesive** | Medical-grade hydrogel (3M 2477P) |
| **Water resistance** | IP67 — shower & swim safe |
| **Operating temp** | 15°C to 40°C (body-worn) |
| **Wear location** | Back of upper arm (tricep area) |

## 3D Model Specifications

### Outer Shell
- **Geometry**: Circular dome with flat base
- **Material**: Medical-grade ABS + TPU overmold
- **Color**: Skin-tone variants (5 shades)
- **Surface**: Matte finish, smooth edges for comfort

### Cartridge Slide-Dock
- **Location**: Side panel, 8mm × 3mm slot
- **Mechanism**: Spring-loaded slide-in with tactile click
- **Interface**: 6-pin spring-loaded pogo connector
- **Cartridge size**: 10mm × 5mm × 2mm

### Sensor Array (Base)
- **CGM sensor**: Micro-needle array (0.5mm depth, painless insertion)
- **Sweat electrodes**: 4x gold-plated pads (Na⁺, K⁺, Mg²⁺, Zn²⁺ ion-selective)
- **Bioimpedance**: 4-electrode tetrapolar configuration
- **pH sensor**: ISFET (Ion-Sensitive Field-Effect Transistor)
- **Temperature**: Skin contact NTC thermistor

### Flexible PCB
- **PCB type**: 2-layer flex (polyimide substrate)
- **Dimensions**: Circular, 30mm diameter × 0.2mm
- **Components**: All bottom-mounted (skin side: sensors only)

## Electrical Specifications

| Parameter | Specification |
|-----------|--------------|
| **MCU** | Nordic nRF52840 (ARM Cortex-M4F @ 64MHz) |
| **Flash** | 1MB internal |
| **RAM** | 256KB |
| **Wireless** | BLE 5.3 |
| **Battery** | 3.0V silver oxide, 65mAh (SR621SW equivalent, custom shape) |
| **Battery life** | 7 days (matches patch replacement cycle) |
| **Not rechargeable** | Battery replaced with weekly patch swap |

## Sensor Specifications

### CGM (Continuous Glucose Monitor)
| Parameter | Value |
|-----------|-------|
| **Technology** | Enzymatic electrochemical (glucose oxidase) |
| **Micro-needle** | 14-gauge, 0.5mm length, painless insertion |
| **Sample rate** | Every 15 minutes (96 readings/day) |
| **Accuracy** | MARD < 10% |
| **Range** | 40 – 500 mg/dL |
| **Warm-up** | 60 minutes after application |

### Sweat Biosensor Array
| Parameter | Value |
|-----------|-------|
| **Electrodes** | 4x ion-selective electrodes (ISE) |
| **Ions measured** | Na⁺, K⁺, Mg²⁺, Zn²⁺ |
| **Sensitivity** | 55 mV/decade (Nernstian response) |
| **Sample rate** | Every 4 hours (event-triggered during exercise) |
| **Min sweat volume** | 0.1 µL (micro-fluidic collection) |

### Bioimpedance (Hydration)
| Parameter | Value |
|-----------|-------|
| **Configuration** | 4-electrode tetrapolar |
| **Frequency** | Multi-frequency: 5 kHz, 50 kHz, 200 kHz |
| **Measurement** | Resistance + reactance (Cole-Cole model) |
| **Application** | Total body water estimation, cellular hydration |
| **Schedule** | 3x daily |

### pH Sensor
| Parameter | Value |
|-----------|-------|
| **Type** | ISFET (Ion-Sensitive FET) |
| **Range** | pH 4.0 – 8.0 |
| **Resolution** | 0.01 pH |
| **Application** | Skin pH monitoring, metabolic state |

## Monthly Blood Cartridge — Slide-Dock Interface

| Parameter | Specification |
|-----------|--------------|
| **Cartridge size** | 10mm × 5mm × 2mm |
| **Interface** | 6-pin pogo connector (power, SPI, detect) |
| **Micro-needle** | 28-gauge, 1.5mm lancet (spring-loaded) |
| **Sample volume** | 5 µL capillary blood |
| **Analysis time** | 2-4 hours (on-cartridge lab-on-chip) |
| **Analytes** | Vitamins A, C, D, E, K, B1-B12, Folate, Iron, Zinc, Calcium, Magnesium |

### Cartridge Types

| Cartridge | Color Code | Metrics | Frequency | Cost |
|-----------|-----------|---------|-----------|------|
| **Standard sweat** | White | Electrolytes (included in patch) | Weekly | Included |
| **Blood micro** | Gold | All vitamins + B-complex | Monthly | $25 |
| **Mineral** | Silver | Iron, zinc, magnesium, calcium | Monthly | $25 |
| **Full panel** | Blue | All vitamins + all minerals | Quarterly | $60 |

## Power Budget

| Mode | Current | Duration | Daily Energy |
|------|---------|----------|-------------|
| Sleep / standby | 8 µA | 16 hr | 128 µAh |
| CGM sampling | 500 µA | 30 sec × 96 | 800 µAh |
| Sweat analysis | 2 mA | 60 sec × 6 | 200 µAh |
| Bioimpedance | 1.5 mA | 30 sec × 3 | 62 µAh |
| BLE transmit | 5 mA | 15 min × 6 | 7,500 µAh |
| Cartridge analysis | 10 mA | 4 hr (monthly, amortized) | 55 µAh |
| **Total daily** | | | **~8.7 mAh** |
| **Battery** | | | **65 mAh** |
| **Estimated life** | | | **~7.5 days** |
