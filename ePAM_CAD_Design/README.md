# ePAM — Personal Air Mobility

> **Solar-Hybrid Personal Transport — 4-Product Line**
> 4-5 seat capacity, Solar + Water/Hydrogen hybrid power

## Product Line Overview

```
Solar hybrid personal transport -- 4-product line
4-5 seat capacity . Solar + water/hydrogen hybrid power

+-------------------+  +-------------------+  +-------------------+  +-------------------+
|   URBAN DRONE     |  |  SPACE SHUTTLE    |  |     ECO CAR       |  |    COMBO UNIT     |
|                   |  |                   |  |                   |  |                   |
|  eVTOL . 4 seats  |  | Suborbital . 4    |  | Ground . 4-5 seats|  | Air+space . 4     |
|  Solar + battery  |  | Solar + H2 fuel   |  | Solar + EV battery|  | Solar + H2 hybrid |
|  0-500m altitude  |  | 100km altitude    |  | Road + highway    |  | 0-100km range     |
|  City commuter    |  | Space tourism     |  | Mass market       |  | Premium fleet     |
|                   |  |                   |  |                   |  |                   |
|  Est. $85K-120K   |  |  Est. $2M-4M      |  |  Est. $28K-45K    |  |  Est. $5M-9M      |
+-------------------+  +-------------------+  +-------------------+  +-------------------+
```

## The 4 Vehicles

| Vehicle | Type | Seats | Power | Altitude | Price Range | Market |
|---------|------|-------|-------|----------|-------------|--------|
| **Urban Drone** | eVTOL aircraft | 4 | Solar + solid-state battery | 0-500m | $85K-$120K | City commuters |
| **Space Shuttle** | Suborbital craft | 4 | Solar + H2 fuel cell | 100km | $2M-$4M | Space tourism |
| **Eco Car** | Ground vehicle | 4-5 | Solar + EV battery | Ground | $28K-$45K | Mass market |
| **Combo Unit** | Air + space hybrid | 4 | Solar + H2 hybrid | 0-100km | $5M-$9M | Premium fleet |

## Power Architecture (All Models)

```
+-------------------+  +-------------------+  +-------------------+  +-------------------+
|   Solar panels    |  |   H2 fuel cell    |  | Solid-state batt  |  |   Kinetic regen   |
|   Primary harvest |  |  Water electrolys |  |   Energy storage  |  |  Descent energy   |
|  Roof + wing mtd  |  |  Long-range boost |  |   Regen braking   |  |  Capture + store  |
+-------------------+  +-------------------+  +-------------------+  +-------------------+
```

### The Water/Solar Energy Loop
1. **Solar Collection** — Vehicle surface coated in flexible perovskite solar cells
2. **Water Electrolysis** — Excess solar energy splits on-board H2O into H2 + O2
3. **Hydrogen Fuel Cell** — H2 powers electric motors, water vapor exhaust is recaptured
4. **Kinetic Regeneration** — Descent/braking energy captured and stored

## Business Model

```
+---------------------+  +---------------------+  +---------------------+
|   Revenue streams   |  |    Market tiers     |  | Cost efficiency     |
|                     |  |                     |  |   levers            |
|  Direct vehicle     |  | Mass -- EcoCar      |  | Shared platform     |
|    sales            |  |   ($28K+)           |  |   chassis           |
|  Fleet leasing      |  | Mid -- Urban Drone  |  | Modular power packs |
|    (B2B)            |  |   ($85K+)           |  | 3D-printed body     |
|  Ride-share         |  | Premium -- Combo    |  |   panels            |
|    platform %       |  |   ($5M+)            |  | OTA software        |
|  Space tourism      |  | Ultra -- Space      |  |   updates           |
|    tickets          |  |   ($2M+)            |  | Vertical solar cell |
|  Software / OTA     |  | Gov / Defense       |  |   mfg               |
|    subscriptions    |  |   contracts         |  | Battery swap        |
|  Energy resale      |  | Franchise /         |  |   network           |
|    (V2G)            |  |   licensing         |  |                     |
+---------------------+  +---------------------+  +---------------------+
```

## Go-To-Market Roadmap

| Phase | Timeline | Milestones |
|-------|----------|-----------|
| **Phase 1** | 2025-27 | EcoCar production, Urban Drone prototype, FAA/EASA certs, seed fleet cities |
| **Phase 2** | 2027-30 | Urban Drone mass launch, ride-share platform live, H2 fueling network, space R&D milestones |
| **Phase 3** | 2030+ | Space shuttle launch, Combo unit fleet, global expansion, IPO / licensing |

## Key Enablers

| Category | Requirements |
|----------|-------------|
| **Regulation** | FAA Part 135, EASA, Space Act agreements, urban air mobility laws |
| **Infrastructure** | Vertiports / landing pads, H2 fueling stations, solar charging grid |
| **Technology** | AI autonomous flight, next-gen solar cells, lightweight composites |

## Directory Structure

```
ePAM_CAD_Design/
+-- README.md
+-- urban_drone/              Urban Drone eVTOL (4-seat)
|   +-- product_datasheet.md
|   +-- drone_schematic.kicad_sch
|   +-- bom.csv
|   +-- manufacturing_notes.md
+-- space_shuttle/            Space Shuttle (suborbital, 4-seat)
|   +-- product_datasheet.md
|   +-- shuttle_schematic.kicad_sch
|   +-- bom.csv
+-- eco_car/                  Eco Car (ground, 4-5 seat)
|   +-- product_datasheet.md
|   +-- car_schematic.kicad_sch
|   +-- bom.csv
+-- combo_unit/               Combo Unit (air + space hybrid)
|   +-- product_datasheet.md
|   +-- combo_schematic.kicad_sch
+-- power_architecture/       Shared power systems
|   +-- solar_subsystem.md
|   +-- hydrogen_fuel_cell.md
|   +-- solid_state_battery.md
|   +-- kinetic_regen.md
+-- 3d_models/                3D CAD model specs
|   +-- drone_3d_model.md
|   +-- shuttle_3d_model.md
|   +-- car_3d_model.md
|   +-- combo_3d_model.md
+-- docs/                     Design docs & business
    +-- business_plan.md
    +-- regulatory_path.md
    +-- infrastructure.md
    +-- trans_atmospheric.md
```

## Related Repositories

| Repo | Relationship |
|------|-------------|
| [eos](https://github.com/embeddedos-org/eos) | Embedded firmware for flight controllers & vehicle ECUs |
| [eAI](https://github.com/embeddedos-org/eAI) | AI for autonomous flight, obstacle avoidance, route planning |
| [eNI](https://github.com/embeddedos-org/eNI) | Neural interface for pilot brain-computer control |
| [EoSim](https://github.com/embeddedos-org/EoSim) | Flight simulation & digital twin of all vehicle models |
| [eApps](https://github.com/embeddedos-org/eApps) | Ride-share platform & passenger app |
