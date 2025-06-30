# 📘 Developer Diary — `StartupScope`

## 🗓️ Date: 28–29 June 2025

> Documenting issues, debugging steps, and learnings during backend + frontend integration & Docker setup.

---

### ✅ Overview

* **Tech Stack**: FastAPI (backend), Nuxt.js (frontend), Docker, SQLite
* **Goal**: Build a full-stack startup discovery app with company tracking
* **Main Focus**: Fixing backend routing issues, DB errors, Swagger access, Docker errors, and final deployment steps.

---

## 🔧 Backend Issues

### 🐞 1. `ImportError: cannot import name 'CompanyBase'`

* **Cause**: Incorrect or missing import in `app/schemas/__init__.py`
* **Fix**: Verified file structure and ensured `CompanyBase` is imported/exported properly.

---

### 🐞 2. Swagger UI not visible

* **Cause**: Routes not loaded properly in main router or incorrect prefix
* **Fix**: Made sure FastAPI's `docs_url` is set and router is included with correct prefix `/api/v1`

---

### 🐞 3. `/companies` returning 404

* **Cause**: Incorrect endpoint prefix or missing trailing slash
* **Fix**: Verified route registered at `/api/v1/companies/`, used trailing slash

---

### 🐞 4. `sqlite3.OperationalError: no such table: companies`

* **Cause**: Table wasn't being created automatically on app start
* **Fix**:

  * Confirmed correct import of `Company` model to trigger table creation
  * Added `Base.metadata.create_all(engine)` at the correct place in `main.py`

---

### 🐞 5. `sqlite3.ProgrammingError: type 'HttpUrl' is not supported`

* **Cause**: Trying to insert a Pydantic `HttpUrl` directly into the DB
* **Fix**: Cast `HttpUrl` fields to string (`str(pydantic_field)`) before DB insert

---

### 🐞 6. `POST /api/v1/companies/` returning 422 Unprocessable Entity

* **Cause**: Request payload didn't match the expected schema (`CompanyBase`)
* **Fix**: Matched the exact Pydantic model — ensured required fields (like `name`, `stage`, `headquarters_country`) were sent

---

## 🐳 Docker & Compose Issues

### 🐞 7. Docker Compose crash: `KeyError: 'ContainerConfig'`

* **Cause**: Old/buggy Docker Compose v1.29.2
* **Fix**: Upgraded to Docker Compose v2 (`docker compose` instead of `docker-compose`)

---

### 🐞 8. Docker health check

* **Task**: Added basic FastAPI health check using:

  ```yaml
  healthcheck:
    test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
    interval: 30s
    timeout: 10s
    retries: 3
  ```
* **Result**: Health monitoring now possible for backend container

---

### 🐞 9. Database not persisting

* **Cause**: SQLite inside container, not mounted to a volume
* **Fix**: Plan to mount a volume (`./backend/startupscope.db:/app/startupscope.db`) or move to PostgreSQL for prod

---

## 🌐 Frontend Issues (Nuxt)

### 🐞 10. Nuxt 404 on `/`

* **Cause**: No index.vue or catch-all route
* **Fix**: Added a fallback route or index page

---

### 🐞 11. Cannot connect frontend to backend

* **Cause**: CORS misconfigured
* **Fix**: Allowed `http://localhost:3000` in FastAPI's `CORSMiddleware`

---

## 🛠️ Today's Errors (30 June 2025)

### 🐞 12. `uvicorn` not found

* **Cause**: Installed in `.venv`, but shell was not using the right Python environment
* **Fix**: Activated virtual environment and verified with `which python`, corrected system vs venv `pip` usage

### 🐞 13. `fastapi`, `sqlalchemy`, `pydantic` not installing

* **Cause**: `pip` used was system-level instead of the `.venv`'s pip
* **Fix**: Used `uv pip` inside `.venv`, re-aligned environment properly

### 🐞 14. `tailwindcss` CLI not working

* **Cause**: Broken lockfile and partial installs
* **Fix**: Deleted `node_modules`, lock files, reinstalled with correct versions

### 🐞 15. `PermissionError` on `.nuxt/tsconfig.json`

* **Cause**: Previously used `sudo` with npm created root-owned files
* **Fix**: Ran `sudo chown -R $USER ~/.npm ~/.config` to fix ownership

---

## 🔁 Why I'm Switching to Arch Linux

* Ubuntu/Mint created permission hell using `sudo` with npm and Python
* Needed a clean, lightweight, customizable base OS with full control
* Want full speed, performance, and a clean dev environment
* Arch gives full transparency and reproducibility
* Prefer a minimal i3-based window manager with no GPU
* Needed perfect control for C++, Rust, Python, Go, and JS/TS workflows

---

## ✅ Achievements

* Swagger UI working at `/docs`
* Company create/list APIs work
* Nuxt frontend connects to FastAPI backend
* Docker builds completed
* `.gitignore`, `.dockerignore`, and health checks added
* Started monetization and project README planning
