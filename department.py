import tkinter as tk
from tkinter import messagebox
import json
import os


def open_department_window():

    # Create department window
    department_window = tk.Toplevel()

    department_window.title("Department Management")
    department_window.geometry("500x500")

    # Find project folder
    project_folder = os.path.dirname(os.path.abspath(__file__))

    # Create data folder
    data_folder = os.path.join(project_folder, "data")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # Department file
    file_path = os.path.join(data_folder, "departments.json")

    # Create JSON file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file)

    # Title
    title = tk.Label(
        department_window,
        text="DEPARTMENT MANAGEMENT",
        font=("Arial", 20, "bold")
    )
    title.pack(pady=20)

    # Department name label
    department_label = tk.Label(
        department_window,
        text="Department Name:",
        font=("Arial", 12)
    )
    department_label.pack()

    # Department input box
    department_entry = tk.Entry(
        department_window,
        font=("Arial", 12),
        width=30
    )
    department_entry.pack(pady=10)

    # Department list
    department_list = tk.Listbox(
        department_window,
        width=40,
        height=10,
        font=("Arial", 12)
    )
    department_list.pack(pady=20)

    # Load departments
    def load_departments():

        department_list.delete(0, tk.END)

        with open(file_path, "r") as file:
            departments = json.load(file)

        for department in departments:
            department_list.insert(tk.END, department)

    # Add department
    def add_department():

        department_name = department_entry.get().strip()

        if department_name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter department name"
            )
            return

        with open(file_path, "r") as file:
            departments = json.load(file)

        if department_name in departments:
            messagebox.showwarning(
                "Warning",
                "Department already exists"
            )
            return

        departments.append(department_name)

        with open(file_path, "w") as file:
            json.dump(departments, file, indent=4)

        department_entry.delete(0, tk.END)

        load_departments()

        messagebox.showinfo(
            "Success",
            "Department added successfully"
        )

    # Add button
    add_button = tk.Button(
        department_window,
        text="Add Department",
        font=("Arial", 12),
        width=20,
        command=add_department
    )
    add_button.pack(pady=10)

    # Load saved departments
    load_departments()