# 📝 Simple Blog Database (CLI)

A simple **command-line blog database** built in Python.  
This project allows users to create, view, and search blog posts stored in a text file (`BD.txt`).  
It uses **Colorama** for colored terminal output and provides a clean, interactive CLI experience.

---

## ✨ Features

- **Add New Blog**  
  - Enter title, author, co-author, and multiline blog content.  
  - Auto-generates index and date for each post.  

- **View All Posts**  
  - Displays all blogs with formatted colors for readability.  

- **Search Blogs**  
  - Search by **Author**  
  - Search by **Co-Author**  
  - Search by **Date**  

- **File Handling**  
  - Automatically creates `BD.txt` if missing.  
  - Shows disclaimer and countdown before redirecting to menu.  

- **Exit Flow**  
  - Graceful exit with countdown timer.  

---

## ⚙️ Requirements

- Python 3.x
- Libraries:
  - `colorama`
  - `datetime` (built-in)
  - `os` (built-in)
  - `re` (built-in)
  - `time` (built-in)

Install dependencies:

```bash
pip install colorama