```markdown
# 🚀 StartupScope

A full-stack web application that helps developers, students, and job-seekers discover startups, their tech stacks, hiring patterns, and founder backgrounds — all in one place.


---

## 🧠 Why StartupScope?

The goal of StartupScope is to **make it easier for tech learners and early-career developers** to:

- Explore **what real startups are building**
- Understand **what technologies they're using**
- Discover **who’s hiring and what roles are in demand**
- Follow **founders, companies, and career pages**

> Built with a focus on **intent validation**, **technical direction**, and **startup discovery** — StartupScope is like a radar for India’s startup ecosystem (and beyond).

---

## ⚙️ Tech Stack

| Layer         | Tech Used                   |
|---------------|-----------------------------|
| Frontend      | Nuxt.js (Vue 3, Composition API) |
| Backend       | FastAPI (Python) + SQLAlchemy ORM |
| Database      | SQLite (Dev), PostgreSQL (Planned) |
| API Style     | RESTful with FastAPI Routers |
| Dev Tools     | Docker, Uvicorn, Watchfiles |
| Package Mgmt  | `uv` (Rust-based Python manager) |

---

## ✨ Features

- 🌍 Browse verified tech startups with rich data
- 🧪 Filter by tech stack, country, hiring stage
- 📈 View company stage, valuation, profitability
- 🧑‍💼 Access founder and contact info (premium)
- 📚 Track what stacks are trending in startup hiring
- 📌 "Watch" companies to get hiring updates (coming soon)

---

## 🔐 Premium (Monetization Plan)

StartupScope is built with future monetization in mind:

| Tier       | Features                                                               |
|------------|------------------------------------------------------------------------|
| Free       | Basic company info, public search                                      |
| Premium ₹49/month | Full founder info, tech stacks, valuation, job links             |
| Recruiter  | Insights dashboard, hiring filters, startup watchlist (coming soon)    |
| Sponsored  | Startups can feature themselves to gain visibility                     |

---

## 🧭 Project Structure

```

StartupScope/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── main.py
├── frontend/
│   ├── components/
│   ├── pages/
│   └── nuxt.config.ts

````

---

## 🧪 Setup (Local Dev)

### 🚀 Backend (FastAPI)

```bash
cd backend
uv pip sync requirements.txt  # or use `uv` to manage dependencies
uvicorn app.main:app --reload --port 8001
````

### 🌐 Frontend (Nuxt)

```bash
cd frontend
npm install
npm run dev
```

App runs on:

* Frontend: `http://localhost:3000`
* Backend: `http://localhost:8001`
* Swagger UI: `http://localhost:8001/docs`

---

## 🛣️ Roadmap

* [x] MVP with Nuxt + FastAPI
* [x] Swagger API with full CRUD
* [x] Tech stack + hiring metadata
* [ ] Job board and resume tips
* [ ] Premium company tracking
* [ ] Recruiter dashboard
* [ ] PostgreSQL + CI deployment

---

## 📈 Why I Built This

> I created this platform for students, freshers, and developers who feel overwhelmed deciding what technologies to learn or what startups to follow. StartupScope acts as a **directional guide** — showing what real startups are building, hiring for, and valuing. It's also a space for discovering startup ethos through their founders and tech choices.

---

## 💰 How I Plan to Sustain It

To make the product viable and keep it running:

* I plan to add **premium features** (like startup tracking, analytics, and tech trends)
* Startups will be able to **feature themselves** and share hiring pages
* Later, a **dashboard for recruiters** and **career switchers** can help fund the platform

---

## 🧑‍💻 Author

**Arjun Pathania**
Developer | ML Enthusiast | Building useful things

* LinkedIn: [www.linkedin.com/in/arjun-pathania-6a9998157](www.linkedin.com/in/arjun-pathania-6a9998157)
* GitHub: [github.com/ArjunPathania](https://github.com/ArjunPathania)

---

## ⭐️ Show Your Support

If this helps you or inspires you, consider:

* 🌟 Starring the repo
* 🗣 Sharing it with students or early-career devs
* 🤝 Contributing data, PRs, or job links

---