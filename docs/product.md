# Habit Tracker — Product definition (MVP)

Status: APPROVED by owner (open questions resolved, see Decisions).

## Problem

I forget one-off tasks and I abandon new habits after a few days. A paper agenda fails
because I must remember to open it. The app must:

1. Show what I have to do **today** (tasks + habits) in one place.
2. **Come to me** with reminders, so it does not depend on my memory to open it.
3. Reward completion so keeping a habit feels worth it.

Users: me and a small group of friends. Each user only sees their own data.

## Core concepts

| Concept | Definition |
|---|---|
| Task | One-off item. Optional due date. Once completed, it is done. |
| Habit | Recurring item with a schedule (for example Mon–Fri). It never "ends"; what we store is each completion. |
| Completion | The fact "habit H was done on local date D by user U". Source of truth for streaks and points. |
| Streak | Consecutive scheduled days completed. **Computed** from completions, never stored as a counter. |
| Points | Earned by completing tasks/habits; each item has its own value (see D4). Spent on rewards. |
| Reward | Something the user defines and gives themselves ("buy that book"), with a point cost. |
| Local day | "Today" is defined by the user's timezone, not the server's. |

## MVP user stories

### Accounts
- **US1** As a visitor, I can sign up with my Google account in one click, so I can try the app without filling in forms.
- **US1b** As a visitor, I can alternatively register with email and password.
- **US2** As a user, I can log in (Google or password) and log out.
- **US3** As a user, I can set my timezone.
- **US4** As a user, I can never see or modify another user's data.

### Habits
- **US5** I can create a habit with a name and the weekdays it applies to.
- **US6** I can edit or archive a habit. Archiving keeps its history.
- **US7** I can see the current streak and best streak of each habit.

### Tasks
- **US8** I can create a task with a name and an optional due date.
- **US9** I can edit, complete, or delete a task.

### Today view
- **US10** I see today's scheduled habits and pending tasks (due today, overdue, or without date).
- **US11** I can mark an item as done and undo it the same day.
- **US11b** I can mark a habit as done for yesterday if I forgot to tick it, so I do not lose my streak or points.

### Reminders
- **US12** I receive a daily reminder email at a time I choose, listing what is pending today.

### Gamification
- **US13** Completing an item earns its points; completing everything scheduled for a day earns a "perfect day" bonus.
- **US13b** When I create a habit or task, I choose its difficulty, which sets how many points it is worth.
- **US14** I can create rewards with a point cost and redeem them when I have enough points.

## Out of scope for the MVP

- Social features (seeing friends' progress, leaderboards).
- Native mobile app.
- Login with providers other than Google (GitHub, Apple...).
- Password reset (planned right after MVP, once email sending exists).
- Habits with targets other than "done / not done" (for example "drink 2 L of water").

## Decisions

- **D1 Registration**: open to anyone. Sign-up with Google is available from day one, plus email/password.
- **D2 Reminder channel**: email.
- **D3 Late completion**: a habit can be marked as done for the previous local day (yesterday only), to avoid losing streaks and points by forgetting to tick it.
- **D4 Points**: each habit/task has its own value, set through a difficulty level (proposal: easy = 5, medium = 10, hard = 20; to be tuned in phase 7).
- **D5 Frontend language**: TypeScript.

## Decided stack

| Layer | Choice |
|---|---|
| API | Python, FastAPI |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Tests | pytest |
| Auth | Email/password + Google sign-in (OAuth 2.0 / OpenID Connect) |
| Frontend | React (Vite) with TypeScript |
| Deploy | Docker on a host reachable over HTTPS |
