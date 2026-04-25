# Smart Ring Pro — Manufacturing Notes

## PCB Fabrication

| Parameter | Specification |
|-----------|--------------|
| **Layer count** | 4 layers (rigid-flex) |
| **Material** | FR-4 rigid + polyimide flex |
| **Copper weight** | 0.5 oz (inner), 1 oz (outer) |
| **Min trace/space** | 75µm / 75µm |
| **Min via** | 150µm laser drill |
| **Surface finish** | ENIG (Electroless Nickel Immersion Gold) |
| **Impedance control** | 50Ω single-ended, 100Ω differential |
| **Flex bend radius** | 2mm minimum (ring curvature) |

## Assembly Process

1. **SMT placement** — Pick-and-place for all 0201/0402 passives and QFN/WLCSP ICs
2. **Reflow** — Lead-free SAC305, peak 245°C, nitrogen atmosphere
3. **Sensor alignment** — PPG LEDs/PDs require ±50µm placement accuracy for optical alignment
4. **Wire bonding** — None (all WLCSP/QFN)
5. **Flex bending** — PCB bent to ring curvature after SMT, secured with adhesive
6. **Encapsulation** — Medical-grade silicone potting compound over PCB
7. **Shell assembly** — PCB + battery press-fit into titanium/ceramic shell
8. **Qi coil** — Bonded to flat segment of ring interior
9. **Seal test** — IP68 pressure test (1 bar, 30 minutes)

## Quality Control

- **AOI** (Automated Optical Inspection) after reflow
- **X-ray** inspection for WLCSP solder joints
- **Functional test**: PPG signal quality, BLE RSSI, accelerometer self-test
- **Charging test**: Qi alignment, charge current, thermal
- **Haptic test**: LRA resonant frequency verification (175 Hz ± 5%)
- **IP68 test**: Pressure chamber submersion
