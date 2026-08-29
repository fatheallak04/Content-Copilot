# Content Copilot 🤖✍️

> An AI-powered, full-stack content automation system — from raw idea to publish-ready design — built to survive a schedule with zero spare time.

![Status](https://img.shields.io/badge/status-in%20development-yellow)
![Python](https://img.shields.io/badge/backend-Python-blue)
![React](https://img.shields.io/badge/frontend-React-61DAFB)
![AI](https://img.shields.io/badge/AI-Gemini%20API-8E75B2)

---

## Table of Contents
1. [Executive Summary](#1-executive-summary)
2. [Problem Statement](#2-problem-statement)
3. [Project Objectives](#3-project-objectives)
4. [Tech Stack](#4-tech-stack)
5. [System Architecture](#5-system-architecture)
6. [Action Plan / Roadmap](#6-action-plan--roadmap)
7. [Success Metrics](#7-success-metrics)
8. [Security & Reliability Notes](#8-security--reliability-notes)
9. [Future Work](#9-future-work)

---

## 1. Executive Summary

Managing time between a computer engineering & networking degree, leading the student union, and evening cashier shifts makes consistent content creation nearly impossible. **Content Copilot** is a full-stack, AI-driven system that automates content production — from the first raw idea to a publish-ready design — end to end.

The system acts as a personal digital assistant: it collapses hours of manual work into seconds, while also serving as a serious engineering showcase — spanning bot development, AI integration, backend logic, database design, and frontend dashboards.

## 2. Problem Statement

Content ideas are usually captured in fragments — a voice note, a rushed thought between shifts, a line jotted down before a lecture. Without a fast capture-to-output pipeline, these ideas die before they ever become a post. The bottleneck isn't creativity — it's **time and friction**.

## 3. Project Objectives

- **Save time and effort** — turn quick, unstructured ideas into professional content (scripts + designs) within seconds via Telegram messages.
- **Ensure consistency** — build a smart scheduling system that sends automatic reminders to keep a weekly publishing cadence.
- **Demonstrate technical competence** — build a real product that integrates frontend development, databases, and API orchestration, reflecting strong problem-solving and system design skills.

## 4. Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | **React** | Fast, interactive dashboard for content calendar & management |
| Backend | **Python** | Bot logic, request handling, service orchestration |
| Database | **SQL / SQLite** | Stores content plan, ideas, and publishing schedule |
| AI Engine | **Gemini API** | Analyzes ideas, generates scripts/text in a personal tone |
| Visual Automation | **HTML/CSS + html2image (Python)** | Converts generated text into publish-ready carousel images |
| Interface | **Telegram Bot API** | Primary input channel — capture ideas anywhere, instantly |

## 5. System Architecture

```
┌─────────────┐      ┌──────────────┐      ┌───────────────┐
│  Telegram   │─────▶│   Python     │─────▶│   Gemini API   │
│  (input)    │      │   Backend    │◀─────│  (text/script) │
└─────────────┘      │  (bot logic) │      └───────────────┘
                      │      │       │
                      │      ▼       │
                      │  SQL/SQLite  │◀── stores ideas, schedule, history
                      │      │       │
                      │      ▼       │
                      │ HTML/CSS +   │──▶ Carousel images (ready to post)
                      │ html2image   │
                      └──────┬───────┘
                             │
                             ▼
                     ┌───────────────┐
                     │  React         │
                     │  Dashboard     │──▶ calendar view, edit/manage content
                     └───────────────┘
```

*(Diagram in plain-text form for now — a rendered version can be generated with tools like Excalidraw or Mermaid once the repo is public.)*

## 6. Action Plan / Roadmap

- [ ] **Phase 1 — Bot Foundation**
  Set up the repository, configure the Telegram Bot, and connect it to the Gemini API to receive messages and convert them into structured text.

- [ ] **Phase 2 — Automated Design**
  Design HTML/CSS templates and write a Python script to merge generated text into templates, producing carousel-ready images.

- [ ] **Phase 3 — Memory & Reminders**
  Build the SQL database to store content history, and activate periodic reminder scripts via Telegram.

- [ ] **Phase 4 — Dashboard**
  Build the React interface for a full content calendar and management view, connected to the backend as one integrated system.

- [ ] **Phase 5 — Hardening** *(new)*
  Add error handling for API failures/timeouts, input validation, and basic logging so the system degrades gracefully instead of silently failing.

## 7. Success Metrics

- Time to go from raw idea → publish-ready post: target **under 2 minutes** (vs. hours manually).
- Weekly publishing consistency: **at least 90%** adherence to the planned schedule.
- Number of ideas captured vs. ideas actually published (capture-to-output conversion rate).

## 8. Security & Reliability Notes

- Bot tokens and API keys are stored in environment variables (`.env`), **never committed to the repo** — a `.gitignore` entry is mandatory from day one.
- Gemini API calls should have timeout + retry logic; failed generations should queue for retry rather than silently drop.
- SQLite backups should run on a simple schedule (even a cron-triggered copy) to avoid losing the content history.

## 9. Future Work

- Multi-platform publishing (Instagram, LinkedIn, X) directly from the dashboard.
- Basic analytics — which topics/styles get the most engagement, fed back into idea generation.
- Style fine-tuning — let the AI learn from past posts to match personal voice more closely over time.
- Voice-note input support (since ideas are often captured by voice, not text).

---

*This document is the single source of truth for the Content Copilot project and will be kept in sync with development. It also serves as the project's GitHub README.*
