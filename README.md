# Employee Management Console Application

## Overview

The Employee Management Console Application is a Python-based console application that allows users to manage employee records efficiently. It provides basic CRUD (Create, Read, Update, Delete) operations along with input validation, sorting, and filtering features.

## Features

- Add Employee
- View All Employees
- Search Employee by ID
- Update Employee Details
- Delete Employee
- Sort Employees by Name
- Filter Employees by Department
- Prevent Duplicate Employee IDs
- Validate Employee Email Address
- Validate Empty Employee ID and Name
- User-friendly Console Menu

---

## Employee Details

Each employee contains the following information:

- Employee ID
- Name
- Email
- Department
- Designation
- Joining Date

---

## Project Structure

```
EmployeeManagement/
│
├── employee.py
├── employee_service.py
├── main.py
└── README.md
```

---

## Technologies Used

- Python 3.x
- Object-Oriented Programming (OOP)
- Regular Expressions (Regex)

---

## How to Run the Application

### Step 1

Clone or download the project.

### Step 2

Open the project folder in Visual Studio Code.

### Step 3

Open the terminal.

### Step 4

Run the following command:

```bash
python main.py
```

If Python is installed as `py`, run:

```bash
py main.py
```

## Application Menu
Employee Management System

1. Add Employee
2. View All Employees
3. Search Employee by ID
4. Update Employee
5. Delete Employee
6. Sort by Name
7. Filter by Department
8. Exit

## Validations Implemented

- Employee ID cannot be empty.
- Employee Name cannot be empty.
- Employee Email must be in a valid format.
- Duplicate Employee IDs are not allowed.

## Future Improvements

- Save employee data to a JSON file or database
- Unit testing
- Date validation
- Search by employee name
- Export employee records
