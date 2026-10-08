# PITWALL: PROJECT STATE (live)

> Update only per `PROJECT_GUIDE.md` section 4.5: edit one section at a time, never rewrite the whole file, never delete history, write only verified or user-stated facts (mark the rest `[unverified]`), no secrets.
> If this file and the repo disagree, the repo wins; flag the mismatch and ask.

## 0. Header
- Guide version: 1.0
- State last updated: 2026-10-09 by Antigravity (P0.1 complete, P0.2 active)
- Repo status: initializing
- Project folder: /home/mallhar/Desktop/f1-project

## 1. Handoff summary (15 lines max; rewrite at every checkpoint)
- Project: PitWall, an F1 race-data backend (ingestion, Postgres, FastAPI, Redis, replay, baseline degradation model).
- P0.1 Intake completed: 10 hrs/week available, Linux OS, moderate terminal comfort.
- User has studied Python OOP fundamentals (classes through @property). Subsequent tech stacks (Git, SQL, Docker, FastAPI, Celery) will be learned via Pause Protocol as phases approach.
- Active Task: P0.2 Repo and environment skeleton.
- Next steps: Initialize git repo, create minimal P0 directory layout, .gitignore, .env.example, requirements/virtualenv, and initial commit.

## 2. Current focus
- Phase: P0
- Task Lock (single active task): P0.2 Repo and environment
- Status: in progress

## 3. Task tracker (`[ ]` todo, `[~]` in progress, `[x]` done, `[-]` cut with reason in Decisions)
**P0** [x] P0.1 Intake · [~] P0.2 Repo and environment · [ ] P0.3 Source spike · [ ] P0.4 Gate G0 · [ ] P0.5 Glossary
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
Include: pinned versions, data source field names and volumes, commands that actually worked, differences between the 2021 course and current library styles.
(none yet)

## 7. Learning queue
Format: `topic | needed for | resource and portion | status (todo / in progress / ready-check passed)`
- Python venv and pip | P0.2 | FCC API course 22:11 to 36:21 | in progress
- Git and GitHub basics | P0.2 | FCC API course 11:23:38 to 11:34:39 | in progress
- Reading tabular data (pandas minimum) | P0.3 | to be chosen at P0.3 | todo
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
(none yet)

## 10. Risks and open questions
- R-1: Data source access, terms or coverage may not match expectations (resolved at P0.3 and Gate G0).
- R-2: The main video course is from 2021; library styles may differ from current versions.
- R-3: Agent rules-file loading in the IDE is unverified; the bootstrap prompt in the guide is the fallback.

## 11. Parking lot (ideas not to build now)
- AI assistant on top of the API (separate later project; keep the API clean for tool-calling).

## 12. Session log (append-only, newest at the bottom)
- **Session 0, 2026-10-08 (planning chat, Claude):** scope and architecture decided; PROJECT_GUIDE.md and PROJECT_STATE.md created. No code written. Next: P0.1 Intake.
- **Session 1, 2026-10-09 (Antigravity):** P0.1 Intake completed. User profile recorded (~10 hrs/week, Linux, moderate terminal, OOP studied). Task Lock set to P0.2 (Repo and environment).
