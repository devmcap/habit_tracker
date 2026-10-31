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
- **Retest 2026-10-29 (phase 1 diagnostic)**: still `REVIEW`, but better.
  - **My answer**: `add` chooses which files go into the commit (staging); `commit` is the
    capture of those changes with a message (Conventional Commits) and builds the history;
    `push` is the final step that uploads the commits "and they stay saved". Two steps exist
    so I can split changes into separate commits; with one step "there would be no way to
    upload changes separately".
  - **Fixed**: gap 3. I now explain why there are two steps.
  - **Still open**:
    1. Commits are already saved after `git commit`, on my machine, and I can go back to them
       without any internet. `push` does not "save" them: it **copies** them to a remote
       (GitHub) so they are backed up and shared. Two steps are about **composing** commits,
       not about uploading.
    2. I still said a commit captures "the changes". It is a snapshot of **all tracked
       files**; the diff is computed by comparing two snapshots.
  - **Same day, again**: I said the file "we are going to upload" when talking about a commit.
    A commit uploads nothing; only `push` does.
- **Check 2026-10-29 (after the first `push` to GitHub)**: correct, but the same day as the
  explanation, so it stays `REVIEW` until a later session confirms it.
  - **Question 1**: what traveled to GitHub with `push`, loose files or commits?
    **My answer**: the commits.
  - **Question 2**: if I edit `docs/roadmap.md` and commit without pushing, what does someone
    opening the repository on GitHub see? **My answer**: the commits that were pushed; the new
    one is local and has not been uploaded.
  - **Fixed**: open point 1. `commit` is local, `push` copies commits to the remote.
  - **Precision**: `push` sends the commits the remote does not have yet (each one with its
    full snapshot) and moves the remote branch (`origin/main`) to point at the last one. In
    question 2, GitHub would show the **previous** version of `roadmap.md`, and
    `git status` would say `Your branch is ahead of 'origin/main' by 1 commit`.
  - **Not tested yet**: open point 2 (snapshot of all tracked files vs "the changes").
  - **Same day, later**: I said "para subir docs/learning-log.md" when proposing a commit
    message. Vocabulary slip again: a commit **records** locally; only `push` uploads.
