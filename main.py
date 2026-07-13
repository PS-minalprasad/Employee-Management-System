from employee import Employee
from employee_service import EmployeeService


def main():
    service = EmployeeService()

    while True:
        print("\n" + "=" * 40)
        print(" Employee Management System")
        print("=" * 40)
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee by ID")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Sort by Name")
        print("7. Filter by Department")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            employee_id = input("Employee ID: ")
            name = input("Name: ")
            email = input("Email: ")
            department = input("Department: ")
            designation = input("Designation: ")
            joining_date = input("Joining Date: ")

            employee = Employee(
                employee_id,
                name,
                email,
                department,
                designation,
                joining_date
            )

            service.add_employee(employee)

        elif choice == "2":
            service.view_employees()

        elif choice == "3":
            employee_id = input("Enter Employee ID: ")
            service.search_employee(employee_id)

        elif choice == "4":
            employee_id = input("Enter Employee ID: ")
            service.update_employee(employee_id)

        elif choice == "5":
            employee_id = input("Enter Employee ID: ")
            service.delete_employee(employee_id)

        elif choice == "6":
            service.sort_by_name()

        elif choice == "7":
            department = input("Enter Department: ")
            service.filter_by_department(department)

        elif choice == "8":
            print("Thank you for using Employee Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()