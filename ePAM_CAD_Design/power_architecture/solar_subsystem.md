# Solar Subsystem — All ePAM Vehicles

## Solar Cell Technology

| Parameter | Atmospheric (Drone/Car) | Space-Grade (Shuttle/Combo) |
|-----------|------------------------|---------------------------|
| **Cell type** | Perovskite/silicon tandem | Triple-junction GaAs |
| **Efficiency** | 25-28% | 32-35% |
| **Form factor** | Flexible, body-integrated | Rigid deployable panels |
| **Weight** | 0.5 kg/m2 | 1.2 kg/m2 |
| **Degradation** | <0.5%/year | <0.3%/year (space-rated) |
| **Temperature range** | -20C to +85C | -150C to +120C |
| **Cost** | $30/m2 (perovskite) | $300/m2 (GaAs) |

## Solar Coverage by Vehicle

| Vehicle | Solar Area | Peak Output | Daily Harvest |
|---------|-----------|-------------|---------------|
| **Eco Car** | 6 m2 | 1.5 kW | 4-6 kWh |
| **Urban Drone** | 18 m2 | 5.4 kW | 15-25 kWh |
| **Space Shuttle** | 24 m2 (deployable) | 7.7 kW | N/A (space ops) |
| **Combo Unit** | 20+30 m2 | 15 kW | 20-35 kWh |

## Solar Concentrator (Space Vehicles)

For the solar-thermal rocket engine, an inflatable parabolic concentrator focuses sunlight:

```
                    SUNLIGHT
                    | | | | |
                    v v v v v
              +-----------------+
             /   Inflatable      \
            /    parabolic        \
           /     reflector         \
          /       (5m dia)          \
         /                           \
        +-------- FOCAL POINT --------+
                     |
                     v
              [H2 HEAT CHAMBER]
              Temperature: 2500K
              H2 expands --> thrust
```

- **Concentrator diameter**: 5m inflatable Mylar parabolic dish
- **Concentration ratio**: 1000:1
- **Focal temperature**: 2,500K
- **Propellant heated**: Liquid H2 expands through nozzle
- **Specific impulse**: 850s (vs 450s for chemical rockets)
