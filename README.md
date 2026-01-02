![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-green)
![License](https://img.shields.io/badge/License-MIT-yellow)






# 📝 Simple Blog Database (CLI)

A simple **command-line blog database** built in Python.  
This project allows users to create, view, and search blog posts stored in a text file (`BD.txt`).  
It uses **Colorama** for colored terminal output and provides a clean, interactive CLI experience.

---

## 📦 Download Executable

You can download the latest `.exe` build from the [Releases page](https://github.com/Rajdeb-Gorai/CLI-Based-Local-Blog-Database/releases).

- **Windows users**: Download `blog_database.exe` and run it directly.
- No need to install Python or dependencies.
---

## ⚡ Quick Start (Windows Executable)
1. Create a new folder (e.g., `BlogDB`).
2. Place `blog_database.exe` inside that folder.
3. Run `blog_database.exe`.
4. A `BD.txt` file will be generated in the same folder to store your blogs.
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