class Employee:
    def __init__(self, employee_id, name, email, department, designation, joining_date):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.designation = designation
        self.joining_date = joining_date

    def __str__(self):
        return (
            f"\nEmployee ID : {self.employee_id}"
            f"\nName        : {self.name}"
            f"\nEmail       : {self.email}"
            f"\nDepartment  : {self.department}"
            f"\nDesignation : {self.designation}"
            f"\nJoining Date: {self.joining_date}"
        )