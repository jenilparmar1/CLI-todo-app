# 📝 Task Tracker CLI

A **Command-Line Interface (CLI)** task management application built in Python, with colored terminal output, time-tracking, and JSON-based storage.

---

## 🚀 Features

- 📌 Add, delete, edit tasks
- 🛠️ Update task status (Pending, In-progress, Done)
- 🔍 Filter tasks by status
- ⏰ View time since task creation and last update
- 🧠 Auto-saves tasks in `tasks.json`
- 🌈 Beautiful CLI with colored output using `colorama`
- 📋 Tabular display using `tabulate`

---

##✅ Dependencies
colorama - For colored terminal output

tabulate - For formatted tables

Python standard libraries: json, os, datetime

---

##📥 Installation

1.Clone the repository (or copy the files):

```bash
git clone <your-repo-url>
cd task-tracker
```

Install dependencies:

```bash
pip install colorama tabulate
```

Run the script:

```bash
python task_tracker.py
```

---

## 💾 Task Data Format (Stored in `tasks.json`)

Each task includes:

```json
{
  "id": 1,
  "task": "Example task",
  "status": "Pending",
  "created at": "18/06/2025, 23:45:22",
  "last updated": "18/06/2025, 23:45:22"
}
```

---
