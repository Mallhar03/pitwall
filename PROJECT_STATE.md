# PITWALL: PROJECT STATE (live)

> Update only per `PROJECT_GUIDE.md` section 4.5: edit one section at a time, never rewrite the whole file, never delete history, write only verified or user-stated facts (mark the rest `[unverified]`), no secrets.
> If this file and the repo disagree, the repo wins; flag the mismatch and ask.

## 0. Header
- Guide version: 1.0
- State last updated: 2026-10-09 by Antigravity (P0.3 complete, Gate G0 next)
- Repo status: in progress, spikes/ and docs/ added
- Project folder: /home/mallhar/Desktop/f1-project

## 1. Handoff summary (15 lines max; rewrite at every checkpoint)
- Project: PitWall (F1 race-data backend).
- P0.1, P0.2, and P0.3 are completed.
- P0.3 Source Spike: Probed OpenF1 and Jolpica-F1 APIs in `spikes/probe_sources.py`. Documented full comparison in `docs/data-sources.md`.
- OpenF1 verified as primary candidate: provides clean JSON arrays for sessions, laps (sectors + speed traps), stints (tyre compound + age), and pit stops.
- Next Task: P0.4 Gate G0 (formally select OpenF1, decide telemetry out, choose first target race: Bahrain 2024).

## 2. Current focus
- Phase: P0
- Task Lock (single active task): P0.4 Gate G0
- Status: in progress

## 3. Task tracker (`[ ]` todo, `[~]` in progress, `[x]` done, `[-]` cut with reason in Decisions)
**P0** [x] P0.1 Intake · [x] P0.2 Repo and environment · [x] P0.3 Source spike · [~] P0.4 Gate G0 · [ ] P0.5 Glossary
**P1** [ ] P1.1 Postgres via Compose · [ ] P1.2 Schema on paper · [ ] P1.3 Models and session · [ ] P1.4 Alembic · [ ] P1.5 Constraint tests · [ ] P1.6 Index experiment · [ ] Gate G1
**P2** [ ] P2.1 Source adapter · [ ] P2.2 Validate and transform · [ ] P2.3 Idempotent loader · [ ] P2.4 CLI · [ ] P2.5 Failure drills
**P3** [ ] P3.1 App skeleton · [ ] P3.2 Read endpoints · [ ] P3.3 Auth · [ ] P3.4 Integration tests · [ ] P3.5 CI skeleton · [ ] P3.6 Baseline load test
**P4** [ ] P4.1 Redis in Compose · [ ] P4.2 Cache candidates · [ ] P4.3 Cache-aside · [ ] P4.4 Failure behaviour · [ ] P4.5 Rate limiting · [ ] P4.6 Re-measure
**P5** [ ] P5.1 Celery and worker · [ ] P5.2 Ingestion as a job · [ ] P5.3 Retry policy · [ ] P5.4 Replay publisher · [ ] P5.5 Idempotent consumer · [ ] P5.6 Failure drills · [ ] Gate G5
**P6 (cuttable)** [ ] P6.1 WebSocket endpoint · [ ] P6.2 Slow clients · [ ] P6.3 Static page · [ ] P6.4 Load test
**P7** [ ] P7.1 Question defined · [ ] P7.2 Dataset (Gate G7) · [ ] P7.3 Baseline and evaluation · [ ] P7.4 One model · [ ] P7.5 Predictor interface · [ ] P7.6 Serve via API · [ ] P7.7 Retraining job (optional)
**P8** [ ] P8.1 Dockerfile · [ ] P8.2 Full stack compose · [ ] P8.3 CI images · [ ] P8.4 Gate G8 · [ ] P8.5 Deploy · [ ] P8.6 Health and logs · [ ] P8.7 Scaling demo (optional) · [ ] P8.8 Runbook
**P9** [ ] P9.1 Security pass · [ ] P9.2 Dependency audit · [ ] P9.3 Failure drills · [ ] P9.4 README · [ ] P9.5 Design notes · [ ] P9.6 Demo script · [ ] P9.7 Retrospective

## 4. User profile (stated by the user only; fill during P0.1)
- OS: Linux
- Weekly hours: 10 hours/week
- Terminal comfort: Moderate ("not too good and not completely unfamiliar")
- Python: OOP fundamentals studied (classes, objects, self, composition, access modifiers, getters/setters, properties) [claimed]
- Git and GitHub: Learning along the way
- SQL / Docker / Automated tests / Redis / Async: New, will learn as required at each phase
- Cloud accounts or credits: Unknown / unconfirmed
- Learning approach: Collaborative building (Tutor + Optimiser paired programming, not an exam)

