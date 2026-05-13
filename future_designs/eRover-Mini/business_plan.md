# 🚙 eRover-Mini — Business / Donor Plan (concept)

> **Status:** Concept (chassis CAD + ROS-2 bridge ported on eos TBD)
> **Donor tier:** $2 K — equip a university robotics lab with 5 rovers for one term.

## What a donor funds

A TurtleBot 4 costs $3 K. eRover-Mini delivers comparable autonomy (SLAM + ROS-2 bridge + camera + LIDAR) for under $400, putting real mobile-robot research within reach of any teaching university or maker-space. One bench seats five rovers for the price of one commercial unit.

## Cost outline (placeholder)

| Line | Estimate |
|---|---|
| BOM (qty 1) | ~$420 |
| BOM (qty 100) | ~$310 |
| Curriculum + lab manuals | Author with university partner ($30 K one-time) |
| CI / hardware-in-loop tests | Run on EoSim (zero marginal) |

## Regulatory path

None beyond CE/FCC for radios.

## Go-to-market / distribution

Direct-to-university discount via educational distributor; classroom curriculum bundled.

## EmbeddedOS components leveraged

- eos (kernel + drivers)
- eAI (SLAM + object detection)
- eIPC (ROS-2 bridge)
- ebuild (cross-compile)

> All numbers are **concept-stage estimates**. They will be sharpened when
> this design graduates from `future_designs/` to its own top-level
> directory under [`eCAD-Hardware-Products`](https://github.com/embeddedos-org/eCAD-Hardware-Products).
