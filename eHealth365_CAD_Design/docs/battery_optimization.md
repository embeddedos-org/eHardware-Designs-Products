# Battery Optimization Plan

## Smart Ring Pro — 22mAh LiPo

### Power Modes

| Mode | Avg Current | Battery Life | Active Sensors |
|------|-------------|-------------|----------------|
| **Ultra-low** | 25 µA | 36 days | Accel only (step counting) |
| **Eco** | 60 µA | 15 days | HR + steps + temp |
| **Standard** | 200 µA | 4.5 days | + SpO₂ + EDA + BLE sync |
| **Active** | 1.5 mA | 14 hours | + gas sensor + high-rate PPG |
| **Full scan** | 8 mA | 2.75 hours | All sensors max rate |

### Optimization Techniques

1. **Duty cycling**: PPG LED pulsed at 25 Hz, 100µs per pulse (0.25% duty)
2. **Event-driven wake**: Accelerometer interrupt wakes MCU from System OFF
3. **BLE batching**: Buffer 15 minutes of data, transmit in single burst
4. **Adaptive sample rate**: 25 Hz resting, 100 Hz during exercise
5. **Gas sensor heating**: Pre-heat only when breath sample requested (30 sec)
6. **CPU sleep**: nRF5340 network core handles BLE while app core sleeps

## Smart Patch Pro — 65mAh Silver Oxide

### Power Modes

| Mode | Avg Current | Battery Life | Active Sensors |
|------|-------------|-------------|----------------|
| **Sleep** | 8 µA | 340 days | Nothing (deep sleep) |
| **Eco** | 50 µA | 54 days | CGM only @ 30min |
| **Standard** | 370 µA | 7.3 days | CGM@15min + sweat@4hr + BLE |
| **Active** | 2 mA | 32 hours | + bioZ + pH + real-time sweat |
| **Cartridge** | 10 mA | 6.5 hours | Lab-on-chip analysis |

### Design for 7-Day Patch Life

The 65mAh budget for 7 days = **387 µAh/day** average:
- CGM: 96 samples × 500µA × 30s = 800 µAh
- Sweat: 6 samples × 2mA × 60s = 200 µAh
- BioZ: 3 samples × 1.5mA × 30s = 62 µAh
- BLE: 6 bursts × 5mA × 150s = 7,500 µAh (dominant cost!)
- Sleep: 16hr × 8µA = 128 µAh
- **Total: ~8.7 mAh/day → 7.5 days**

### BLE Optimization (Biggest Power Consumer)

- **Connection interval**: 1000ms (vs 7.5ms default)
- **Payload packing**: Compress 15 min of CGM data into single 100-byte packet
- **Batch transfer**: 6 syncs/day instead of continuous
- **PHY**: Use 2M PHY for faster transfer (halves TX time)
