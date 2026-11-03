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

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **My answer**: `add` puts the changed files in staging to choose what goes into the
    commit; `commit` takes a capture of the whole project and stores it on my machine, so I
    can review commits without internet; `push` uploads those commits to the remote on GitHub.
  - **Fixed**: open point 2. A commit is a capture of the **whole project**, not only of the
    changes, and it is local.

### Conventional Commits: choosing the type

- **Status**: `REVIEW` (type: `OK` since the 2026-11-03 closing quiz; message format still `REVIEW`)
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
  - `fix(backend): change Query import from FastAPI and documentation.`: not a `fix` (no
    behavior changed), trailing period, vague. Better: `docs(backend): describe /habits query parameters`.
  - `docs: completed phase 1 slice 2`: past tense status again. Better:
    `docs: record phase 1 slice 2 results`.
- **Commits 2026-10-31 (slice 3)**: both imperative now; the remaining gaps are type choice
  and English.
  - `feat(backend): add dependencies injection to get habits data`: behavior did not change,
    so the type is `refactor`. English: "dependency injection" and "habit data" (see
    noun-as-adjective rule below). Better: `refactor(backend): inject habit store with Depends`.
  - `docs: register slice 3 of phase 1`: imperative and clear. "Register" is a false friend
    of "registrar": in English it means to sign up or enrol (register a user, a domain).
    To write something down is **record**. Better: `docs: record phase 1 slice 3 results`.
- **English for commit summaries** (I am a native Spanish speaker; these are my usual slips):
  - Test: the summary must complete "If applied, this commit will ...". Base verb, no `-ed`,
    no `-s`, no final period.
  - A noun used as an adjective stays **singular**: habit tracker, habit data, dependency
    injection (not "habits data", "dependencies injection").
  - Useful verbs: `add` (new thing), `remove`, `fix`, `update` (change existing content),
    `rename`, `move`, `record` (write results down), `describe` / `document`,
    `extract` / `inject` (refactors), `restore` (bring back something that broke).
  - Type by **effect**: new behavior `feat`; wrong behavior corrected `fix`; same behavior,
    different code `refactor`; only documentation `docs`.
- **Closing quiz 2026-11-03 (phase 1)**: type 3/3, format still `REVIEW`.
  - **Question**: which type for (a) a new `DELETE /habits/{habit_id}` endpoint, (b) fixing
    `limit=-1` returning data instead of an error, (c) renaming an internal function without
    changing the API? **My answer**: `feat`, `fix`, `refactor`. All right.
  - **Same day, real commit**: my first draft was
    `record corrections in commit messages in learning log`.
    1. No type: it must start with `docs:`.
    2. "corrections in commit messages" reads as if I had corrected something *inside* the
       messages; what I recorded is feedback *about* them: "commit message feedback".
    3. Missing article ("in **the** learning log"); the phrase can go, since `docs` and the
       diff already say where.
    4. Right: imperative `record` (not `register`), lowercase, no final period.
  - **Final message**: `docs: record commit message feedback` (`6d4b7b6`). Good.
  - **Second commit**: `docs: record exam result for phase 1 closing` (`e8c4266`). Format
    right without help. English: "for phase 1 closing" sounds unnatural; nouns used as
    adjectives go in front: `docs: record phase 1 closing quiz results`. Use the log's
    words ("quiz", not "exam") so history and log are easy to search together.

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

- **Status**: `REVIEW`
- **Explanation**: A streak is not stored as a counter that is incremented every day. We store
  the facts (completion of habit H on date D) and compute the streak from them. A stored
  result can get corrupted by any bug and cannot be rebuilt; facts can always be recomputed.
- **Phase 2 diagnostic 2026-11-03**: not applied. Asked what is wrong with a `done` column
  in the habit row, I saw no problem. See "Modeling habits: completions, not a `done`
  column" in phase 2.

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

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **My answer**: method, HTTP version, path, headers, optional body, "and a final empty
    line that marks where the request ends".
  - **Fixed**: the path (the gap of the diagnostic).
  - **Precision**: the empty line separates the **headers from the body**; it does not end
    the request. Where the body ends is given by the `Content-Length` header (or the
    connection closing).

