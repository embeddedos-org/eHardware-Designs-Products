# Hydrogen Fuel Cell Subsystem

## Water/Solar Energy Loop

The core innovation: use solar energy to split water into hydrogen and oxygen, then recombine in a fuel cell for power. Water vapor exhaust is recaptured.

```
    SOLAR ENERGY (from vehicle panels)
              |
              v
    +-------------------+
    |   ELECTROLYZER    |     PEM electrolysis
    |   H2O --> H2 + O2 |     Efficiency: 80%
    +--------+----------+
             |
     +-------+-------+
     |               |
     v               v
  [H2 TANK]     [O2 TANK]
  700 bar        200 bar
  Type IV        Type III
     |               |
     v               v
    +-------------------+
    |   PEM FUEL CELL   |     Efficiency: 60%
    |   H2 + O2 --> H2O |     Output: 15-50 kW
    |      + electricity |
    +--------+----------+
             |
     +-------+-------+
     |               |
     v               v
  [ELECTRIC      [H2O EXHAUST]
   MOTORS]           |
                     v
              [WATER RECOVERY]
              Recaptured to
              electrolyzer tank
```

## Specifications by Vehicle

| Vehicle | Fuel Cell | H2 Storage | Electrolyzer | Role |
|---------|----------|-----------|-------------|------|
| **Eco Car** | 30 kW PEM | 3 kg (700 bar) | 2 kW on-board | Range extender |
| **Urban Drone** | 30 kW PEM | 5 kg (700 bar) | None (ground-charged) | Range extender |
| **Space Shuttle** | 15 kW PEM | 200 kg LH2 | None | Backup + water recovery |
| **Combo Unit** | 50 kW PEM | 15 kg (700 bar) | 5 kW on-board | Transition power |
