# IPL Data Engineering Project

## Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline using IPL datasets. Data is extracted from CSV files, cleaned and transformed using Pandas, loaded into MySQL, and analyzed using SQL queries and visualizations.

---

## Tech Stack

- Python
- Pandas
- MySQL
- SQLAlchemy
- PyMySQL
- Matplotlib
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## Project Workflow

CSV Files
↓
Extract
↓
Transform (Cleaning)
↓
Load into MySQL
↓
SQL Analysis
↓
Visualization

---

## Project Architecture

matches.csv + deliveries.csv
            ↓
        Extract
            ↓
       Transform
            ↓
      Cleaned Data
            ↓
         MySQL
            ↓
      SQL Analysis
            ↓
      Visualization

---

## Project Structure

```text
ipl-data-project/
├── data/
├── cleaned_data/
├── notebooks/
├── screenshots/
├── sql/
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── main.py
├── requirements.txt
└── README.md