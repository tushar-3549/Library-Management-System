# 📚 Library Management System

A minimal yet functional **Library Management System** built with **Python**, **SQLite**, and object-oriented design. It allows you to manage books, members, and their borrowing history — ideal for small libraries or learning DB-backed applications.

---

## 🚀 Features

- 📖 Add/search books with author and title
- 👥 Add/view library members
- 📅 Issue and return books with timestamps
- ✅ Auto-handling of book availability status
- 🗃️ Data stored in a local SQLite database
- 🐳 Dockerized for easy deployment

---

## 🛠️ Setup Instructions

### ▶️ Run with Python (Locally)

1. **Clone the repository**
   ```bash
   git clone https://github.com/tushar-3549/Library-Management-System.git
   cd Library-Management-System
   ```
2. **Run the script**
   ```
   python main.py
   ```
All tables are automatically created when the script is run.

### 🐳 Run with Docker
- Build the Docker image
  ```bash
  docker build -t library-app .
  ```
- Run the container
  ```bash
  docker run -it --rm library-app
  ```
### Requirements

- Python 3.7+
- Docker (optional)
- No external dependencies (uses standard library only)
