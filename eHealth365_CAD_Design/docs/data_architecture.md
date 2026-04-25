# Data Architecture — Single Hub Flow

## Pipeline: Skin → Edge → Cloud

```
STAGE 1: SENSE              STAGE 2: EDGE COMPUTE         STAGE 3: SYNC
─────────────               ──────────────────             ──────────────
Ring sensors                 Ring MCU (nRF5340)             BLE 5.3
  PPG → raw photopleth.        Bandpass filter                15-min intervals
  Accel → raw XYZ              Motion artifact removal        Compressed packets
  Temp → raw ADC               Feature extraction             AES-128 encrypted
  EDA → raw conductance        HR/HRV/SpO₂ calculation

Patch sensors                Patch MCU (nRF52840)           BLE 5.3
  CGM → raw current            Glucose algorithm              15-min intervals
  ISE → raw voltage            Ion concentration calc         Compressed packets
  BioZ → raw impedance         Cole-Cole model fitting        AES-128 encrypted
  pH → raw FET voltage         pH calculation
  Cartridge → raw SPI          Analyte concentration


STAGE 4: AI ENGINE           STAGE 5: PRESENTATION
──────────────────           ─────────────────────
📱 App (on-device ML)        📱 App Dashboard
  Combine Chemical + Physical    Daily Score (readiness)
  Digital Twin model             Sleep Lab
  Trend analysis                 Nutrition Score
  Anomaly detection              Glucose Trends
  Meal impact prediction         Electrolyte Balance
  Deficiency alerts              Stress & Recovery
  Doctor report generation       Monthly Blood Report
                                 Deficiency Alerts
                                 Doctor Sharing
```

## Data Retention Policy

| Data Type | On-Device | App (Local) | Cloud (Optional) |
|-----------|-----------|-------------|-----------------|
| Raw sensor data | 24 hours | 7 days | Not uploaded |
| Processed metrics | 7 days | 90 days | 1 year |
| Daily summaries | — | 2 years | 5 years |
| Monthly lab results | — | Permanent | Permanent |
| AI model weights | — | On-device | Not uploaded |

## Privacy & Security

- **End-to-end encryption**: BLE link encrypted with AES-128-CCM
- **On-device ML**: All AI inference runs locally on phone — no cloud dependency
- **Data sovereignty**: User owns all data, can export or delete at any time
- **HIPAA-ready**: Architecture supports HIPAA compliance for doctor sharing
- **No advertising**: Health data is never used for ads or sold to third parties
