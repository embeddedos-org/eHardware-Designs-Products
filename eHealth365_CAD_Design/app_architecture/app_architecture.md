# eHealth365 Mobile App — Architecture

## Dashboard Modules

```
HOME DASHBOARD
├── 🟢 Live vitals (HR, SpO₂, temp)
├── 📊 Today's nutrition score
├── 💧 Hydration status
├── 😴 Last night's sleep
├── ⚡ Energy & readiness score
└── ⚠️ Deficiency alerts

DETAILED MODULES
├── 🍎 Macros tracker (protein/carbs/fat) — AI food camera
├── 💊 Micronutrient vault (vitamins/minerals) — monthly cartridge
├── 📈 Glucose trends — CGM patterns & meal impact
├── 🧪 Electrolyte balance — Na⁺/K⁺/Mg²⁺/Zn²⁺
├── 😴 Sleep lab — stages, consistency, recovery
├── 🧠 Stress & recovery — HRV trend, cortisol estimate
├── 📋 Monthly blood report — full vitamin/mineral panel
└── 👨‍⚕️ Doctor dashboard — shareable reports & trends
```

## App Replaces 3 Hardware Devices

| Replaced Device | App Solution |
|----------------|-------------|
| 🍴 Smart fork | AI camera — photo meal, auto-calculate calories + macros |
| 💧 Smart water bottle | Hydration reminders + manual log + patch bioimpedance confirms |
| ⚖️ Food scale | AI portion estimation from photo — no scale needed |

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Mobile** | React Native 0.73+ (iOS + Android) |
| **State management** | Redux Toolkit |
| **BLE** | react-native-ble-plx |
| **AI food camera** | TensorFlow Lite (on-device) |
| **Health ML** | CoreML (iOS) / TFLite (Android) |
| **Local DB** | SQLite + Realm |
| **Charts** | Victory Native |
| **Backend** | Firebase / Supabase (optional cloud sync) |
| **Auth** | Biometric + PIN |
| **Notifications** | FCM / APNs |
