# 🧩 Nesting Tool

A tool to optimize cutting of metal profiles from an Excel file, using a *greedy* algorithm to calculate raw material needed for a project.

---

## 📌 Description

This project allows you to:

* Read a list of parts from Excel
* Read available profiles (materials)
* Group parts by profile
* Execute a nesting (cutting) algorithm
* Generate a new Excel file with:

  * Cutting details (`Nesting_detail`)
  * Material usage summary (`Nesting_summary`)

It includes a simple graphical user interface for non-technical users.

---

## 🏗️ Project Structure

```
src/
│
├── core_al/
│   └── nesting.py          # Cutting algorithm logic
│
├── data_io/
│   └── xls_reader.py       # Excel data reader
│
├── models/
│   ├── Parts.py            # Part model
│   └── Profiles.py         # Profile model
│
├── ui/
│   └── nesting_ui.py       # UI + pipeline
│
└── main.py                 # Entry point
```

---

## ▶️ How to Run

### Inside profile_nesting folder:

```bash
py -m src.main
```

---

## 📥 Excel Format

### Sheet: `Parts`

| item | length | qty | profile |
| ---- | ------ | --- | ------- |
| 1    | 48.50  | 2   | PTR 2x2 |

---

### Sheet: `Materials`

| name    | length |
| ------- | ------ |
| PTR 2x2 | 120    |

---

## ⚙️ Program Flow

1. File selection (UI)
2. Data reading (`xls_reader.py`)
3. Conversion to objects (`Part`, `Profile`)
4. Grouping parts by profile
5. Expanding by quantity (`qty`)
6. Running nesting algorithm
7. Generating results
8. Exporting to Excel

---

## 🧠 Nesting Algorithm

The implemented algorithm follows a **greedy (First Fit Decreasing)** approach:

1. Sort parts from largest to smallest
2. Try to place each part in the first available bar
3. If it doesn't fit, create a new bar

📌 Main functions:

* `nesting_parts()` → orchestrates the process
* `group_parts()` → groups and expands parts by quantity
* `nesting()` → assigns parts to bars

---

## 📊 Output

### Sheet: `Nesting_detail`

| profile |     pieces    | used | waste |
| ------- | ------------- | ---- | ----- |
| PTR 2x2 | 48.50 | 48.50 |  97  |  23   |

---

### Sheet: `Nesting_summary`

| profile | total_bars | total_used | total_waste | utilization_% |
| PTR 2x2 |     1      |     97     |     23      |     80.83     |

---

## 🧱 Models

### `Part`

Represents a single part.

Attributes:

* `item`
* `length`
* `qty`
* `profile`

Methods:

* `from_row()` → creates instance from pandas row
* `clone()` → duplicates the part with qty = 1 so you have a different instance for every part

---

### `Profile`

Represents an available material.

Attributes:

* `name`
* `length`

Methods:

* `from_row()`

---

## 📂 Modules

### `xls_reader.py`

* Reads Excel data
* Cleans null values
* Casts data types
* Returns lists of objects

---

### `nesting.py`

Core logic:

* Groups parts
* Expands by quantity
* Executes nesting algorithm

---

### `nesting_ui.py`

* Tkinter-based GUI
* File handling
* Executes full pipeline
* Exports results to Excel

---

## 👤 Author

[Erick Melchor](https://github.com/melchor16)

---

## 🛠️ Technologies

* Python
* Pandas
* OpenPyXL
* Tkinter
