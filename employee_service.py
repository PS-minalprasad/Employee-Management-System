import re

class EmployeeService:
    def __init__(self):
        self.employees = []

    def is_valid_email(self, email):
        """Validate email format."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))

    def get_employee_by_id(self, employee_id):
        """Return employee object if ID exists."""
        for employee in self.employees:
            if employee.employee_id == employee_id:
                return employee
        return None

    def add_employee(self, employee):
        """Add a new employee."""

        if not employee.employee_id.strip():
            print("Employee ID cannot be empty.")
            return

        if self.get_employee_by_id(employee.employee_id):
            print("Employee ID already exists.")
            return

        if not employee.name.strip():
            print("Employee name cannot be empty.")
            return

        if not self.is_valid_email(employee.email):
            print("Invalid email address.")
            return

        self.employees.append(employee)
        print("\nEmployee added successfully.")

    def view_employees(self):
        """Display all employees."""

        if not self.employees:
            print("\nNo employees found.")
            return

        print("\n========== Employee List ==========")

        for employee in self.employees:
            print(employee)
            print("-" * 40)

    def search_employee(self, employee_id):
        """Search employee by ID."""

        employee = self.get_employee_by_id(employee_id)

        if employee:
            print("\nEmployee Found")
            print(employee)
        else:
            print("\nEmployee not found.")

    def update_employee(self, employee_id):
        """Update employee details."""

        employee = self.get_employee_by_id(employee_id)

        if not employee:
            print("\nEmployee not found.")
            return

        print("\nLeave blank to keep existing value.")

        name = input(f"Name ({employee.name}): ").strip()
        email = input(f"Email ({employee.email}): ").strip()
        department = input(f"Department ({employee.department}): ").strip()
        designation = input(f"Designation ({employee.designation}): ").strip()
        joining_date = input(f"Joining Date ({employee.joining_date}): ").strip()

        if name:
            employee.name = name

        if email:
            if self.is_valid_email(email):
                employee.email = email
            else:
                print("Invalid email. Email not updated.")

        if department:
            employee.department = department

        if designation:
            employee.designation = designation

        if joining_date:
            employee.joining_date = joining_date

        print("\nEmployee updated successfully.")

    def delete_employee(self, employee_id):
        """Delete employee."""

        employee = self.get_employee_by_id(employee_id)

        if employee:
            self.employees.remove(employee)
            print("\nEmployee deleted successfully.")
        else:
            print("\nEmployee not found.")

    def sort_by_name(self):
        """Display employees sorted by name."""

        if not self.employees:
            print("\nNo employees found.")
            return

        sorted_employees = sorted(
            self.employees,
            key=lambda emp: emp.name.lower()
        )

        print("\n====== Employees Sorted by Name ======")

        for employee in sorted_employees:
            print(employee)
            print("-" * 40)

    def filter_by_department(self, department):
        """Display employees from a department."""

        filtered = [
            employee
            for employee in self.employees
            if employee.department.lower() == department.lower()
        ]

        if not filtered:
            print("\nNo employees found in this department.")
            return

        print(f"\n====== {department} Department ======")

        for employee in filtered:
            print(employee)
            print("-" * 40)