- **Incident 2026-10-31**: commit `8417e7b` was pushed with `# @app.get("/health")` commented
  out (left over from the slice 1 check experiment), so `GET /health` returned 404 on
  GitHub. Fixed in `64f3564`.
  - **Lesson**: before every commit, read what is staged (`git diff --staged`, or the diff
    view in PyCharm's Commit window). A commit records **exactly** what is staged, including
    leftovers from experiments.

### Conventional Commits: choosing the type

- **Status**: `REVIEW` (type: OK; message format: see check of 2026-10-29)
- **My answer**: The commit adding the learning log is `docs`, because the file documents the
  learning in the project. It does not add a feature or fix a bug.
- **Additional notes**: The type describes the **effect of the change**, not the file type.
  Common types: `feat` (new behavior for the user), `fix` (corrects wrong behavior), `docs`,
  `test`, `refactor` (changes code without changing behavior), `chore` (tooling, config).
  Format: `type(optional-scope): imperative summary`, for example
  `feat(habits): add weekly schedule`.
- **Recheck 2026-10-29**: still `OK`, with a slip. I chose the right type but wrote `doc`
  instead of `docs`. Types are an exact vocabulary: tools such as commitlint reject `doc`.
  My reason was "the file belongs to the documentation" (file type); the better reason is the
  effect: the change only adds documentation, no behavior.
- **Check 2026-10-29 (phase 1, slice 1 commits)**: types right (`docs`, `feat`), format wrong.
  Moves back to `REVIEW` for the format.
  - **My messages**: `(docs) phase 1 started, firsts concepts asked` and
    `(feat) add backend with first rute get /health`.
  - **Mistakes / gaps**:
    1. Format is `type: summary` or `type(scope): summary`. Parentheses hold the optional
       **scope**, never the type: `(docs) ...` is not recognized by tools.
    2. The summary is an **imperative verb** describing what the commit does ("add",
       "record"), not a past-tense status ("phase 1 started").
    3. Typos stay in history forever: "firsts" -> "first", "rute" -> "route".
  - **Better**: `docs: record phase 1 slice 1 check results` and
    `feat(backend): add FastAPI app with GET /health endpoint`.
- **Commit 2026-10-31 (written without a model answer)**: format fixed; stays `REVIEW` until
  the phase 1 closing quiz.
  - **My message**: `fix(main): uncomment decorator for GET /health endpoint`.
  - **Right**: type `fix`, `type(scope): summary` format, lowercase imperative.
  - **To improve**:
    1. Keep scopes consistent: the previous commit used `backend`. The scope names an area
       of the project, not a file.
    2. Describe the **effect**, not the mechanics: "uncomment decorator" says how; the
       reader of the history needs what, for example `fix(backend): restore GET /health route`.
- **Commits 2026-10-31 (slice 2)**: code and docs correctly split into two commits.
  - `feat(main): add GET /habits and GET /habits/{habit_id} endpoint with temporary in-memory habits list data`:
    scope `main` again (use `backend`) and far too long; keep the summary under about 72
    characters and put details in the body. Better: `feat(backend): add endpoints to list and get habits`.
  - `docs: add new explanation of query path and query params`: typo ("query path"); the
    commit records check results, so better `docs: record phase 1 slice 2 check results`.
  - `feat(backend): add limit to habit list`: good. Right scope, short, imperative,
    describes the effect.

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

## Phase 1 — Skeleton

### Parts of an HTTP request

- **Status**: `REVIEW`
- **My answer**: method (GET, POST, PUT, DELETE, PATCH), headers, body, "and I do not remember
  more".
- **Mistakes / gaps**:
  1. I forgot the most important part: **where** the request goes, the URL path (with its
     optional query string, `?date=2026-10-29`).
- **Correct explanation**: An HTTP request is plain text with four parts:
  1. **Request line**: method + path + HTTP version, for example `GET /habits?done=false HTTP/1.1`.
  2. **Headers**: metadata as `Name: value` lines (`Host`, `Content-Type`, `Authorization`...).
  3. **An empty line**, which marks the end of the headers.
  4. **Body** (optional): the data sent, usually JSON in an API. `GET` normally has none.

  The response has the same shape: status line (`HTTP/1.1 200 OK`), headers, empty line, body.

### `GET` vs `POST`

- **Status**: `REVIEW`
- **My answer**: `GET` sends the information in the URL and does not encrypt it; `POST` sends
  it in the body and encrypts it. Sensitive data should always go by `POST`.
- **Mistakes / gaps**:
  1. **`POST` encrypts nothing.** Encryption comes from **HTTPS** (TLS), and it protects the
     whole request: path, query string, headers and body alike. Over plain HTTP, a `POST`
     body is readable by anyone in between, exactly like a URL.
  2. The advice (sensitive data in the body, not the URL) is right, but for a different
     reason: URLs end up in server logs, browser history and bookmarks, and are sent to other
     sites in the `Referer` header. Bodies are not.
  3. I did not say what each method **means**.
- **Correct explanation**: The method states the **intent** of the request.
  - `GET` **reads** a resource. It must not change anything on the server ("safe"), so
    repeating it is harmless and browsers and proxies may cache it. Parameters go in the
    query string.
  - `POST` **sends data to be processed**, usually to create something (`POST /habits` creates
    a habit). Repeating it can create a duplicate. Data goes in the body.

### HTTP status codes 200, 404, 500

- **Status**: `OK` (answered correctly on the first try, with no previous explanation)
- **My answer**: 200 OK, the request succeeded. 404 not found, the address does not exist
  ("or you have no permission"). 500 server error; the client is not to blame.
- **Additional notes**: Codes are grouped by first digit: 2xx success, 4xx the client did
  something wrong, 5xx the server failed. The "no permission" case has its own codes:
  **401** (I do not know who you are: not logged in) and **403** (I know who you are and you
  are not allowed). Even so, my intuition was useful: in phase 3, asking for another user's
  habit will return **404**, not 403, on purpose, so the API does not reveal that the habit
  exists.

### What `@app.get("/habits")` does

- **Status**: `REVIEW`
- **My answer**: It creates a route with the path `/habits`; `@app.<http-method>` creates the
  route with the HTTP method I want.
- **Mistakes / gaps**:
  1. I did not mention the **function** below the decorator, which is the whole point: the
     route is a link between a request and that function.
- **Correct explanation**: `@app.get("/habits")` is a **decorator**: it receives the function
  defined below it and **registers** it in the app as the handler for the pair
  (`GET`, `/habits`). When a request with that method and path arrives, FastAPI calls the
  function, and converts its return value (a dict, a list, a model) into a JSON response with
  status 200. A `POST /habits` would not match: same path, different method, different
  handler.
- **Check 2026-10-29 (phase 1, slice 1)**: correct, same day, so it stays `REVIEW`.
  - **Question**: if I delete `@app.get("/health")` and restart, what does `GET /health`
    return? **My answer**: `404 Not Found`, because the decorator defines the route and
    without it the route does not exist.
  - **Precision**: the function `health` still exists; it is just never **registered** in the
    app's route table, so FastAPI has nothing to call for that path.
- **Question 2026-10-31**: "what is `list_habits`? Nothing defines it" (it is defined right
  under `@app.get("/habits")`). The confusion: no code ever calls `list_habits(...)`.
  - **Explanation**: I never call handlers; **FastAPI** does, after the decorator registers
    them. The function name is for readers of the code (and the title in `/docs`); the URL
    comes only from the decorator. Renaming the function does not change the URL.

### The `app` object

- **Status**: `NEW`
- **My question**: is my application "inside" the variable `app`?
- **Explanation**: `FastAPI(...)` creates an **object** (an instance of the `FastAPI` class)
  and `app` is just the name that points to it. The object holds the route table and the
  settings. The file is a recipe: when Python imports `app/main.py` it runs it top to
  bottom, line 3 builds the empty object, and each `@app.get(...)` adds a route to its
  table. After the import, "my application" is that object in memory with its routes.
  `uvicorn app.main:app` means "import module `app.main` and take the variable `app`";
  Uvicorn keeps it and calls it once per request. The name `app` is a convention: with
  `api = FastAPI()` the command would be `uvicorn app.main:api`.

### Why a `venv`

- **Status**: `REVIEW` (close; two corrections)
- **My answer**: A virtual environment stores all the project's dependencies, which avoids
  installing everything on my own machine. The operating system has dependencies that projects
  also use, and installing on top of them could cause conflicts; the venv isolates everything.
- **Mistakes / gaps**:
  1. Packages **are** installed on my machine: in a folder inside the project (`.venv/`)
     instead of the global Python installation.
  2. I missed the most common conflict: **between projects**. Project A needs
     `fastapi==0.100` and project B needs `fastapi==0.115`; with one global installation, only
     one version can exist.
- **Correct explanation**: A venv is a folder with its own Python interpreter link and its own
  `site-packages`. Each project gets its own versions, so projects cannot break each other or
  the system Python. Together with a dependency file (`requirements.txt` or `pyproject.toml`)
  it makes the setup **reproducible**: anyone can recreate the same environment. It only
  isolates **Python packages**; isolating the whole system (OS libraries, database) is what
  Docker does in phase 8.
- **Check 2026-10-29 (phase 1, slice 1)**: partial, stays `REVIEW`.
  - **Question**: a teammate clones the repository. Why is `.venv/` missing, and which two
    commands give them my environment?
  - **My answer**: it is listed in `.gitignore`, which defines the files ignored when
    committing. Command: `pip install -r requirements.txt`.
  - **Mistakes / gaps**:
    1. I gave one command, not two. First the venv must exist: `py -3.14 -m venv .venv`.
       Without it, `pip install` goes into the global Python, the exact thing the venv avoids.
    2. I did not say **why** it is ignored, only that it is.
  - **Correct explanation**: from `backend/`, `py -3.14 -m venv .venv`, then
    `.venv\Scripts\python -m pip install -r requirements.txt` (or activate first and use
    `pip`). `.venv/` is not committed because it is **rebuildable** from `requirements.txt`,
    heavy (thousands of files), and tied to my machine (Windows binaries, absolute paths). The
    repository keeps the recipe (`requirements.txt`), not the result. Precisely,
    `.gitignore` stops untracked files from being added with `git add`, so they never get
    into a commit.
- **Incident 2026-10-31**: `uvicorn` was "not recognized" in a new PowerShell terminal,
  although it worked two days before.
  - **Explanation**: activating a venv is **not permanent**. `Activate.ps1` only prepends
    `.venv\Scripts` to the `PATH` of **that terminal**. Every new terminal must activate it
    again (the prompt shows `(.venv)` when active), or call the venv's Python directly:
    `.\.venv\Scripts\python -m uvicorn app.main:app --reload`.

### Server, ASGI and framework

- **Status**: `NEW`
- **Explanation**: FastAPI does not listen on any port. A **server** (Uvicorn) opens the port,
  reads the bytes from the network and parses HTTP. **ASGI** is the contract between that
  server and the framework, so the server can be swapped without touching my code. Flask uses
  **WSGI**, its synchronous predecessor; the "A" in ASGI means asynchronous: while one request
  waits for something slow (database, sending an email), the server can serve others.
- **Check 2026-10-29 (phase 1, slice 1)**: correct, same day, so it stays `NEW` until a later
  session.
  - **Question**: who opens port 8000, FastAPI or Uvicorn? **My answer**: Uvicorn, the server.

### One repository or two (monorepo vs polyrepo)

- **Status**: `NEW`
- **What I thought**: a big backend should go in its own repository.
- **Explanation**: Size is not the criterion (Google keeps almost everything in one
  repository). What decides it is **who works on it and how it changes**:
  - **Same repository** when changes cross both sides: a new API field and the screen that
    shows it go in one commit, so history never has a frontend that expects an API that does
    not exist yet. One history, one place for docs.
  - **Separate repositories** when different teams own each part, they are released and
    versioned independently, or they need different access permissions.
  - Repository layout and deployment are independent: backend and frontend from one
    repository can still be deployed separately. The cost of a monorepo is CI work, such as
    not running frontend tests when only the backend changed.

### Path params vs query params

- **Status**: `REVIEW`
- **Explanation**: In `GET /habits/42?done=true&limit=10`, `42` is a **path param** and
  `done`, `limit` are **query params**.
  - **Path param**: part of the route (`/habits/{habit_id}`), required, **identifies** a
    resource. Removing it changes which resource I am talking about.
  - **Query param**: after `?`, separated by `&`, usually optional with a default;
    **filters, sorts, paginates** or sets options. Removing it only changes how the answer
    comes back.
  - In FastAPI, a function parameter whose name matches `{...}` in the route is a path
    param; any other simple-typed parameter is a query param. With a default it is
    optional; without one it is required (422 if missing).
- **Check 2026-10-31 (phase 1, slice 2)**: partial.
  - **Question**: `done: bool | None = None` changed to `done: bool = False`; what does
    `GET /habits` return with no parameters, and why is it a bug?
    **My answer**: only the habits not done yet, because the default is `False`; a bug "for
    that reason".
    **Gap**: the behavior is right, but the reason is the consequence: no URL could return
    **all** habits any more. `None` is the third state that means "no filter was given".
  - **Question**: should `limit` (at most N habits) be a path or a query param, and how would
    I declare it? **My answer**: query param, because it goes after `?`, can be optional, and
    is not in the route of the decorator. Example:
    `@app.get('/habits/{habit_id}') def get_habit(habit_id: int, limit: int | None = None)`.
    **Mistake**: right kind of parameter, wrong endpoint. `/habits/{habit_id}` returns **one**
    habit, so there is nothing to limit. `limit` belongs to the list endpoint:
    `@app.get("/habits") def list_habits(done: bool | None = None, limit: int | None = None)`.

### Automatic validation: 404 from my code vs 422 from FastAPI

- **Status**: `NEW`
- **Explanation**: Everything in a URL arrives as text. Type hints (`habit_id: int`,
  `done: bool`) tell FastAPI what I expect; it uses **Pydantic** to convert (`"42"` -> `42`)
  and to reject invalid input with **422 Unprocessable Entity** before my function runs. The
  error's `loc` field says where the bad value was (`["path", "habit_id"]`,
  `["query", "done"]`). A **404** for a missing habit is different: the input is valid, my
  code looks for the habit and decides to `raise HTTPException(status_code=404, ...)`.
