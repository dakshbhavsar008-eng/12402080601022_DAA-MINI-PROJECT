import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Database connection
conn = sqlite3.connect("resources.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    requirement INTEGER NOT NULL,
    priority INTEGER NOT NULL
)
""")

conn.commit()


# Add project to database
def add_project():
    name = name_entry.get().strip()
    requirement = requirement_entry.get()
    priority = priority_combo.get()

    if not name or not requirement or not priority:
        messagebox.showerror(
            "Error", "Please fill in all fields."
        )
        return

    try:
        requirement = int(requirement)
        priority = int(priority)

        if requirement <= 0:
            messagebox.showerror(
                "Error", "Requirement must be positive."
            )
            return

        cursor.execute("""
            INSERT INTO projects (name, requirement, priority)
            VALUES (?, ?, ?)
        """, (name, requirement, priority))

        conn.commit()

        name_entry.delete(0, tk.END)
        requirement_entry.delete(0, tk.END)
        priority_combo.set("")

        display_projects()

        messagebox.showinfo(
            "Success", "Project added successfully!"
        )

    except ValueError:
        messagebox.showerror(
            "Error", "Enter a valid numerical requirement."
        )


# Display projects
def display_projects():
    for item in project_table.get_children():
        project_table.delete(item)

    cursor.execute(
        "SELECT id, name, requirement, priority FROM projects"
    )

    for project in cursor.fetchall():
        project_table.insert("", tk.END, values=project)


# Optimize resource allocation
def optimize_allocation():
    try:
        total_resources = int(resource_entry.get())

        if total_resources < 0:
            messagebox.showerror(
                "Error", "Resources cannot be negative."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error", "Enter a valid total resource amount."
        )
        return

    cursor.execute("""
        SELECT id, name, requirement, priority
        FROM projects
        ORDER BY priority DESC, id ASC
    """)

    projects = cursor.fetchall()

    if not projects:
        messagebox.showwarning(
            "Warning", "Please add projects first."
        )
        return

    for item in result_table.get_children():
        result_table.delete(item)

    remaining = total_resources
    allocated_total = 0

    for project in projects:
        project_id, name, requirement, priority = project

        # Allocate resources according to priority
        allocated = min(requirement, remaining)

        remaining -= allocated
        allocated_total += allocated

        result_table.insert(
            "",
            tk.END,
            values=(
                name,
                requirement,
                priority,
                allocated,
                requirement - allocated
            )
        )

    summary_label.config(
        text=(
            f"Total Resources: {total_resources}   |   "
            f"Allocated: {allocated_total}   |   "
            f"Remaining: {remaining}"
        )
    )


# Delete selected project
def delete_project():
    selected = project_table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning", "Select a project to delete."
        )
        return

    project_id = project_table.item(
        selected[0], "values"
    )[0]

    cursor.execute(
        "DELETE FROM projects WHERE id = ?",
        (project_id,)
    )

    conn.commit()

    display_projects()

    messagebox.showinfo(
        "Success", "Project deleted successfully!"
    )


# Main window
root = tk.Tk()
root.title("Resource Allocation Optimization System")
root.geometry("950x700")
root.configure(bg="#eef2f7")

# Heading
tk.Label(
    root,
    text="Resource Allocation Optimization System",
    font=("Arial", 20, "bold"),
    bg="#eef2f7",
    fg="#243b67"
).pack(pady=15)


# Project input section
input_frame = tk.LabelFrame(
    root,
    text="Add New Project",
    font=("Arial", 12, "bold"),
    bg="#eef2f7",
    padx=10,
    pady=10
)

input_frame.pack(fill="x", padx=20, pady=5)

tk.Label(
    input_frame, text="Project Name:",
    bg="#eef2f7"
).grid(row=0, column=0, padx=5, pady=8)

name_entry = tk.Entry(input_frame, width=20)
name_entry.grid(row=0, column=1, padx=5)

tk.Label(
    input_frame, text="Resource Requirement:",
    bg="#eef2f7"
).grid(row=0, column=2, padx=5)

requirement_entry = tk.Entry(input_frame, width=12)
requirement_entry.grid(row=0, column=3, padx=5)

tk.Label(
    input_frame, text="Priority (1-5):",
    bg="#eef2f7"
).grid(row=0, column=4, padx=5)

priority_combo = ttk.Combobox(
    input_frame,
    values=["1", "2", "3", "4", "5"],
    width=5,
    state="readonly"
)

priority_combo.grid(row=0, column=5, padx=5)

tk.Button(
    input_frame,
    text="Add Project",
    command=add_project,
    bg="#3156a3",
    fg="white"
).grid(row=1, column=1, pady=10)

tk.Button(
    input_frame,
    text="Delete Selected",
    command=delete_project,
    bg="#c0392b",
    fg="white"
).grid(row=1, column=3, pady=10)


# Project list
tk.Label(
    root,
    text="Project Details",
    font=("Arial", 13, "bold"),
    bg="#eef2f7"
).pack(pady=5)

project_table = ttk.Treeview(
    root,
    columns=("ID", "Name", "Requirement", "Priority"),
    show="headings",
    height=6
)

for col in ("ID", "Name", "Requirement", "Priority"):
    project_table.heading(col, text=col)
    project_table.column(col, anchor="center", width=150)

project_table.pack(fill="x", padx=20, pady=5)


# Resource allocation section
allocation_frame = tk.LabelFrame(
    root,
    text="Resource Optimization",
    font=("Arial", 12, "bold"),
    bg="#eef2f7",
    padx=10,
    pady=10
)

allocation_frame.pack(fill="x", padx=20, pady=10)

tk.Label(
    allocation_frame,
    text="Total Available Resources:",
    bg="#eef2f7"
).grid(row=0, column=0, padx=10, pady=10)

resource_entry = tk.Entry(
    allocation_frame, width=15
)

resource_entry.grid(row=0, column=1, padx=10)

tk.Button(
    allocation_frame,
    text="Optimize Allocation",
    command=optimize_allocation,
    bg="#218838",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=0, column=2, padx=15)


# Allocation results
tk.Label(
    root,
    text="Allocation Results",
    font=("Arial", 13, "bold"),
    bg="#eef2f7"
).pack(pady=5)

result_table = ttk.Treeview(
    root,
    columns=(
        "Name", "Required", "Priority",
        "Allocated", "Unallocated"
    ),
    show="headings",
    height=7
)

headers = {
    "Name": "Project Name",
    "Required": "Required",
    "Priority": "Priority",
    "Allocated": "Allocated",
    "Unallocated": "Unallocated"
}

for col, heading in headers.items():
    result_table.heading(col, text=heading)
    result_table.column(
        col, anchor="center", width=150
    )

result_table.pack(fill="x", padx=20, pady=5)


# Summary
summary_label = tk.Label(
    root,
    text="Enter available resources to begin.",
    font=("Arial", 11, "bold"),
    bg="#eef2f7",
    fg="#243b67"
)

summary_label.pack(pady=15)


# Load existing projects
display_projects()

# Run application
try:
    root.mainloop()
finally:
    conn.close()
