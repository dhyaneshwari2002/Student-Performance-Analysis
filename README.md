# Student-Performance-Analysis

# 🎓 EduInsight - Student Performance Analytics System

EduInsight is a Python-based data analysis and visualization project built to analyze student academic records stored in a MySQL database. It helps identify performance trends, subject-wise strengths, and provides insightful visualizations for better decision-making in education.

---

## 📌 Features

- 📊 Subject-wise Average Marks Analysis
- 🧑‍🎓 Individual Student Performance Visualization
- 🏅 Top 5 Students Based on Total Marks
- 📈 Correlation Between Subjects (e.g., Physics vs Mathematics)
- 📚 Remark Distribution Charts
- 🎯 Standard-wise Filtering for Targeted Analysis

---

## 🛠 Technologies Used

- *Python 3.x*
- *MySQL* (with PyMySQL for connection)
- *Matplotlib & Seaborn* for data visualization
- *Pandas* for data handling and analysis

---

## 🗃 Database Structure

*Table Name*: Student

| Column Name    | Data Type         | Description                      |
|----------------|-------------------|----------------------------------|
| Student_ID     | INT (Primary Key) | Auto-incremented ID              |
| Student_Name   | VARCHAR(200)      | Name of the student              |
| Physics        | INT               | Marks in Physics                 |
| Chemistry      | INT               | Marks in Chemistry               |
| Mathematics    | INT               | Marks in Mathematics             |
| Standard       | VARCHAR(30)       | Class/Standard (e.g., 10th)      |
| Remark         | VARCHAR(30)       | Performance remark (e.g., Good)  |

---
