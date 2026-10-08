# F1 Data Sources Evaluation (P0.3 Spike)

Date of evaluation: 2026-10-09  
Evaluated via: `spikes/probe_sources.py` and official documentation.

---

## 1. Summary Comparison Table

| Feature / Metric | **OpenF1** | **Jolpica-F1 (Ergast successor)** | **FastF1 (Python library)** |
|---|---|---|---|
| **Primary Access Method** | REST API (`https://api.openf1.org/v1`) | REST API (`https://api.jolpi.ca/ergast/f1`) | Python package (`import fastf1`) |
| **Authentication / API Key** | None required (Open public API) | None required | None required (pulls from F1 live timing & Ergast) |
| **Rate Limits** | Fair use (~3–4 req/sec recommended) | 4 req/sec (standard Ergast tier) | Client-side rate-limited by F1 live timing CDN |
| **Available Seasons** | 2023–present (modern live timing) | 1950–present (historical results) | 2018–present (detailed telemetry/laps) |
| **Lap Timing Granularity** | Sector 1/2/3, speed traps, out-laps | Single lap duration per driver | Sector 1/2/3, speed traps, micro-telemetry |
| **Tyre & Stint Data** | `compound`, `stint_number`, `tyre_age_at_start`, `lap_start`, `lap_end` | Not natively structured in laps (only results) | Full compound, stint history, tyre age |
| **Pit Stop Details** | `stop_duration`, `lane_duration`, `pit_duration`, `lap_number` | `lap`, `duration`, `time` (stop duration only) | In/out laps, pit stop duration, pit lane time |
| **Response Format** | Flat, clean JSON arrays | Deeply nested MRData XML/JSON | Pandas DataFrames |
| **Measured Latency (Bahrain 2024)** | ~0.50s - 0.70s per endpoint | ~0.82s - 0.93s per endpoint | N/A (downloads compressed binary cache) |
| **Data Volume per Race** | ~5–10 MB uncompressed JSON (laps + stints + pits) | ~1–2 MB JSON (laps only) | ~15–30 MB (with full car telemetry) |
| **Suitability for PitWall** | **Ideal Primary Source** (native stints, tyre age, sector durations, clean REST API) | Good fallback for driver/season metadata | Better for offline data-science scripts than clean backend ingestion API |

---

## 2. Deep Dive: OpenF1 (Primary Candidate)

### Verified Endpoints & Fields (`spikes/probe_results.json`)
1. **`/sessions`**:
   - Fields: `session_key`, `session_type`, `session_name`, `date_start`, `date_end`, `meeting_key`, `circuit_key`, `circuit_short_name`, `country_name`, `year`.
2. **`/laps`**:
   - Fields: `session_key`, `driver_number`, `lap_number`, `date_start`, `duration_sector_1`, `duration_sector_2`, `duration_sector_3`, `lap_duration`, `is_pit_out_lap`, `i1_speed`, `i2_speed`, `st_speed`.
3. **`/stints`**:
   - Fields: `session_key`, `driver_number`, `stint_number`, `lap_start`, `lap_end`, `compound`, `tyre_age_at_start`.
4. **`/pit`**:
   - Fields: `session_key`, `driver_number`, `lap_number`, `date`, `lane_duration`, `stop_duration`, `pit_duration`.

### Strengths
- Native concept of **Stints** and **Tyre Compound/Age**, which is critical for our Phase P7 degradation model.
- Clean relational structure keyed by `session_key` and `driver_number`.
- High availability with standard HTTP status codes.

### Known Gaps & Handling Policy
- `stop_duration` can occasionally be `null` if the sensor misses the stationary trigger (in which case `lane_duration` or `pit_duration` is used).
- In-laps / out-laps must be identified by `is_pit_out_lap` or pit entry timestamps.

---

## 3. Deep Dive: Jolpica-F1 (Secondary / Metadata Candidate)

### Verified Endpoints
1. `/{year}/{round}/results.json` - Race winner, points, final classification.
2. `/{year}/{round}/pitstops.json` - Pit stop order and duration.
3. `/{year}/{round}/laps/{lap_num}.json` - Paginated lap times.

### Strengths & Limitations
- **Pros:** Full historical coverage going back to 1950.
- **Cons:** Lap endpoint is paginated per-lap (57 HTTP requests required to get all laps for a 57-lap race) and lacks tyre compound data per lap.

---

## 4. Recommendation for Gate G0

- **Primary Ingestion Source:** **OpenF1** for session, lap, stint, tyre compound, and pit-stop ingestion.
- **Scope Confirmation:** Car telemetry (high-frequency throttle/brake/RPM coordinates) is excluded from v1 per Rule B-15 and scope table; timing, stints, tyre compounds, and pit stops are fully included.
