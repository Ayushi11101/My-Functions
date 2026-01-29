# Reusable Python Functions for Data Analytics

**Author:** Ayushi Gupta  

This repository contains a collection of **reusable Python utility functions** designed to support common tasks in **data analytics**.  
The functions are written with clarity and simplicity in mind and can be reused across multiple projects.

This repository will continue to grow over time as more reusable functions are added.

---

## 📂 Repository Contents

- `reusable_functions.py`  
  A Python file containing reusable helper functions.

---

## 🛠️ Current Functionality

The functions currently focus on **basic CSV handling and data parsing**, implemented using core Python concepts.

### 1. Parse CSV Headers
```python
parse_header(header_line)
```
- Reads the header line of a CSV file
- Splits column names correctly

### 2. Parse CSV Values
```python
parse_values(data_line)
```
- Converts numeric values to `float`
- Handles missing values safely
- Keeps text values as strings

### 3. Create Dictionary Records
```python
create_item_dict(values, headers)
```
- Combines headers and values
- Returns a dictionary representing one row of data

### 4. Read CSV File
```python
read_csv(path)
```
- Reads a CSV file from disk
- Returns a list of dictionaries (one per row)
- Useful for basic data analysis workflows

### 5. Write CSV File
```python
write_csv(items, path)
```
- Writes a list of dictionaries to a CSV file
- Automatically writes headers
- Handles empty datasets gracefully

---

## 🚀 Usage Example
```python
from reusable_functions import read_csv, write_csv

data = read_csv("input.csv")
write_csv(data, "output.csv")
```

---

## 📌 Future Enhancements
More reusable functions may be added in the future, including but not limited to:
- Data cleaning utilities
- Statistical helper functions
- File handling helpers
- Data transformation functions
- Optional integration with libraries such as `pandas`

---

## 🎯 Purpose of This Repository
- Practice writing clean and reusable Python code
- Build a personal utility library for projects
- Strengthen core Python and data analytics concepts
- Showcase practical Python skills on GitHub

---

## 📫 Contact
Ayushi Gupta
GitHub: https://github.com/Ayushi11101
---