### `GET` vs `POST`

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **My answer**: `GET` reads; calling it 20 times changes nothing. `POST` sends data that
    can be stored or change something. `POST` is not safer and encrypts nothing; HTTPS
    encrypts the body so a man in the middle cannot read it.
  - **Fixed**: the encryption myth of the diagnostic.
  - **Precision**: HTTPS encrypts the **whole** request (path, query string, headers, body),
    not only the body. "Changes nothing when repeated" is called a **safe** method.

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

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **My answer**: it is a decorator that links the `GET` method and the `/health` path of
    the app to the function below; without it, `/health` is not found because the route is
    not defined anywhere.
  - **Fixed**: the function is now part of my answer (the gap of the diagnostic).

### The `app` object

- **Status**: `REVIEW`
- **My question**: is my application "inside" the variable `app`?
- **Explanation**: `FastAPI(...)` creates an **object** (an instance of the `FastAPI` class)
  and `app` is just the name that points to it. The object holds the route table and the
  settings. The file is a recipe: when Python imports `app/main.py` it runs it top to
  bottom, line 3 builds the empty object, and each `@app.get(...)` adds a route to its
  table. After the import, "my application" is that object in memory with its routes.
  `uvicorn app.main:app` means "import module `app.main` and take the variable `app`";
  Uvicorn keeps it and calls it once per request. The name `app` is a convention: with
  `api = FastAPI()` the command would be `uvicorn app.main:api`.
- **Closing quiz 2026-11-03 (phase 1)**: too vague, moves to `REVIEW`.
  - **My answer**: an instance of `FastAPI` "that defines where our API is".
  - **Gap**: it has two concrete jobs. It is the **route table** (every `@app.get` adds an
    entry to it), and it is the **ASGI application**: Uvicorn imports it and calls it on
    every request.

### Why a `venv`

- **Status**: `REVIEW` (purpose fixed; creation command and "why not committed" still open)
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
- **Closing quiz 2026-11-03 (phase 1)**: partial, stays `REVIEW`.
  - **My answer**: it holds the project's dependencies so several projects can use
    different versions (Flask, for example) without conflicts; created with
    `python -m venv .venv`; activated in every new terminal; not committed "because the
    dependencies are installed in our system with `requirements.txt`" (I admitted I did not
    remember).
  - **Fixed**: gap 2, the conflict **between projects**; activation per terminal.
  - **Still open**:
    1. On this machine there is no `python` on the `PATH`: the command is
       `py -3.14 -m venv .venv`. Activate in PowerShell with `.\.venv\Scripts\Activate.ps1`.
    2. Packages are installed **inside `.venv/`**, not in the system; that contradicts my
       own first sentence.
    3. Why `.venv/` is not committed (second time missed): heavy, tied to my machine, and
       rebuildable from `requirements.txt`. The repository keeps the recipe, not the dish.
- **Retest 2026-11-03 (phase 2 diagnostic, same day as the correction)**: almost right, stays
  `REVIEW` until a later session.
  - **Question**: exact commands, from `backend/`, for a teammate on Windows to start the API,
    and why `.venv/` is not in the repository.
  - **My answer**: `py -3.14 -m venv .venv`, `.\.venv\Scripts\Activate.ps1`,
    `pip install -r requirements.txt`; not committed because it is heavy, tied to my machine,
    and `requirements.txt` is the recipe to rebuild it.
  - **Missing**: the last step, the one that starts the API: `uvicorn app.main:app --reload`.

