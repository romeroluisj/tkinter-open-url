# Workflow Reminders

## Personal Reminders for Working with Windsurf AI Assistant

These are reminders to always direct the AI assistant to read PLANNING.md and TASK.md in every prompt.

## 1. 🔑 Golden Rules
These are the high-level principles that guide how to work with AI tools efficiently and effectively. We'll be implementing these through global rules and our prompting throughout the process:

- Use markdown files to manage the project (README.md, PLANNING.md, TASK.md).
- Keep files under 500 lines. Split into modules when needed.
- Start fresh conversations often. Long threads degrade response quality.
- Don't overload the model. One task per message is ideal.
- Test early, test often. Every new function should have unit tests.
- Be specific in your requests. The more context, the better. Examples help a lot.
- Write docs and comments as you go. Don't delay documentation.
- Implement environment variables yourself. Don't trust the LLM with API keys.

## 2. 🧠 Planning & Task Management

Before writing any code, it’s important to have a conversation with the LLM to plan the initial scope and tasks for the project. 

Scope goes into PLANNING.md, and specific tasks go into TASK.md. 

These should be updated by the AI coding assistant as the project progresses.

### PLANNING.md
**Purpose:** High-level vision, architecture, constraints, tech stack, tools, etc.
**Prompt to AI:** "Use the structure and decisions outlined in PLANNING.md."
**Note:** Have the LLM reference this file at the beginning of any new conversation.

### TASK.md
**Purpose:** Tracks current tasks, backlog, and sub-tasks.
**Includes:** Bullet list of active work, milestones, and anything discovered mid-process.
**Prompt to AI:** "Update TASK.md to mark XYZ as done and add ABC as a new task."
**Note:** Can prompt the LLM to automatically update and create tasks as well (through global rules).

---

## Quick Start Phrase
For new conversations, use: **"Please read PLANNING.md first"**

This will activate both project context and AI assistant rules automatically.
