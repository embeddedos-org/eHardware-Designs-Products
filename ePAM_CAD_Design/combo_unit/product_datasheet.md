# Combo Unit — Trans-Atmospheric Vehicle Product Datasheet

## Overview

The Combo Unit is the ultimate vehicle: a 4-seat craft that operates as an urban drone (low altitude), transitions through the atmosphere, and reaches suborbital space. The "Trans-Atmospheric" design handles both aerodynamic lift (drone mode) and reaction mass (space mode).

## Physical Specifications

| Parameter | Specification |
|-----------|--------------|
| **Type** | Trans-atmospheric hybrid (eVTOL + suborbital) |
| **Seats** | 4 (1 pilot + 3 passengers) |
| **Length** | 11m |
| **Wingspan** | 10m (rotors) / 6m (wings only, rotors retracted) |
| **Height** | 3.5m |
| **Empty weight** | 2,800 kg |
| **MTOW** | 4,800 kg |
| **Body material** | Ti-6Al-4V frame + carbon-fiber/aerogel skin + ceramic TPS |

## Trans-Atmospheric Flight Profile

```
ALTITUDE
100km  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ KARMAN LINE ─ ─ ─ ─ ─ ─
                              ╱ ╲
                            ╱     ╲    SPACE MODE
                          ╱ Solar-  ╲   (Solar-thermal +
                        ╱  thermal   ╲   RCS thrusters)
30km   ─ ─ ─ ─ ─ ─ ─╱─ ─ ─ ─ ─ ─ ─ ╲─ ─ ─ ─ ─ ─ ─ ─ ─
                    ╱                   ╲
                  ╱  TRANSITION          ╲  TRANSITION
                ╱    (Rotors retract,      ╲ (Rotors deploy,
              ╱       rocket ignites)       ╲  glide descent)
500m   ─ ─ ╱─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╲─ ─ ─ ─ ─ ─
          ╱                                   ╲
        ╱   DRONE MODE                         ╲  DRONE MODE
      ╱     (8x tilt-rotors, DEP)                ╲ (VTOL landing)
0m  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    TAKEOFF                                      LANDING
```

## Operating Modes

| Mode | Altitude | Propulsion | Speed |
|------|----------|-----------|-------|
| **Drone** | 0-500m | 8x electric tilt-rotors | 0-300 km/h |
| **Transition** | 500m-30km | Rotors retract + hybrid rocket ignites | 300-1,500 km/h |
| **Space** | 30km-100km+ | Solar-thermal rocket + RCS | Mach 3+ |
| **Re-entry** | 100km-500m | Glide + thermal protection | Controlled descent |
| **Landing** | 500m-0 | Rotors deploy + VTOL | 0-50 km/h |

## Propulsion

| System | Specification |
|--------|--------------|
| **Drone rotors** | 8x 75kW PMSM tilt-rotor (retractable into body) |
| **Hybrid rocket** | 200 kN thrust (HTPB + N2O) — atmospheric climb |
| **Solar-thermal** | 25 kN thrust (concentrated sunlight heats H2) |
| **RCS** | 16x cold gas N2 thrusters |
| **Total drone power** | 600 kW electric |
| **Total rocket thrust** | 225 kN |

## Power System

| Parameter | Specification |
|-----------|--------------|
| **Solar (atmospheric)** | 20m2 perovskite cells (wings + body) |
| **Solar (space)** | 30m2 deployable GaAs panels |
| **Battery** | 150 kWh solid-state (drone mode + avionics) |
| **H2 fuel cell** | 50 kW PEM (transition power + backup) |
| **H2 storage** | 15 kg compressed H2 (700 bar Type IV tanks) |

## Estimated Pricing

| Model | Price |
|-------|-------|
| **Full vehicle** | $5M - $9M |
| **1/16th fractional share** | $400,000 (25 flight hours/year) |
| **Managed fleet unit** | $7M (includes 5-year maintenance) |

## Design Challenges

| Challenge | Solution |
|-----------|---------|
| Weight vs. protection | Carbon-fiber/aerogel composite (light + insulating) |
| Dual atmosphere operation | Retractable rotors reduce drag in space transition |
| Thermal management | Ceramic TPS tiles + active cooling channels |
| Regulation | Dual FAA Part 135 + AST commercial space license |
| Power density | Solar-thermal rocket eliminates heavy chemical propellant |
