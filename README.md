Python Learning & Project Portfolio

# 🗂️ English Flashcard App

### *Master English vocabulary directly from your terminal with ASCII art and streak tracking.*

---

## 🚀 Key Features

* **100% Hand-Coded Logic** – Built purely by hand in Python without any AI generation.
* **Stunning CLI Visuals** – Rendered with `pyfiglet` for giant ASCII words and `rich` for vibrant, colorized menus and statistics tables.
* **Smart Hint System** – Type `help` during a game to reveal a clue showing only the first and last letters of the Turkish translation.
* **Win Streak Tracking** – Tracks your consecutive correct answers. One mistake resets your streak to zero to keep you on your toes!
* **Mistakes Pool Recovery** – Missed words automatically save to a dedicated "Wrong Answers Section" so you can practice them later until perfected.

---

## 📂 Project Structure

```text
flash-card-app-original/
│
├── flashcard.py              # Application entry point and core game loop
├── where.data           # Local vocabulary database file
├── README.md            # Project documentation
└── requirements.txt     # Python external dependencies
```

---

## 📊 Data Format

The application pulls vocabulary randomly from a local text database named `where.data`. Each word pair must follow a strict `english_word:turkish_meaning` format with **no spaces around the colon**:

```text
encounter:rastlamak
handy:kullanışlı
accustomed:alışkın
```

You can customize or expand this file with your own vocabulary lists by following the exact same layout.

---

## 🛠️ Installation & Setup

Get the application up and running on your local machine in just a few steps.

### 1. Clone the Repository
```bash
git clone https://github.com
cd Python-learning-and-projects/flash-card-app-original
```

### 2. Install Dependencies
This project relies on `pyfiglet` and `rich`. Install them cleanly via pip:
```bash
pip install -r requirements.txt
```
*(Alternatively, install them manually: `pip install pyfiglet rich`)*

### 3. Run the App
```bash
python flashcard.py
```

---

## 🎮 How to Play / Usage Guide

1. **Start the Game:** Launching the app initializes a beautiful terminal layout presenting you with a random English word.
2. **Submit Your Answer:** Type the exact Turkish translation and hit `Enter`. 
   * **Correct Answer:** Your **Win Streak** increases!
   * **Incorrect Answer:** Your streak drops to `0`, and the word is sent to your **Mistakes Pool**.
3. **Need a Hint?:** Stalled on a difficult word? Type `help` in the prompt to view the first and last letters of the Turkish meaning.(hints are disabled for translations that are shorter than 4 letters)
4. **Review Mode:** Choose the review option from the main menu to pull exclusively from your **Wrong Answers Section** and clear out your historical mistakes.

---

## 📦 Dependencies

* **Python 3.x**
* **pyfiglet** – Converts text into large, stylistic ASCII art fonts.
* **rich** – Handles colorized logs, crisp bounding boxes, and organized terminal data tables.

PY4E Course Exercises (Dr. Charles Severance)

My solutions and assignments from the *Python for Everybody (PY4E)* curriculum.

Certificate : https://www.py4e.com/tsugi/assertions/ma2c0bdb5db73eac61535b54e7519a28b

* **Core Foundations:** Practice codes covering basic syntax, strings, files, dicts, and tuples.


---

## ⚙️ Adapted & Enhanced Projects

Open-source projects from learning resources that I analyzed, refactored, and improved.

* **Atatürk Statues Map Visualizer:** Bypassed a library rendering bug by writing a custom Python script that serializes coordinate data from `where.data` into a dynamic JavaScript file (`where.js`).
* **Relational Music Tracks Database:** Parses `tracks.csv` and structures a **Many-to-Many (M:M)** relational model in `SQLite` across Artist, Genre, Album, and Track tables.
* **Automated Image Scraper Bot:** Connects to a target URL, parses the HTML structure, and automatically downloads images to a local folder.
* **Domain Counter:** Parses `mbox-short.txt` to extract email domains and logs the counts into an `SQLite` database.
