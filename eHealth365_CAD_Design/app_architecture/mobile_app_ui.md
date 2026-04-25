# eHealth365 Mobile App — UI Specification

## Design Language

| Property | Value |
|----------|-------|
| **Theme** | Dark mode primary (OLED-optimized) |
| **Background** | #0D1117 (deep navy-black) |
| **Card background** | #161B22 (elevated surface) |
| **Accent colors** | Green (#3FB950), Purple (#BC8CFF), Orange (#F0883E), Cyan (#79C0FF) |
| **Typography** | SF Pro (iOS) / Roboto (Android), weights 400/600/700 |
| **Corner radius** | 16px (cards), 12px (buttons), 24px (health score ring) |

## Home Dashboard Layout

```
+---------------------------------------------+
| 9:41              ...              87%       |  Status bar
+---------------------------------------------+
| Good morning, Alex                    [AJ]   |  Greeting + avatar
| Friday, April 24 . All systems synced        |
+---------------------------------------------+
| +-------------------------------------------+|
| |    [82]       82/100                       ||
| |   /100    Daily health score               ||  Health Score Ring
| |           +----------------+               ||  Circular progress
| |           | Good -- above  |               ||
| |           |     avg        |               ||
| |           +----------------+               ||
| |           +4 pts vs yesterday              ||
| +-------------------------------------------+|
+---------------------------------------------+
| +----------+ +----------+ +--------------+   |
| |Hydration | |Sleep: 7h | |Glucose       |   |  Alert chips
| |low       | |42m       | |stable        |   |  Orange=warning
| |Drink     | |Recovery  | |5.4 mmol/L    |   |  Green=normal
| |400ml now | |91%       | |              |   |
| +----------+ +----------+ +--------------+   |
+---------------------------------------------+
| LIVE VITALS                                   |
| +----------------+ +----------------+         |
| | (heart) 72 bpm | | (O2) 98 %     |         |  2x2 vitals grid
| | Heart rate     | | Blood oxygen   |         |
| | ########       | | ##########     |         |
| +----------------+ +----------------+         |
| +----------------+ +----------------+         |
| | (drop) 68 %   | | (temp) 36.7 C  |         |
| | Hydration      | | Body temp      |         |
| | ######         | | ########--     |         |
| +----------------+ +----------------+         |
+---------------------------------------------+
| Glucose -- last 3 hours    [5.4 mmol/L]      |
| +-------------------------------------------+|
| |     /\                        /\           ||  CGM line chart
| |    /  \    /\               /  \--         ||  Green line
| | --/    \--/  \-------------/               ||
| | 3h ago    1.5h ago              now        ||
| +-------------------------------------------+|
+---------------------------------------------+
| ELECTROLYTES (SWEAT SCAN 2H AGO)             |
| +----+ +----+ +----+ +----+                  |
| |142 | |3.2 | |0.9 | |1.1 |                  |  4 mineral cards
| |Na  | |K   | |Mg  | |Zn  |                  |
| |mmol| |mmol| |mmol| |umol|                  |
| |Norm| |Low!| |Norm| |Norm|                  |  Color: green/orange
| +----+ +----+ +----+ +----+                  |
+---------------------------------------------+
| DEVICES                                       |
| +------------------+ +------------------+     |
| | Ring Pro         | | Patch Pro        |     |  Device status
| | Connected        | | Connected        |     |
| | 4 days left      | | 3 days left      |     |
| | ########---      | | ######----       |     |
| +------------------+ +------------------+     |
+---------------------------------------------+
|                  . O .                        |  Page dots
+---------------------------------------------+
| Dashboard  Trends   Profile  Settings         |  Tab bar
|    .                                          |
+---------------------------------------------+
```

## Tab Navigation

| Tab | Icon | Screen | Content |
|-----|------|--------|---------|
| **Dashboard** | Grid | Home | Health score, live vitals, glucose, electrolytes, devices |
| **Trends** | Chart | Analytics | 7/30/90-day trends, glucose patterns, sleep history |
| **Profile** | Person | Health profile | Monthly blood reports, vitamin vault, doctor sharing |
| **Settings** | Gear | Configuration | Device pairing, notifications, data export, privacy |

## Key Screens

### Sleep Lab
- Sleep stages timeline bar (REM=purple, Deep=blue, Light=cyan, Awake=orange)
- Sleep consistency score (7-day trend line)
- HRV during sleep (recovery indicator with green/yellow/red zones)
- SpO2 overnight curve (line chart with 90% threshold line)
- Readiness score for next day (0-100 ring)

### Nutrition Dashboard
- AI food camera button (center, large, prominent green circle)
- Macro breakdown pie chart (protein=blue, carbs=orange, fat=yellow)
- Meal timeline with glucose impact overlay for each meal
- Micro-nutrient vault grid (monthly blood cartridge results)
- Deficiency alerts with supplement suggestions

### Glucose Detail
- Real-time CGM value (large center number, color-coded)
- Time range selector: 3h / 12h / 24h / 7d
- Trend line with meal markers (camera icon pins)
- Pattern recognition cards (morning spikes, post-meal curves)
- Time-in-range donut chart (green=in range, orange=high, red=low)

### Monthly Blood Report
- Full vitamin/mineral panel in grid layout
- Traffic light indicators per analyte (green/yellow/red)
- Trend arrows vs. previous months
- Doctor-shareable PDF export button
- AI supplement recommendations

### Electrolyte Detail
- 4 large cards: Na+, K+, Mg2+, Zn2+
- Historical trend for each ion (7-day line chart)
- Hydration correlation overlay
- Exercise impact markers
- Dietary recommendations

## Component Library

| Component | Props | Variants |
|-----------|-------|----------|
| **VitalCard** | value, unit, label, trend_data | Normal (green), Warning (orange), Critical (red) |
| **HealthScoreRing** | score (0-100), delta | Animated SVG ring with gradient |
| **AlertChip** | text, subtext, type | Info (purple), Warning (orange), Normal (green) |
| **MineralCard** | value, ion, unit, status | Normal, Low, High, Critical |
| **DeviceCard** | name, connected, battery_pct | Ring, Patch variants |
| **TrendChart** | data[], range | 3h, 12h, 24h, 7d, 30d, 90d |
| **MealCard** | photo_uri, macros, glucose_impact | With/without glucose overlay |
| **SleepStageBar** | stages[] with timestamps | REM/Deep/Light/Awake colors |

## Animations

| Interaction | Animation | Duration |
|-------------|-----------|----------|
| Health score load | Ring fills clockwise with easing | 1.2s |
| Vital card update | Number morphs (count up/down) | 0.3s |
| Alert chip appear | Slide in from right with fade | 0.4s |
| Chart data load | Line draws left-to-right | 0.8s |
| Tab switch | Cross-fade with slight upward shift | 0.25s |
| Pull to refresh | Bounce + sync indicator | 0.5s |

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Framework** | React Native 0.73+ |
| **Navigation** | React Navigation 6 |
| **State** | Redux Toolkit + RTK Query |
| **BLE** | react-native-ble-plx |
| **Charts** | Victory Native / react-native-svg |
| **AI Camera** | TensorFlow Lite (on-device food recognition) |
| **Health ML** | CoreML (iOS) / TFLite (Android) |
| **Storage** | SQLite (Watermelon DB) + Realm |
| **Auth** | Biometric (FaceID/TouchID/Fingerprint) + PIN |
| **Notifications** | FCM (Android) / APNs (iOS) |
