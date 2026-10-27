# Roadmap

Budget: about 16 h/week (Tue 2 h, Thu 3 h, Fri 3 h, Sat 4 h, Sun 4 h). Target: about 6 months.
Estimates are rough and will be revised at the end of each phase.

| Phase | Deliverable | Key concepts | Estimate |
|---|---|---|---|
| 0. Definition | `docs/product.md` approved, repository ready | Scope, user stories, Git basics | 1 week |
| 1. Skeleton | Minimal FastAPI app, project layout, tooling | HTTP, ASGI, routing, dependency injection, virtual environments | 1–2 weeks |
| 2. Data | Models, migrations, CRUD for habits and tasks | SQL by hand first, then ORM; sessions, transactions, Alembic | 2–3 weeks |
| 3. Users | Register, login (password + Google), per-user data isolation | Password hashing, sessions vs JWT, OAuth 2.0 / OpenID Connect, authentication vs authorization | 3–4 weeks |
| 4. Tests | Test suite running against an isolated test database | Test-first, fixtures, isolation (continues in every later phase) | ongoing |
| 5. Frontend | React app: login + today view + habits + tasks | JavaScript/TypeScript, React, state, calling an API, CORS | 4–6 weeks |
| 6. Reminders | Daily reminder at the user's chosen time | Background jobs, scheduling, timezones, sending email/push | 2 weeks |
| 7. Gamification | Points, perfect-day bonus, rewards | Business rules as testable pure functions | 2 weeks |
| 8. Deploy | Friends can use it from their phones | Docker, environment variables, secrets, HTTPS | 2 weeks |

## Learning loop (every step)

1. Concept first: why it exists and what problem it solves.
2. The AI writes a small slice of code.
3. I read the whole diff and ask about anything unclear.
4. Check: I answer 2–3 questions about the slice. If I cannot, we do not move on.
5. Sometimes I make a small change myself, to prove I can modify it.
6. I make the commit with a message I write myself.