### Server, ASGI and framework

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
- **Explanation**: FastAPI does not listen on any port. A **server** (Uvicorn) opens the port,
  reads the bytes from the network and parses HTTP. **ASGI** is the contract between that
  server and the framework, so the server can be swapped without touching my code. Flask uses
  **WSGI**, its synchronous predecessor; the "A" in ASGI means asynchronous: while one request
  waits for something slow (database, sending an email), the server can serve others.
- **Check 2026-10-29 (phase 1, slice 1)**: correct, same day, so it stays `NEW` until a later
  session.
  - **Question**: who opens port 8000, FastAPI or Uvicorn? **My answer**: Uvicorn, the server.
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **Question**: why is `python main.py` not enough? **My answer**: Uvicorn is the server;
    it has to be started and pointed at our `app`.
  - **Precision**: `python main.py` only builds the `app` object and exits; nothing stays
    listening on a port.

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

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`.
  - **Question**: in `GET /habits/3?done=true`, which is the path param and which the query
    param, and when do I use each? **My answer**: `3` is the path param (the habit id),
    `done` the query param; path for a concrete resource ("give me habit 3"), query to filter
    ("only done ones").

### Automatic validation: 404 from my code vs 422 from FastAPI

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
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
- **Closing quiz 2026-11-03 (phase 1)**: 4/4, moves to `OK`.
  - **Question**: status code and who generates it for `/habits/99`, `/habits/abc`,
    `/habits?limit=0`, `/habits?done=maybe`? **My answer**: 404 from my code; 422 from
    FastAPI (Pydantic); 422 from FastAPI because of `Query(ge=1)`; 422 from FastAPI.
  - **Note**: I called 422 "Unprocessable Content", its current name (RFC 9110); older
    documents call it "Unprocessable Entity". Same code.

### Slicing and negative indexes

- **Status**: `REVIEW`
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
- **Closing quiz 2026-11-03 (phase 1)**: results right, reason missing, moves to `REVIEW`.
  - **Question**: with 3 habits, what do `[:2]`, `[:None]` and `[:-1]` return, and why was
    `limit=-1` a bug? **My answer**: first and second; all; first and second. I did not
    remember why `-1` was a bug: "a negative limit is like saying show nothing, and it still
    shows".
  - **Gap**: I computed `[:-1]` right but did not connect it: Python reads `-1` as "count
    from the end", so `?limit=-1` silently meant "all except the last". The bug is that
    nonsense input was **interpreted** instead of **rejected**. `Query(ge=1)` makes FastAPI
    answer 422 before my function runs.

### Validation constraints with `Query`

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
- **Explanation**: Types reject the wrong kind of value (`limit=abc`); **constraints** reject
  values of the right kind that make no sense (`limit=-1`).
  `limit: Annotated[int | None, Query(ge=1)] = None` keeps the type `int | None` and adds the
  rule "greater than or equal to 1". FastAPI checks it before calling the function and
  answers 422 with `"type": "greater_than_equal"`. Other constraints: `gt`, `le`, `lt`,
  `max_length`.
- **Import note**: `from fastapi import Query` is the public import; PyCharm suggested
  `from fastapi.params import Query`, an internal module. It works today, but internal
  paths can change between versions.
- **Documenting parameters**: each fact lives in one place. `Query(description=...)`
  explains one parameter and shows next to it in `/docs`; the docstring is a one-line summary
  of the whole endpoint (also shown in `/docs`). Repeating parameter details in both places
  makes them drift apart. A parameter description must make sense on its own, including
  what happens when the parameter is omitted.
- **Closing quiz 2026-11-03 (phase 1)**: correct, moves to `OK`. `limit=0` -> 422 from
  FastAPI because of `ge=1`; whatever the user sends below 1 never reaches my function.

### Dependency injection (`Depends`)

- **Status**: `OK` (phase 1 closing quiz, 2026-11-03)
- **My first reaction**: "I do not see what it is for". Fair: with an in-memory list the
  benefit is invisible; it pays off from phase 2 on.
- **Explanation**: an endpoint **declares** what it needs
  (`store: Annotated[list[dict], Depends(get_habit_store)]`) and **FastAPI provides it**,
  calling `get_habit_store()` on every request. Calling `get_habit_store()` inside the
  endpoint would also keep the data source in one place, but then the endpoint decides
  where its data comes from and nobody can change it from outside. With `Depends`, FastAPI
  decides, so `app.dependency_overrides[get_habit_store] = ...` can plug in other data
  (tests with known data, real data untouched) without changing a line of the endpoints.
  Analogy: a lamp with a plug vs a lamp soldered to the wall wires.
  Coming next: `get_db` (phase 2) opens a session per request and FastAPI always closes it;
  `get_current_user` (phase 3) is written once and reused, answering 401 when not logged in.
- **My summary**: Depends gives the data from one point; with an override, tests use fake
  data and never touch the real source; calling the function directly would force code
  changes to test, or tests would touch real data.
  **Precision**: "one point" is also true of a plain function call. What `Depends` adds is
  **who decides**: FastAPI, so it can be replaced from outside.
- **Check 2026-10-31 (phase 1, slice 3)**: correct, same day, so it stays `NEW`.
  - **Question**: why does `store` not appear in `/docs` while `done` and `limit` do?
    **My answer**: the API user does not need to touch it; it is where the data comes from.
    **Precision**: it is not that the client does not *need* to send it; the client
    **cannot**. FastAPI resolves `Depends` on the server and never reads it from the request,
    so it is not part of the API contract (OpenAPI).
  - **Question**: why does `/habits/1` return 404 in the override demo, and did `get_habit`
    change? **My answer**: the override provides `FAKE_HABITS` (ids 100 and 200); no endpoint
    code changed, only the override in the demo file.
  - **Question**: what does `Depends(get_habit_store())` (with parentheses) pass?
    **My answer**: the result, not the function, so the override would not work.
    **Extra**: `get_habit_store()` would run once at import time, and FastAPI fails at
    startup with `TypeError: [...] is not a callable object`, because it needs something it
    can call on every request.
- **Closing quiz 2026-11-03 (phase 1)**: concept right, moves to `OK`.
  - **Question**: find the bug in `Depends(get_habit_store())`, and what does `Depends` give
    over using `HABITS` directly? **My answer**: the parentheses call the function and pass
    its result; without them `Depends` keeps a reference and FastAPI calls it when needed.
    With the result, an override for tests would not work.
  - **Precision (second time)**: it does not even get to the override. The app **fails at
    startup** with `TypeError: [...] is not a callable object`.

## Phase 2 — Data

### Why a database instead of a list in memory

- **Status**: `REVIEW`
- **My answer (diagnostic 2026-11-03)**: the data reset when the app restarts; people cannot
  change them because they are in the code; people could see possibly sensitive data in the
  code if the app is on the web.
- **Mistakes / gaps**:
  1. A list **can** be changed while the server runs (`HABITS.append(...)`); nobody can yet
     because there is no write endpoint. The real problem is that changes do not
     **persist**.
  2. Clients of a web API never see the server's Python code, only its responses. Here the
     data are visible for another reason: the GitHub repository is public. Real data never
     go into code or Git.
  3. Missing: several server processes (normal in production) each have their **own** list;
     two writes at the same time can overwrite each other; searching a big list is slow
     (databases have indexes); no backups; no rules (nothing stops two habits with the
     same `id`).

### Table, row, column, primary key

- **Status**: `REVIEW`
- **My answer (diagnostic 2026-11-03)**: a table describes an entity (I typed "identidad";
  I meant "entidad"), a row is one record, a column is what the entity is made of, and the
  primary key is "how it is organized". Example: table `habit`; columns `id`, `name`,
  `done`; row `1, "Drink water", true`; primary key `id`. The example is right.
- **Mistake**: the primary key does not organize the table. It **uniquely identifies each
  row**: never repeated, never empty, and it should never change. It is what `/habits/3`
  uses to find one habit.

### First SQL query

- **Status**: `NEW` (right on the first try, no previous explanation)
- **My answer (diagnostic 2026-11-03)**: `SELECT * FROM habit WHERE done = false`. Correct.
- **Note**: **SQL** is the language; **MySQL** is one database that speaks it. This project
  uses **PostgreSQL** (`docs/product.md`).

### Modeling habits: completions, not a `done` column

- **Status**: `REVIEW`
- **My answer (diagnostic 2026-11-03)**: no problem with `done` in the habit; "it is
  complete or not, and that is it". Then I proposed a `habit_status` table
  (`id`, `status`: pending, done, not done) referenced from `habit`.
- **Mistakes / gaps**: a habit **repeats**. `done = true` does not say **which day**.
  1. Tomorrow it must be pending again: something would have to reset it at midnight (and
     whose midnight? every user has a timezone).
  2. The reset **erases history**: a streak (consecutive days) and points cannot be computed.
  3. US11b (mark yesterday as done) is impossible: one boolean has no room for yesterday.
  4. My `habit_status` table is a valid pattern for a list of fixed values, but it still
     stores **one** status per habit, so it has the same problem.
- **Correct explanation**: store the **fact** of each completion (phase 0, "Store facts,
  compute derived values"):
  - `habit`: `id`, `name`, weekdays, ... (what the habit is).
  - `completion`: `id`, `habit_id` (foreign key to `habit.id`), `user_id`, `date`, with a
    rule "one completion per habit and date" (`UNIQUE (habit_id, date)`).
  - "Done today" = a completion exists for that habit with today's local date. Streaks and
    points are computed from these rows. Yesterday is just another row.
  - Contrast: a **task** is one-off ("once completed, it is done"), so a column in the task
    itself (`completed_at`) **is** right there.
- **Check 2026-11-03 (after a day-by-day table diagram)**: correct, same day, so it stays
  `REVIEW`.
  - **My answer**: `completion` stores each completion with its date; a missed day simply
    has no row and nothing has to be done; yesterday can be added later. So I can compute
    the streak and see which days I missed. With `done`, the value is only "now", it is
    overwritten every day without any date, and history is lost.
  - **Precision**: it stores **completions** (facts), not habits: one row per habit and day
    done. A day without a row breaks the streak only if the habit was **scheduled** that day
    (weekdays, US5); a Saturday off for a Mon–Fri habit is not a miss.

### Foreign key

- **Status**: `NEW` (right on the first try, no previous explanation)
- **My answer (diagnostic 2026-11-03)**: a key with a connection to the primary key of
  another table. Correct.
- **Addition**: the database **enforces** it (referential integrity): a completion for a
  habit `99` that does not exist is rejected.

### Transactions

- **Status**: `NEW` (right intuition, no previous explanation)
- **Question (diagnostic 2026-11-03)**: redeeming a reward means "subtract 50 points" and
  "record the redemption"; the server crashes in between.
- **My answer**: it should roll back and not confirm the changes, so when the user comes back
  nothing was redeemed, as if it never happened.
- **Precision**: without a transaction, the points are lost and no redemption is recorded.
  A **transaction** groups both writes: all or nothing (`COMMIT` makes them permanent,
  `ROLLBACK` discards them). The subtraction is not "left pending": it never becomes
  visible. Applying "store facts" again, the balance could even be computed
  (points earned - points spent), so redeeming would be **one** write.

### ORM

- **Status**: `NEW`
- **My answer (diagnostic 2026-11-03)**: never heard of it; guessed "Object Relation Model",
  something to work with database objects from Python. SQL by hand first to have the basics
  before using Python to touch databases.
- **Correct explanation**: **Object-Relational Mapping**. It maps classes to tables and
  objects to rows, and **generates the SQL** for me (here: SQLAlchemy). SQL first because
  when an ORM query is slow or wrong, I must read the SQL it generated to understand why.

### PostgreSQL vs MySQL

- **Status**: `NEW`
- **My question**: how is PostgreSQL different from MySQL?
- **Explanation**: both are relational, free, open source and speak SQL; what I learn here
  works almost the same in both. PostgreSQL is stricter (errors instead of silent fixes),
  has a real `boolean` and richer types (`jsonb`, arrays), and runs structure changes
  (`CREATE`, `ALTER`) **inside a transaction**, so a failed migration is undone. MySQL is
  owned by Oracle (MariaDB is the community fork) and common in classic PHP/WordPress code.
  Dialect example: `GENERATED ALWAYS AS IDENTITY` (PostgreSQL) vs `AUTO_INCREMENT` (MySQL).

### Database server, client and `PATH`

- **Status**: `NEW`
- **Explanation (installation 2026-11-03)**: PostgreSQL 18.6 is a **server**, like Uvicorn
  but for data: it listens on port **5432**, runs as a Windows **service** (starts with the
  computer) and keeps data **on disk**. `psql` is a **client** for typing SQL by hand; my API
  will be another client. `pg_hba.conf` only lets in connections from my own machine, always
  with a password. The `postgres` user is the superuser: its password never goes into the
  repository.
- **`PATH`**: the list of folders where Windows looks for commands. The installer does not add
  `C:\Program Files\PostgreSQL\18\bin`, so I added it for my user with
  `[Environment]::SetEnvironmentVariable(...)`. Unlike `Activate.ps1`, it is permanent, but
  each terminal reads `PATH` only when it starts, so I had to open a new one.

### `psql` basics

- **Status**: `NEW`
- **My mistake (2026-11-03)**: I typed `SELECT version()` without `;` and pressed Enter, then
  `SELECT version();`, and got `ERROR: error de sintaxis ... LÍNEA 2`.
- **Explanation**: without `;`, psql does not run the statement; it keeps it in a buffer and
  waits for more. The prompt shows it: `postgres=#` waits for a **new** statement,
  `postgres-#` means the previous one **continues**. Both lines were joined into one invalid
  statement. `\r` (or `Ctrl+C`) empties the buffer.
  - SQL statements end with `;`. Commands starting with `\` (`\q`, `\r`, `\l`, `\c`, `\dt`)
    belong to psql, not SQL, and need no `;`.
  - SQL always answers with a table, even for one value: `SELECT version();` returned one
    column (`version`) and one row (`(1 fila)`).
- **Coming next**: one server holds several databases. The project gets its own
  (`CREATE DATABASE habit_tracker;`), like one venv per project; `postgres` is for
  administration.

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
| 2026-10-31 | Check | 1 | Pass | Slice 3 (`Depends`): `store` hidden from `/docs` (client cannot send it), override demo 404, `Depends(f())` passes the result |
| 2026-11-03 | Closing | 1 | Pass | 10 concepts to `OK` (Git, commit type, HTTP parts, `GET`/`POST`, decorator, ASGI, path vs query, 404 vs 422, `Query` constraints, `Depends`); `REVIEW`: commit format, venv, `app` object, negative slicing |
| 2026-11-03 | Diagnostic | 2 | Partial | SQL query, foreign key, transaction intuition right; gaps: why a database, primary key, modeling completions (`done` column) |

## Pending

- Phase 1 closed on 2026-11-03 (closing quiz passed).
- Phase 2 diagnostic done on 2026-11-03. Not retested that day, because they were explained
  the same day: the `app` object, slicing with negative indexes, `venv`. Ask them at the
  start of the next session.
- PostgreSQL 18.6 installed on 2026-11-03 (official installer), `psql` on the `PATH`,
  first `SELECT version();` worked.
- Next: `CREATE DATABASE habit_tracker;`, `\l`, `\c habit_tracker`, `\dt`; then phase 2
  slice 1, SQL by hand: `habit` and `completion` tables, primary and foreign keys.
