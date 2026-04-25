# eHealth365 — Business Plan & Cost Analysis

## BOM Cost Breakdown

### Smart Ring Pro — $100 BOM

| Component | Cost |
|-----------|------|
| Sensors + optics (PPG, temp, accel, EDA, gas) | $28 |
| Processor + BLE chip (nRF5340) | $12 |
| Titanium shell (CNC machined, PVD coated) | $18 |
| Battery + charging coil (22mAh LiPo + Qi Rx) | $8 |
| Breath port micro-valve (MEMS + gas sensor) | $14 |
| Assembly + QC (SMT, flex-bend, IP68 test) | $20 |
| **BOM total** | **$100** |
| **Retail price target** | **$299** |
| **Gross margin** | **~66%** |

### Smart Patch Pro — $90 BOM

| Component | Cost |
|-----------|------|
| CGM sensor + needle (glucose oxidase array) | $22 |
| Sweat biosensor array (4x ISE electrodes) | $18 |
| Bioimpedance electrodes (4x tetrapolar) | $10 |
| Flexible PCB + BLE (nRF52840 + flex substrate) | $14 |
| Thin-film battery (65mAh silver oxide) | $6 |
| Adhesive + encapsulation (3M 2477P + TPU shell) | $8 |
| Assembly + sterile pack (clean-room, gamma sterilization) | $12 |
| **BOM total (starter kit)** | **$90** |
| **Retail price target** | **$199** |
| **Gross margin** | **~55%** |

## Recurring Consumables Revenue

| Consumable | Price | Annual Revenue/User |
|------------|-------|-------------------|
| Weekly patch refill (per unit) | $15/week | $780/year |
| Monthly blood cartridge | $25/month | $300/year |
| App subscription | $9.99/month | $120/year |
| Quarterly metabolic panel | $60/quarter | $240/year |
| **Total annual recurring (per user)** | | **$1,440/year** |

## First-Year Total Cost of Ownership

| Component | Cost |
|-----------|------|
| Hardware upfront (Ring + Patch starter kit) | $498 |
| Consumables + app (year 1) | $1,440 |
| **Total year 1 per user** | **$1,938** |
| **Year 2+ (hardware already owned)** | **$1,440** |

## R&D Cost Estimate

| Category | Investment | Notes |
|----------|-----------|-------|
| Sensor R&D (CGM + sweat + breath) | $8M - $15M | Novel biosensor integration, calibration algorithms |
| Hardware engineering + prototyping | $5M - $10M | PCB design, enclosure tooling, 3D modeling, DFM |
| Clinical trials + FDA clearance | $10M - $25M | 510(k) or De Novo, biocompatibility, accuracy studies |
| App + AI platform development | $3M - $6M | React Native app, on-device ML, cloud backend |
| Manufacturing setup + tooling | $4M - $8M | Injection molds, SMT lines, clean-room, QC stations |
| **Total R&D to launch** | **$30M - $64M** | |

## Break-Even & Scale Milestones

### MVP Break-Even

| Metric | Target |
|--------|--------|
| Users needed | ~25,000 |
| Timeline | Year 2-3 |
| Revenue at break-even | ~$48M ARR |

### Scale Milestone

| Metric | Target |
|--------|--------|
| Users at scale | 500,000+ |
| Timeline | Year 5-7 |
| Revenue potential | $720M ARR |

## Revenue Model

```
YEAR 1: Hardware + Consumables
  Ring Pro: $299 x units
  Patch Starter: $199 x units
  Weekly patches: $15/week x users
  Monthly cartridges: $25/month x users
  App subscription: $9.99/month x users

YEAR 2+: Consumables Only (users already have hardware)
  Weekly patches: $780/year x users
  Monthly cartridges: $300/year x users
  App subscription: $120/year x users
  Quarterly panels: $240/year x users

REVENUE MIX AT SCALE
  Hardware (one-time): ~25% of year-1 revenue
  Consumables + app (recurring): ~75% of year-1, 100% of year-2+
  --> Classic "razor and blade" model
```

## Competitive Landscape

| Competitor | What They Do | eHealth365 Advantage |
|-----------|-------------|---------------------|
| **Oura Ring** | Sleep + HRV + temp | We add SpO2, ketones, EDA, glucose (via patch) |
| **Dexcom G7** | CGM glucose only | We add electrolytes, hydration, vitamins, HRV |
| **Apple Watch** | HR + SpO2 + ECG | We add glucose, electrolytes, blood labs |
| **Whoop** | HRV + strain + sleep | We add glucose, chemistry, nutrition |
| **Levels** | CGM + metabolic insights | We add ring vitals, blood labs, hydration |

**Unique position**: No competitor covers both physical vitals (ring) AND blood chemistry (patch) in a unified system with monthly lab-grade blood analysis.

## Regulatory Path

| Body | Classification | Timeline |
|------|---------------|----------|
| **FDA (USA)** | Class II (510(k) or De Novo) | 12-18 months |
| **CE Mark (EU)** | MDR Class IIa | 12-15 months |
| **TGA (Australia)** | Class IIa | 8-12 months |
| **Health Canada** | Class II | 10-14 months |

### FDA Strategy
1. **Phase 1**: Submit Ring Pro as wellness device (HR, sleep, activity) — no FDA needed
2. **Phase 2**: Submit CGM patch as Class II medical device — 510(k) with predicate (Dexcom G7)
3. **Phase 3**: Submit blood cartridge as Class II IVD — De Novo pathway
