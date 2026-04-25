# Smart Sensing Strategy — "Sample & Store" Model

> **Core Principle**: Don't monitor 24/7 — monitor smartly at the right intervals.

## Sensing Schedule Framework

### Continuous (Always On) — Low Power Only

| Sensor | Device | Metric | Why Continuous | Current Draw |
|--------|--------|--------|----------------|-------------|
| PPG (HR) | 💍 Ring | Heart rate, HRV | Emergency detection | 45 µA |
| SpO₂ | 💍 Ring | Oxygen saturation | Critical safety | (shared with PPG) |
| Accelerometer | 💍 Ring | Movement, steps | Very low power | 12 µA |
| Temperature | 💍 Ring | Body temp | Infection detection | 3 µA |

### Periodic Sensing — Scheduled Bursts

| Sensor | Device | Metric | Frequency | Duration |
|--------|--------|--------|-----------|----------|
| CGM | 🩹 Patch | Blood glucose | Every 15 min | 30 sec |
| Sweat biosensor | 🩹 Patch | Electrolytes | Every 4 hours | 60 sec |
| Bioimpedance | 🩹 Patch | Hydration level | 3× daily | 30 sec |
| Skin pH | 🩹 Patch | Metabolic state | Every 4 hours | 15 sec |
| Skin conductance | 💍 Ring | Hydration hint | Every 4 hours | 10 sec |
| Breath port | 💍 Ring | Ketones | Morning & evening | 30 sec |

### Event-Triggered Sensing

| Trigger | Sensor Activated | Device |
|---------|-----------------|--------|
| Meal detected (HR + glucose rise) | CGM high-rate + digestion tracking | 🩹 Patch |
| Workout detected (HR + accel) | Electrolyte + lactate recovery scan | 🩹 Patch |
| Wake-up detected (movement) | Full morning health snapshot | Both |
| Before sleep (stillness) | HRV + stress + readiness score | 💍 Ring |
| User taps device | Manual full scan on demand | Both |
| Anomaly (low SpO₂, high HR) | Continuous high-rate monitoring | 💍 Ring |

### Weekly / Monthly

| Metric | Method | Frequency | Device |
|--------|--------|-----------|--------|
| Vitamins (A, D, B12, etc.) | Micro blood-draw cartridge | Monthly | 🩹 Patch |
| Iron, zinc, magnesium | Same micro blood cartridge | Monthly | 🩹 Patch |
| Full vitamin + mineral panel | Full panel cartridge | Quarterly | 🩹 Patch |

## Battery Optimization Modes

| Mode | Ring Battery | Patch Battery | What's Active |
|------|-------------|--------------|---------------|
| **Eco mode** | 7 days | N/A | HR + steps + temp only |
| **Standard mode** | 3-4 days | 7 days | + glucose + sweat every 4hr |
| **Full scan mode** | 16 hours | 3 days | All sensors active |
| **Sleep mode** | Passive | Passive | SpO₂ + HRV + glucose@30min |
