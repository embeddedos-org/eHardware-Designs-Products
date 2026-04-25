# Urban Drone — eVTOL Product Datasheet

## Overview

The Urban Drone is a 4-seat electric vertical takeoff and landing (eVTOL) aircraft designed for city-to-city commuting. Solar-hybrid power with solid-state batteries provides near-zero operating cost after initial purchase.

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Type** | eVTOL (tilt-rotor configuration) |
| **Seats** | 4 (1 pilot/autonomous + 3 passengers) |
| **Wingspan** | 12m (rotors extended) / 4m (folded) |
| **Length** | 7.5m |
| **Height** | 2.8m (landing gear extended) |
| **Empty weight** | 850 kg |
| **MTOW** | 1,400 kg |
| **Payload** | 400 kg (4 passengers + luggage) |
| **Body material** | Carbon-fiber/aerogel composite |
| **Canopy** | Electrochromic smart glass |

## Performance

| Parameter | Specification |
|-----------|--------------|
| **Range** | 300-500 km (battery + solar) |
| **Cruise speed** | 250 km/h |
| **Max speed** | 320 km/h |
| **Service ceiling** | 500m (urban air corridor) |
| **Hover endurance** | 45 minutes |
| **Takeoff/landing** | Vertical (VTOL) — 8m x 8m pad |
| **Noise** | <65 dB at 75m (whisper-quiet DEP) |
| **Autonomy** | Level 4 autonomous (pilot optional) |

## Propulsion

| Parameter | Specification |
|-----------|--------------|
| **Configuration** | 8x tilt-rotors (distributed electric propulsion) |
| **Motors** | 8x 50kW permanent magnet synchronous (400kW total) |
| **Props** | 8x 1.5m diameter, 5-blade, variable pitch |
| **Tilt mechanism** | 0-90 degree tilt (VTOL to cruise transition) |
| **Redundancy** | Fly-safe with 2 motors failed |

## Power System

| Parameter | Specification |
|-----------|--------------|
| **Solar panels** | 18m2 flexible perovskite cells (roof + wing upper surface) |
| **Solar efficiency** | 28% (tandem perovskite/silicon) |
| **Solar output** | 5.4 kW peak (in-flight), 3.2 kW average |
| **Battery** | 120 kWh solid-state lithium (QuantumScape-class) |
| **Battery energy density** | 500 Wh/kg |
| **Battery weight** | 240 kg |
| **H2 fuel cell (optional)** | 30 kW PEM range extender |
| **Regen braking** | Descent energy recapture (rotors as generators) |
| **Charging** | 400V DC fast-charge (20 min to 80%) |
| **V2G** | Bidirectional — vehicle-to-grid energy resale |

## Avionics

| System | Component |
|--------|-----------|
| **Flight controller** | Triple-redundant EoS RTOS (ARM Cortex-R52) |
| **Navigation** | GPS/Galileo/BeiDou + INS + visual SLAM |
| **Obstacle avoidance** | 8x LiDAR + 12x cameras (360-degree) |
| **Communication** | 5G-NR + satellite link (Starlink) |
| **ADS-B** | Mode S transponder (FAA compliant) |
| **Autopilot** | eAI Level 4 autonomous flight |
| **Passenger display** | 15" touchscreen (flight info, entertainment) |
| **Emergency** | Ballistic parachute system (BPS) |

## Estimated Pricing

| Variant | Price |
|---------|-------|
| **Standard** (battery only) | $85,000 |
| **Extended range** (+ H2 fuel cell) | $105,000 |
| **Premium** (full autonomous + luxury interior) | $120,000 |

## Certification

| Authority | Standard | Status |
|-----------|---------|--------|
| FAA | Part 135 (air taxi) | In progress |
| EASA | SC-VTOL | In progress |
| CAA (UK) | CAP 2505 | Planned |
