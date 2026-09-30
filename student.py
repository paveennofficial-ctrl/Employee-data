import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


def open_student_window():


    student_window = tk.Toplevel()
    student_window.title("Student Management")
    student_window.geometry("900x700")

    

    project_folder = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(project_folder, "Data")

    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    file_path = os.path.join(data_folder, "student.json")

    # Create JSON file if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump([], file, indent=4)

    

    title = tk.Label(
        student_window,
        text="STUDENT MANAGEMENT",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    

    form_frame = tk.Frame(student_window)
    form_frame.pack(pady=10)

    
    tk.Label(
        form_frame,
        text="Student ID",
        font=("Arial", 12)
    ).grid(row=0, column=0, padx=10, pady=8, sticky="w")

    id_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    id_entry.grid(row=0, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Student Name",
        font=("Arial", 12)
    ).grid(row=1, column=0, padx=10, pady=8, sticky="w")

    name_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    name_entry.grid(row=1, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Gender",
        font=("Arial", 12)
    ).grid(row=2, column=0, padx=10, pady=8, sticky="w")

    gender_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    gender_entry.grid(row=2, column=1, padx=10, pady=8)

    tk.Label(
        form_frame,
        text="Department",
        font=("Arial", 12)
    ).grid(row=3, column=0, padx=10, pady=8, sticky="w")

    department_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    department_entry.grid(row=3, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Year",
        font=("Arial", 12)
    ).grid(row=4, column=0, padx=10, pady=8, sticky="w")

    year_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    year_entry.grid(row=4, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Semester",
        font=("Arial", 12)
    ).grid(row=5, column=0, padx=10, pady=8, sticky="w")

    semester_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    semester_entry.grid(row=5, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Phone",
        font=("Arial", 12)
    ).grid(row=6, column=0, padx=10, pady=8, sticky="w")

    phone_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    phone_entry.grid(row=6, column=1, padx=10, pady=8)

    
    tk.Label(
        form_frame,
        text="Email",
        font=("Arial", 12)
    ).grid(row=7, column=0, padx=10, pady=8, sticky="w")

    email_entry = tk.Entry(
        form_frame,
        width=35,
        font=("Arial", 12)
    )
    email_entry.grid(row=7, column=1, padx=10, pady=8)

    

    def add_student():

        student_id = id_entry.get().strip()
        name = name_entry.get().strip()
        gender = gender_entry.get().strip()
        department = department_entry.get().strip()
        year = year_entry.get().strip()
        semester = semester_entry.get().strip()
        phone = phone_entry.get().strip()
        email = email_entry.get().strip()

        
        if (
            student_id == "" or
            name == "" or
            gender == "" or
            department == "" or
            year == "" or
            semester == "" or
            phone == "" or
            email == ""
        ):
            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )
            return

        # Load existing students
        try:
            with open(file_path, "r") as file:
                students = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            students = []

        
        for student in students:

            if str(student["student_id"]) == student_id:

                messagebox.showerror(
                    "Error",
                    "Student ID already exists."
                )
                return

        
        new_student = {
            "student_id": student_id,
            "name": name,
            "gender": gender,
            "department": department,
            "year": year,
            "semester": semester,
            "phone": phone,
            "email": email
        }

        students.append(new_student)

        
        with open(file_path, "w") as file:
            json.dump(students, file, indent=4)

        messagebox.showinfo(
            "Success",
            "Student added successfully."
        )

        # Clear fields
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        year_entry.delete(0, tk.END)
        semester_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

    

    def view_students():

        view_window = tk.Toplevel(student_window)
        view_window.title("View Students")
        view_window.geometry("1100x600")

        title = tk.Label(
            view_window,
            text="ALL STUDENTS",
            font=("Arial", 20, "bold")
        )
        title.pack(pady=15)

        

        search_frame = tk.Frame(view_window)
        search_frame.pack(pady=5)

        tk.Label(
            search_frame,
            text="Search:",
            font=("Arial", 12)
        ).pack(side="left", padx=5)

        search_entry = tk.Entry(
            search_frame,
            width=35,
            font=("Arial", 12)
        )
        search_entry.pack(side="left", padx=5)

        

        table_frame = tk.Frame(view_window)
        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "ID",
            "Name",
            "Gender",
            "Department",
            "Year",
            "Semester",
            "Phone",
            "Email"
        )

        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        for column in columns:

            table.heading(
                column,
                text=column
            )

            table.column(
                column,
                width=120
            )

        # Scrollbars

        vertical_scroll = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=table.yview
        )

        horizontal_scroll = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=table.xview
        )

        table.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        table.pack(
            side="left",
            fill="both",
            expand=True
        )

        vertical_scroll.pack(
            side="right",
            fill="y"
        )

        horizontal_scroll.pack(
            side="bottom",
            fill="x"
        )

        

        def load_students():

            # Clear table
            for item in table.get_children():
                table.delete(item)

            try:

                with open(file_path, "r") as file:
                    students = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):

                students = []

            search_text = search_entry.get().strip().lower()

            for student in students:

                # Search in ID and Name
                if (
                    search_text == "" or
                    search_text in str(student["student_id"]).lower() or
                    search_text in student["name"].lower()
                ):

                    values = (
                        str(student["student_id"]),
                        student["name"],
                        student["gender"],
                        student["department"],
                        str(student["year"]),
                        str(student["semester"]),
                        str(student["phone"]),
                        student["email"]
                    )

                    table.insert(
                        "",
                        "end",
                        values=values
                    )

        

        def search_students():

            load_students()

        search_button = tk.Button(
            search_frame,
            text="Search",
            width=10,
            command=search_students
        )
        search_button.pack(side="left", padx=5)

        clear_button = tk.Button(
            search_frame,
            text="Clear",
            width=10,
            command=lambda: [
                search_entry.delete(0, tk.END),
                load_students()
            ]
        )
        clear_button.pack(side="left", padx=5)

        # Load data when window opens
        load_students()



    def edit_student():

        edit_window = tk.Toplevel(student_window)
        edit_window.title("Edit Student")
        edit_window.geometry("500x650")

        tk.Label(
            edit_window,
            text="EDIT STUDENT",
            font=("Arial", 20, "bold")
        ).pack(pady=20)

        
        tk.Label(
            edit_window,
            text="Student ID",
            font=("Arial", 12)
        ).pack(pady=5)

        edit_id_entry = tk.Entry(
            edit_window,
            width=35,
            font=("Arial", 12)
        )
        edit_id_entry.pack(pady=5)

        
        tk.Label(
            edit_window,
            text="Student Name"
        ).pack(pady=3)

        edit_name_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_name_entry.pack(pady=3)

        # Gender
        tk.Label(
            edit_window,
            text="Gender"
        ).pack(pady=3)

        edit_gender_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_gender_entry.pack(pady=3)

        # Department
        tk.Label(
            edit_window,
            text="Department"
        ).pack(pady=3)

        edit_department_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_department_entry.pack(pady=3)

        # Year
        tk.Label(
            edit_window,
            text="Year"
        ).pack(pady=3)

        edit_year_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_year_entry.pack(pady=3)

        # Semester
        tk.Label(
            edit_window,
            text="Semester"
        ).pack(pady=3)

        edit_semester_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_semester_entry.pack(pady=3)

        # Phone
        tk.Label(
            edit_window,
            text="Phone"
        ).pack(pady=3)

        edit_phone_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_phone_entry.pack(pady=3)

        # Email
        tk.Label(
            edit_window,
            text="Email"
        ).pack(pady=3)

        edit_email_entry = tk.Entry(
            edit_window,
            width=35
        )
        edit_email_entry.pack(pady=3)



        def find_student():

            student_id = edit_id_entry.get().strip()

            if student_id == "":
                messagebox.showwarning(
                    "Warning",
                    "Enter Student ID."
                )
                return

            try:

                with open(file_path, "r") as file:
                    students = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):

                students = []

            for student in students:

                if str(student["student_id"]) == student_id:

                    edit_name_entry.delete(0, tk.END)
                    edit_name_entry.insert(
                        0,
                        student["name"]
                    )

                    edit_gender_entry.delete(0, tk.END)
                    edit_gender_entry.insert(
                        0,
                        student["gender"]
                    )

                    edit_department_entry.delete(0, tk.END)
                    edit_department_entry.insert(
                        0,
                        student["department"]
                    )

                    edit_year_entry.delete(0, tk.END)
                    edit_year_entry.insert(
                        0,
                        student["year"]
                    )

                    edit_semester_entry.delete(0, tk.END)
                    edit_semester_entry.insert(
                        0,
                        student["semester"]
                    )

                    edit_phone_entry.delete(0, tk.END)
                    edit_phone_entry.insert(
                        0,
                        student["phone"]
                    )

                    edit_email_entry.delete(0, tk.END)
                    edit_email_entry.insert(
                        0,
                        student["email"]
                    )

                    return

            messagebox.showerror(
                "Error",
                "Student not found."
            )

        

        def update_student():

            student_id = edit_id_entry.get().strip()

            if student_id == "":
                messagebox.showwarning(
                    "Warning",
                    "Enter Student ID."
                )
                return

            try:

                with open(file_path, "r") as file:
                    students = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):

                students = []

            found = False

            for student in students:

                if str(student["student_id"]) == student_id:

                    student["name"] = edit_name_entry.get().strip()
                    student["gender"] = edit_gender_entry.get().strip()
                    student["department"] = edit_department_entry.get().strip()
                    student["year"] = edit_year_entry.get().strip()
                    student["semester"] = edit_semester_entry.get().strip()
                    student["phone"] = edit_phone_entry.get().strip()
                    student["email"] = edit_email_entry.get().strip()

                    found = True
                    break

            if not found:

                messagebox.showerror(
                    "Error",
                    "Student not found."
                )
                return

            # Save updated data
            with open(file_path, "w") as file:
                json.dump(students, file, indent=4)

            messagebox.showinfo(
                "Success",
                "Student updated successfully."
            )

            edit_window.destroy()

        tk.Button(
            edit_window,
            text="Find Student",
            width=20,
            command=find_student
        ).pack(pady=10)

        tk.Button(
            edit_window,
            text="Update Student",
            width=20,
            command=update_student
        ).pack(pady=5)

    

    def delete_student():

        delete_window = tk.Toplevel(student_window)
        delete_window.title("Delete Student")
        delete_window.geometry("400x250")

        tk.Label(
            delete_window,
            text="DELETE STUDENT",
            font=("Arial", 20, "bold")
        ).pack(pady=25)

        tk.Label(
            delete_window,
            text="Enter Student ID",
            font=("Arial", 12)
        ).pack(pady=5)

        delete_id_entry = tk.Entry(
            delete_window,
            width=30,
            font=("Arial", 12)
        )
        delete_id_entry.pack(pady=10)

    

        def delete():

            student_id = delete_id_entry.get().strip()

            if student_id == "":
                messagebox.showwarning(
                    "Warning",
                    "Enter Student ID."
                )
                return

            try:

                with open(file_path, "r") as file:
                    students = json.load(file)

            except (FileNotFoundError, json.JSONDecodeError):

                students = []

            new_students = []
            found = False

            for student in students:

                if str(student["student_id"]) == student_id:

                    found = True

                else:

                    new_students.append(student)

            if not found:

                messagebox.showerror(
                    "Error",
                    "Student not found."
                )
                return

            confirm = messagebox.askyesno(
                "Confirm Delete",
                "Are you sure you want to delete this student?"
            )

            if not confirm:
                return

            with open(file_path, "w") as file:
                json.dump(new_students, file, indent=4)

            messagebox.showinfo(
                "Success",
                "Student deleted successfully."
            )

            delete_window.destroy()

        tk.Button(
            delete_window,
            text="Delete Student",
            width=20,
            command=delete
        ).pack(pady=15)


    button_frame = tk.Frame(student_window)
    button_frame.pack(pady=20)

    add_button = tk.Button(
        button_frame,
        text="ADD STUDENT",
        width=18,
        height=2,
        command=add_student
    )
    add_button.grid(row=0, column=0, padx=8, pady=8)

    view_button = tk.Button(
        button_frame,
        text="VIEW STUDENTS",
        width=18,
        height=2,
        command=view_students
    )
    view_button.grid(row=0, column=1, padx=8, pady=8)

    edit_button = tk.Button(
        button_frame,
        text="EDIT STUDENT",
        width=18,
        height=2,
        command=edit_student
    )
    edit_button.grid(row=1, column=0, padx=8, pady=8)

    delete_button = tk.Button(
        button_frame,
        text="DELETE STUDENT",
        width=18,
        height=2,
        command=delete_student
    )
    delete_button.grid(row=1, column=1, padx=8, pady=8)

    search_button_main = tk.Button(
        button_frame,
        text="SEARCH STUDENT",
        width=18,
        height=2,
        command=view_students
    )
    search_button_main.grid(row=2, column=0, columnspan=2, padx=8, pady=8)