- **Check 2026-10-31 (phase 1, slice 2)**: correct, same day, so it stays `NEW`.
  - **Question**: why does `/habits/99` return 404 and `/habits/abc` 422, and who generates
    each error? **My answer**: 99 is a valid int, my code does not find it in the list and
    raises `HTTPException` 404 with `Habit not found`; `abc` is not an int, so FastAPI rejects
    it with 422 while validating with Pydantic.

### Slicing and negative indexes

- **Status**: `NEW`
- **Where I got stuck**: I tried to put a counter inside a list comprehension to stop after
  `limit` items. A comprehension has no `break`; the clean way is two steps: **filter**, then
  **cut** the result with slicing.
- **Explanation**: `items[:n]` returns the first `n` items (no error if `n` is bigger than
  the list). `items[:None]` returns the whole list, so an optional `limit` needs no `if`.
  **Negative indexes count from the end**: `items[-1]` is the last item and `items[:-1]` is
  everything except the last one.
- **My discovery**: I expected `?limit=-1` to return all habits; it returned all except the
  last. Valid Python, but a bug for the API: nonsense input must be rejected, not
  interpreted. Same for `limit=0`, which returned `[]`.
- **Structure lesson**: my first version repeated `[:limit]` in both branches of the `if`.
  When both branches end with the same step, that step goes after the `if`.