## 5. Decisions log
Baseline decisions B-1 to B-16 in the guide apply unless superseded here.
Format: `DR-001 | date | decision | why | alternatives considered | who decided | supersedes`
(none yet)

## 6. Verified facts register
Only facts verified in a session. Format: `fact | how verified | date`
- Python 3.12.3 installed on host | `python3 --version` | 2026-10-09
- pytest 9.1.1, ruff 0.16.10 installed in `.venv` | `.venv/bin/pytest`, `.venv/bin/ruff --version` | 2026-10-09
- Smoke test passing on editable install | `pytest` run in `.venv` | 2026-10-09
- OpenF1 API live and reachable without auth key | `spikes/probe_sources.py` | 2026-10-09
- OpenF1 returns native stints with compound and tyre_age_at_start | `spikes/probe_sources.py` | 2026-10-09
- Jolpica-F1 (Ergast successor) requires per-lap pagination for race laps | `spikes/probe_sources.py` | 2026-10-09

## 7. Learning queue
Format: `topic | needed for | resource and portion | status (todo / in progress / ready-check passed)`
- Python venv and pip | P0.2 | FCC API course 22:11 to 36:21 | ready-check passed (environment created & verified)
- Git and GitHub basics | P0.2 | FCC API course 11:23:38 to 11:34:39 | in progress
- Reading tabular data (pandas / requests / JSON inspection) | P0.3 | official docs & spikes | ready-check passed (probed & parsed live JSON)
- SQL basics | P1 | FCC API course 2:24:11 to 4:08:00 and/or FCC Postgres course | todo
- Docker basics | P1.1 | FCC API course 13:26:09 to 14:08:08 | todo
- SQLAlchemy 2.x models | P1.3 | official docs; FCC 4:31:18 to 5:28:21 for concepts only | todo
- Alembic | P1.4 | FCC API course 10:30:18 to 11:13:50 | todo
- Indexes and EXPLAIN | P1.6 | Use The Index, Luke; Postgres docs | todo

## 8. User-reported learning
Format: `date | what the user says they learned | status: claimed / verified / needs work`
- 2026-10-09 | Python OOP fundamentals (classes, objects, self, composition, access modifiers, getters/setters, @property) | status: claimed

## 9. Metrics log
Format: `date | what was measured | how (tool, data size, machine) | result`
- 2026-10-09 | OpenF1 endpoint latency (Bahrain 2024 session key 9472) | `httpx` probe in `spikes/probe_sources.py` | sessions: 0.697s, laps: 0.518s, stints: 0.500s, pits: 0.496s
- 2026-10-09 | Jolpica-F1 latency (Bahrain 2024) | `httpx` probe in `spikes/probe_sources.py` | results: 0.852s, lap 1: 0.824s, pitstops: 0.932s

## 10. Risks and open questions
- R-1: Data source access, terms or coverage may not match expectations (resolved in P0.3: OpenF1 is viable & rich).
- R-2: The main video course is from 2021; library styles may differ from current versions.
- R-3: Agent rules-file loading in the IDE is unverified; the bootstrap prompt in the guide is the fallback.

## 11. Parking lot (ideas not to build now)
- AI assistant on top of the API (separate later project; keep the API clean for tool-calling).

## 12. Session log (append-only, newest at the bottom)
- **Session 0, 2026-10-08 (planning chat, Claude):** scope and architecture decided; PROJECT_GUIDE.md and PROJECT_STATE.md created. No code written. Next: P0.1 Intake.
- **Session 1, 2026-10-09 (Antigravity):** P0.1 Intake completed. User profile recorded (~10 hrs/week, Linux, moderate terminal, OOP studied). P0.2 completed: Git repo initialized, `.gitignore`, `.env.example`, `pyproject.toml`, virtual environment `.venv`, and passing smoke tests. Task Lock set to P0.3 (Source spike).
- **Session 1 (cont.), 2026-10-09 (Antigravity):** P0.3 Source Spike completed: probed OpenF1 & Jolpica live APIs, verified schema fields and latencies in `spikes/probe_sources.py`, created `docs/data-sources.md`. Task Lock advanced to P0.4 Gate G0.
