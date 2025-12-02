Absolutely — here is a **clean, simple, and complete cheat-sheet** for setting up and running your **Patient-Tracker-System** on any machine.

---

# 🧪 Patient-Tracker-System — Setup Cheat Sheet

*(Works on Windows, Linux, macOS — tailored for your Windows setup)*

---

## ✅ 1. **Install Required Software**

### ✔ Python 3.11 (recommended for compatibility)

Download:
🔗 [https://www.python.org/downloads/release/python-311/](https://www.python.org/downloads/release/python-311/)

During installation → **check**:
☑ *Add Python 3.11 to PATH*

---

## ✅ 2. **Get the Project**

Place the project folder somewhere clean, e.g.:

```
C:\Users\Jai Talreja\Downloads\Patient-Tracker-System\Patient-Tracker-System
```

---

## ✅ 3. **Create a Virtual Environment**

Open CMD inside the project folder:

```bash
cd "C:\Users\Jai Talreja\Downloads\Patient-Tracker-System\Patient-Tracker-System"
```

Then:

```bash
py -3.11 -m venv venv
```

---

## ✅ 4. **Activate the Virtual Environment**

### Windows:

```bash
venv\Scripts\activate
```

### Linux/macOS:

```bash
source venv/bin/activate
```

You should now see:

```
(venv)
```

---

## ✅ 5. **Upgrade pip (optional but recommended)**

```bash
python -m pip install --upgrade pip setuptools wheel
```

---

## ✅ 6. **Install all project dependencies**

```bash
pip install -r requirements.txt
```

This installs:

* Flask
* SQLAlchemy
* Flask-SQLAlchemy
* psycopg2-binary
* dotenv
* bcrypt
* etc.

---

## ✅ 7. **Run the Server**

Inside the venv run:

```bash
python server.py
```

If successful, you’ll see:

```
Running on http://127.0.0.1:5001
Debugger is active!
```

Open your browser →
👉 [http://127.0.0.1:5001](http://127.0.0.1:5001)

---

## ✅ 8. **Stopping the Server**

Press:

```
CTRL + C
```

---

## ✅ 9. **Common Issues & Fixes**

### 🔥 Issue: `ModuleNotFoundError: No module named 'flask'`

Cause: Wrong directory / wrong venv
Fix:

```bash
cd <project-folder>
venv\Scripts\activate
```

### 🔥 Issue: Missing static files (404 on CSS/JS)

Create structure:

```
static/core/css/styles.css
static/core/js/scripts.js
```

(or restore from original repo)

### 🔥 Issue: Wrong Python version

Use Python 3.11:

```bash
py -3.11 -m venv venv
```

---

## 🎯 OPTIONAL (Highly Useful)

### ⭐ Create a shortcut to run server quickly

Create `run_server.bat` inside project folder:

```bat
@echo off
call venv\Scripts\activate
python server.py
pause
```

Double-click → server starts automatically.

---

### ⭐ To deactivate the environment

```bash
deactivate
```

---

### ⭐ To check installed Python versions

```bash
py --list
```

---

# ✅ You're All Set

If you want, I can also generate a **README.md** file for the project containing this cheat sheet, so it stays inside your repo permanently.