### Validation constraints with `Query`

- **Status**: `NEW`
- **Explanation**: Types reject the wrong kind of value (`limit=abc`); **constraints** reject
  values of the right kind that make no sense (`limit=-1`).
  `limit: Annotated[int | None, Query(ge=1)] = None` keeps the type `int | None` and adds the
  rule "greater than or equal to 1". FastAPI checks it before calling the function and
  answers 422 with `"type": "greater_than_equal"`. Other constraints: `gt`, `le`, `lt`,
  `max_length`.
- **Import note**: `from fastapi import Query` is the public import; PyCharm suggested
  `from fastapi.params import Query`, an internal module. It works today, but internal
  paths can change between versions.

---

## Quiz history

| Date | Type | Phase | Result | Notes |
|---|---|---|---|---|
| 2026-10-27 | Check | 0 | Partial | `git add` vs `git commit`: right idea, three gaps (see entry) |
| 2026-10-27 | Check | 0 | Pass | Conventional Commits type: `docs`, correct reasoning |
| 2026-10-29 | Recheck | 0 | Pass (slip) | Conventional Commits: right type, wrote `doc` instead of `docs` |
| 2026-10-29 | Diagnostic | 1 | Partial | Status codes OK; Git improved but still `REVIEW`; HTTP parts, `GET`/`POST` (encryption myth), decorator and venv to `REVIEW` |
| 2026-10-29 | Check | 1 | Pass | `commit` (local) vs `push` (copies commits to the remote): both answers right; same day, so still `REVIEW` |
| 2026-10-29 | Check | 1 | Partial | Slice 1 (`GET /health`): decorator removed -> 404 OK; Uvicorn opens the port OK; venv: missed the `venv` creation command and why `.venv/` is not committed |
| 2026-10-31 | Check | 1 | Partial | Slice 2 (`/habits`): 404 vs 422 OK; `bool \| None` behavior OK, weak reason; `limit` is a query param OK, but put on the single-habit endpoint |
| 2026-10-31 | Exercise | 1 | Pass (with hints) | Implemented `limit` myself: filter then slice; found the `limit=-1` bug by testing; added `Query(ge=1)` |

## Pending

- Phase 1 closing quiz must include every `REVIEW` entry above: Git `add`/`commit`/`push`,
  Conventional Commits format, HTTP request parts, `GET` vs `POST`, `@app.get` decorator,
  `venv`, path vs query params.
