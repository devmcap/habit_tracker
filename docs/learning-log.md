# Learning log

Personal record of what I learn while building this project: concepts, my own answers,
my mistakes and their corrections. It is the source for the quizzes at the start and end
of every phase.

## How it works

- **Every concept I am tested on gets an entry**, with my answer in my own words, what was
  wrong or missing, and the corrected explanation.
- **Mistakes stay written.** Corrections are added below them; the original answer is never
  deleted. Seeing what I got wrong is the point.
- **Status** of each concept:
  - `NEW` — explained, not tested yet.
  - `REVIEW` — tested, answer wrong or incomplete. Asked again in the next quiz.
  - `OK` — answered correctly in a later quiz without help.
- A concept only moves to `OK` when I get it right **in a later session**, not right after
  the explanation (short-term memory does not count).

## Quizzes

| When | What it covers | Goal |
|---|---|---|
| Start of a phase | The concepts the phase needs + every `REVIEW` entry | Find gaps before building on them |
| End of a phase | What the phase taught | Prove I understood it, not only that the code works |
| Occasionally | Random `OK` entries from old phases | Check I have not forgotten |

Question types: explain a concept, predict what a piece of code does, find the bug in a
snippet, choose between two designs and justify it. The last two matter most, because my
job is reading and directing code that someone else (often an AI) wrote.

Quiz results are recorded in the history table at the end.

---

## Phase 0 — Definition

### Git: `git add` vs `git commit`

- **Status**: `REVIEW`
- **My answer**: `git add` puts files in staging, the area that prepares what will go into the
  commit. `git commit` takes what is staged and makes a "capture" of the changes. Many commits
  form a history of what I have done.
- **Mistakes / gaps**:
  1. I said staging prepares files "for upload". A commit uploads nothing: it is local.
     Uploading to a server (GitHub) is `git push`.
  2. A commit is a snapshot of **all tracked files**, not only of the changes. The changes
     ("diff") are computed by comparing two snapshots.
  3. I did not explain **why** there are two steps.
- **Correct explanation**: Two steps exist so I can choose what goes into each commit. If in
  one session I fix a bug and start a feature, I can commit the fix alone and the feature
  later (even part of a file, with `git add -p`). Each commit then makes sense on its own and
  can be undone without losing the other. History is not only a log: it lets me go back to any
  point and find which commit introduced a bug.

### Conventional Commits: choosing the type

- **Status**: `OK` (answered correctly on the first try, with no previous explanation)
- **My answer**: The commit adding the learning log is `docs`, because the file documents the
  learning in the project. It does not add a feature or fix a bug.
- **Additional notes**: The type describes the **effect of the change**, not the file type.
  Common types: `feat` (new behavior for the user), `fix` (corrects wrong behavior), `docs`,
  `test`, `refactor` (changes code without changing behavior), `chore` (tooling, config).
  Format: `type(optional-scope): imperative summary`, for example
  `feat(habits): add weekly schedule`.

### User stories and MVP

- **Status**: `NEW`
- **What I thought**: a user story was a step the user must perform, or a list to go through
  one by one.
- **Correct explanation**: A user story is a **capability the system must offer, told from the
  point of view of who uses it**: "As [who], I want [what], so that [why]". The "so that" part
  records the reason, so nobody removes the feature without knowing why it exists. Stories are
  used to plan (one unit of work), prioritize (in or out of the MVP) and verify (each one gets
  a test). The **MVP** (Minimum Viable Product) is the smallest version that already solves the
  real problem.

### Friction

- **Status**: `NEW`
- **Explanation**: Every extra step in a flow (forms, confirmations) makes people drop out.
  That is why sign-up with Google is in the MVP: someone who only wants to try the app should
  not have to fill in forms.

### Store facts, compute derived values

- **Status**: `NEW`
- **Explanation**: A streak is not stored as a counter that is incremented every day. We store
  the facts (completion of habit H on date D) and compute the streak from them. A stored
  result can get corrupted by any bug and cannot be rebuilt; facts can always be recomputed.

### "Today" depends on the user's timezone

- **Status**: `NEW`
- **Explanation**: The server and each user can be in different timezones, so "today" must be
  computed with the user's timezone, never the server's. Dates and timezones are a classic
  source of real-world bugs.

### Authentication vs authorization

- **Status**: `NEW`
- **Explanation**: Authentication answers "who are you?" (login). Authorization answers "what
  are you allowed to see or do?" (only your own habits). Being logged in does not mean you can
  access everything: every database query must filter by owner.

### Secrets never go into the repository

- **Status**: `NEW`
- **Explanation**: Credentials live in `.env`, which is listed in `.gitignore`. A secret that
  was ever committed must be treated as leaked, even if it is deleted later, because it stays
  in the history.

---

## Quiz history

| Date | Type | Phase | Result | Notes |
|---|---|---|---|---|
| 2026-10-27 | Check | 0 | Partial | `git add` vs `git commit`: right idea, three gaps (see entry) |
| 2026-10-27 | Check | 0 | Pass | Conventional Commits type: `docs`, correct reasoning |

## Pending

- Phase 1 diagnostic quiz (5 questions: Git `add`/`commit`/`push` review, HTTP request parts,
  `GET` vs `POST` and status codes 200/404/500, what `@app.get("/habits")` does, why `venv`).
  To be answered at the start of the next session.
