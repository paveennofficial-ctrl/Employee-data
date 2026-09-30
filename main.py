import tkinter as tk
from department import open_department_window
from student import open_student_window
window=tk.Tk()
window.title("STUDENT MANAGEMENT SYSTEM")
window.geometry("800x500")
title=tk.Label(window,text="Student Management System",font=("Arial",24))
title.pack(pady=50)

student_button = tk.Button(window,text="Student Management",command=open_student_window)
student_button.pack(pady=10)
department_button = tk.Button(window,text="Department Management",command=open_department_window)
department_button.pack(pady=10)
exit_button = tk.Button(window, text="Exit",command=window.destroy)
exit_button.pack(pady=10)

window.mainloop()
