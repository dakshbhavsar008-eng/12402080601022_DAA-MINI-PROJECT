# 12402080601022_DAA-MINI-PROJECT
# Resource Allocation Optimization System

## 📌 Project Overview

The **Resource Allocation Optimization System** is a desktop-based mini project developed using Python, Tkinter, and SQLite. It is designed to manage multiple projects and allocate limited resources according to their priority and resource requirements.

The application provides a graphical user interface (GUI) where users can add projects, specify their resource requirements, assign priority levels, delete projects, and optimize resource allocation based on the total available resources.

The system follows a **priority-based allocation approach**, giving preference to projects with higher priority. It also displays the allocated and unallocated resources for each project, helping users understand how resources are distributed.

## 🎯 Objectives

- To manage project details efficiently.
- To allocate limited resources according to project priorities.
- To minimize manual effort in resource distribution.
- To track required, allocated, and unallocated resources.
- To store project information permanently using an SQLite database.
- To provide a simple and user-friendly desktop application.

## ✨ Features

### 1. Add New Project
Users can add projects by entering:
- Project Name
- Resource Requirement
- Priority Level (1–5)

The application validates the input before saving project details to the database.

### 2. View Project Details
Displays all saved projects in a table containing:
- Project ID
- Project Name
- Resource Requirement
- Priority

### 3. Delete Selected Project
Allows users to select and delete a project from the project list and database.

### 4. Priority-Based Resource Optimization
The system sorts projects by priority in descending order. Projects with higher priority receive resources first. If resources are insufficient to fulfill a project's complete requirement, the remaining available resources are allocated to that project.

### 5. Allocation Results
Displays the following information for every project:
- Project Name
- Required Resources
- Priority Level
- Allocated Resources
- Unallocated Resources

### 6. Resource Summary
Displays a summary of:
- Total Available Resources
- Total Resources Allocated
- Remaining Resources

### 7. Input Validation
The application handles invalid numerical inputs, missing fields, negative resource availability, and non-positive project requirements.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming logic |
| Tkinter | Desktop graphical user interface |
| ttk (Themed Tkinter Widgets) | Tables and priority selection |
| SQLite | Persistent storage of project details |
| SQL | Database operations such as INSERT, SELECT, and DELETE |

## ⚙️ System Requirements

- Python 3.x
- Visual Studio Code or another Python IDE
- Tkinter (usually included with standard Python installations)
- SQLite3 (included with Python's standard library)

**No external Python packages are required** for the provided code under a standard Python installation that includes Tkinter.

## 🚀 Installation and Execution

### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/downloads/).

During installation on Windows, enable the option to add Python to PATH.

### Step 2: Create the Project File
Create a folder named `Resource-Allocation-Optimization-System` and save your Python code in a file named:

`main.py`

### Step 3: Open the Project
Open the project folder in Visual Studio Code.

### Step 4: Run the Application
Open the terminal in VS Code and execute:

```bash
python main.py
```

If your system uses the Python launcher, you can also try:

```bash
py main.py
```

### Step 5: Use the Application
1. Enter the project name.
2. Enter the required number of resources.
3. Select a priority from 1 to 5.
4. Click **Add Project**.
5. Repeat to add more projects.
6. Enter the total available resources.
7. Click **Optimize Allocation** to view the allocation results.
8. Select a project and click **Delete Selected** to remove it when required.

## 🧠 Resource Allocation Algorithm

The application uses a greedy, priority-based allocation method.

**Algorithm:**
1. Accept the total available resources.
2. Retrieve all projects from the SQLite database.
3. Sort projects by priority in descending order.
4. Process projects in priority order.
5. Allocate the minimum of the project's requirement and the remaining resources.
6. Calculate the unallocated resources for each project.
7. Update the remaining resource count.
8. Display the final allocation table and summary.

**Allocation formula:**

```text
Allocated Resources = min(Project Requirement,
                          Remaining Resources)

Unallocated Resources = Project Requirement
                        - Allocated Resources

Remaining Resources = Previous Remaining Resources
                      - Allocated Resources
```

If two projects have the same priority, the project added earlier is processed first.

## 📊 Example

Suppose the system contains the following projects:

| Project | Required | Priority |
|---|---:|---:|
| Project A | 50 | 5 |
| Project B | 40 | 4 |
| Project C | 30 | 3 |

Total available resources: **100**

| Project | Required | Priority | Allocated | Unallocated |
|---|---:|---:|---:|---:|
| Project A | 50 | 5 | 50 | 0 |
| Project B | 40 | 4 | 40 | 0 |
| Project C | 30 | 3 | 10 | 20 |

**Summary:**
- Total Resources: 100
- Allocated: 100
- Remaining: 0

This example demonstrates how the system distributes limited resources according to project priority.

## 🗄️ Database Structure

The application automatically creates a database named `resources.db` and a table named `projects` if they do not already exist.

| Field | Data Type | Description |
|---|---|---|
| id | INTEGER | Unique project ID and primary key |
| name | TEXT | Name of the project |
| requirement | INTEGER | Number of resources required |
| priority | INTEGER | Project priority from 1 to 5 |

Project records remain stored in the database when the application is closed and reopened.

## 📁 Project Structure

```text
Resource-Allocation-Optimization-System/
│
├── main.py
├── resources.db    # Created automatically
└── README.md
```

The `resources.db` file is generated automatically when the Python application runs. It does not need to be created manually.

## 🔮 Future Enhancements

- Add AI or machine-learning-based resource allocation.
- Introduce user login and administrator access.
- Add project editing and updating functionality.
- Generate allocation reports and graphical charts.
- Support multiple resource types, such as money, staff, and equipment.
- Implement advanced optimization algorithms for complex allocation problems.
- Add export functionality for reports in CSV or PDF format.

## 🎓 Project Purpose

This mini project demonstrates the practical use of Python GUI programming, database management, input validation, greedy algorithms, and resource optimization concepts. It is suitable for academic demonstration and learning purposes.

## 👨‍💻 Author

**Daksh Bhavsar**

## 📄 License

This project is intended for educational and academic purposes.
