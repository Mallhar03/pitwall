# PitWall Domain Glossary

This document defines the Formula 1 domain concepts and exact terminology used throughout the PitWall project. All definitions are grounded in official F1 sporting regulations and mapped directly to OpenF1 API field representations.

---

## 1. Event & Session Hierarchy

### Meeting (`meeting_key`)
- **Definition**: An official F1 Grand Prix event weekend taking place at a specific circuit on specific dates (e.g., *Bahrain Grand Prix 2024*).
- **OpenF1 Mapping**: `meeting_key` (integer, e.g., `1229`).

### Session (`session_key`, `session_name`, `session_type`)
- **Definition**: A distinct track activity block within a Grand Prix meeting. Standard sessions include Practice (`FP1`, `FP2`, `FP3`), Qualifying (`Q1`, `Q2`, `Q3` or `Qualifying`), Sprint / Sprint Shootout, and the main `Race`.
- **OpenF1 Mapping**: `session_key` (integer, e.g., `9472`), `session_name` (string, e.g., `"Race"`), `session_type` (string).

### Driver (`driver_number`, `name_acronym`)
- **Definition**: A competitor driving a specific car in a session. Identified uniquely in timing data by their racing number.
- **OpenF1 Mapping**: `driver_number` (integer, e.g., `1` for Verstappen, `44` for Hamilton), `name_acronym` (string, e.g., `"VER"`), `team_name` (string).

---

## 2. Timing & Laps

### Lap (`lap_number`, `lap_duration`)
- **Definition**: One complete circuit around the track by a driver, starting and ending at the Start/Finish line.
- **OpenF1 Mapping**: `lap_number` (integer), `lap_duration` (float seconds, e.g., `91.456`).

### Sectors (`duration_sector_1`, `duration_sector_2`, `duration_sector_3`)
- **Definition**: Each lap is divided into three consecutive geographical sections (Sector 1, Sector 2, Sector 3). The sum of all three sector times equals the total lap duration.
- **OpenF1 Mapping**: `duration_sector_1`, `duration_sector_2`, `duration_sector_3` (float seconds).

### Out-Lap (`is_pit_out_lap`)
- **Definition**: The lap on which a car exits the pit lane and enters the track. Out-laps are significantly slower because the car travels through the pit lane speed limiter zone and tires are not yet up to optimum operating temperature.
- **OpenF1 Mapping**: `is_pit_out_lap` (boolean `true`/`false`).

### In-Lap
- **Definition**: The lap on which a car leaves the track and enters the pit lane to perform a pit stop or end a stint. In-laps have a slower final sector due to pit-entry speed limits.
- **OpenF1 Mapping**: Identified when the subsequent lap is an `is_pit_out_lap` or when a corresponding `pit` entry record occurs on that lap number.

---

## 3. Tyres & Stints

### Stint (`stint_number`)
- **Definition**: A continuous period of driving on a single set of tires without entering the pit lane. A standard race consists of 1 to 3 stints depending on tire strategy and degradation.
- **OpenF1 Mapping**: `stint_number` (integer, 1-indexed per driver per session).

### Tyre Compound (`compound`)
- **Definition**: The specific rubber mixture of the fitted tire set. Pirelli supplies dry compounds (designated `SOFT`, `MEDIUM`, `HARD`, or C1-C5 range) and wet compounds (`INTERMEDIATE`, `WET`).
- **OpenF1 Mapping**: `compound` (string, upper-case e.g., `"SOFT"`, `"MEDIUM"`, `"HARD"`).

### Tyre Age (`tyre_age_at_start`)
- **Definition**: The number of laps a tire set has completed prior to the start of the current stint (includes laps run in earlier Qualifying or Practice sessions if a used set is fitted).
- **OpenF1 Mapping**: `tyre_age_at_start` (integer laps).

### Tyre Degradation
- **Definition**: The loss of tire performance (increased lap times / reduced grip) over successive laps within a stint as the tread rubber wears down and thermal degradation accumulates.

---

## 4. Pit Stops

### Pit Stop (`pit_duration`, `stop_duration`)
- **Definition**: The action of entering the pit lane, stopping at the pit box to change tires (and/or replace damaged parts), and re-joining the track.
- **OpenF1 Mapping**: 
  - `pit_duration`: Total time spent in the pit lane from pit entry line to pit exit line (float seconds, e.g., `24.512`).
  - `stop_duration`: Time the car was stationary at the pit box while mechanics changed tires (float seconds, e.g., `2.31`).

---

## 5. Track Conditions & Neutralisations

### Neutralised Laps (Safety Car / VSC / Red Flag)
- **Definition**: Laps where racing speed is restricted by race control due to an accident, debris, or severe weather:
  - **Safety Car (SC)**: Physical Safety Car leads the field; lap times are 30–60% slower.
  - **Virtual Safety Car (VSC)**: Drivers must adhere to a minimum Delta time on screen; lap times are ~30% slower.
  - **Red Flag**: Session suspended; cars return to the pit lane.
- **OpenF1 Mapping**: `track_status` codes / flag indicators.

### Representative Lap vs. Non-Representative Lap
- **Definition**: A crucial distinction for tire degradation modeling and race analytics:
  - **Representative Lap**: A clean, full-speed lap completed under green flag conditions without traffic interference or pit lane travel.
  - **Non-Representative Lap**: Laps impacted by Out-laps (`is_pit_out_lap = true`), In-laps, Safety Car / VSC / Yellow flags, lap 1 (standing start), or severe incident delays. *These laps must be filtered out when training or evaluating tire degradation models.*
