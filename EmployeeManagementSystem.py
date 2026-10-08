# 17th gthub Project --> Employee Management System
print('----------Employee Management System----------')
employees = {}


def add_employee():
    emp_id = input("Enter Employee ID: ").strip()

    if emp_id == "":
        print("❌ ID cannot be empty!\n")
        return

    if emp_id in employees:
        print("❌ Employee ID already exists!\n")
        return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    salary = input("Enter Salary: ").strip()

    if name == "" or department == "" or salary == "":
        print("❌ All fields are required!\n")
        return

    employees[emp_id] = {
        "name": name,
        "department": department,
        "salary": salary
    }

    print(f"✅ Employee '{name}' added successfully!\n")


def view_all_employees():
    if not employees:
        print("\n📭 No employees found.\n")
        return

    print("\n" + "=" * 65)
    print(f"{'ID':<10}{'Name':<20}{'Department':<20}{'Salary':<15}")
    print("=" * 65)

    for emp_id in employees:
        info = employees[emp_id]
        print(f"{emp_id:<10}{info['name']:<20}{info['department']:<20}{info['salary']:<15}")

    print("=" * 65 + "\n")


def search_employee():
    if not employees:
        print("📭 No employees to search.\n")
        return

    query = input("Enter Employee ID or Name to search: ").strip().lower()
    found = False

    for emp_id in employees:
        info = employees[emp_id]
        if query == emp_id.lower() or query in info["name"].lower():
            print(f"\n🔍 Found → ID: {emp_id} | Name: {info['name']} | "
                  f"Dept: {info['department']} | Salary: {info['salary']}")
            found = True

    if not found:
        print("❌ No matching employee found.\n")
    else:
        print()


def update_employee():
    if not employees:
        print("📭 No employees to update.\n")
        return

    emp_id = input("Enter Employee ID to update: ").strip()

    if emp_id not in employees:
        print("❌ Employee not found!\n")
        return

    print("(Press Enter to keep the current value)")

    name = input(f"New Name [{employees[emp_id]['name']}]: ").strip()
    department = input(f"New Department [{employees[emp_id]['department']}]: ").strip()
    salary = input(f"New Salary [{employees[emp_id]['salary']}]: ").strip()

    if name != "":
        employees[emp_id]["name"] = name
    if department != "":
        employees[emp_id]["department"] = department
    if salary != "":
        employees[emp_id]["salary"] = salary

    print("✅ Employee updated successfully!\n")


def delete_employee():
    if not employees:
        print("📭 No employees to delete.\n")
        return

    emp_id = input("Enter Employee ID to delete: ").strip()

    if emp_id not in employees:
        print("❌ Employee not found!\n")
        return

    confirm = input(f"Are you sure you want to delete "
                    f"{employees[emp_id]['name']}? (y/n): ").strip().lower()

    if confirm == "y":
        del employees[emp_id]
        print("🗑️ Employee deleted successfully!\n")
    else:
        print("❌ Deletion cancelled.\n")


def count_employees():
    print(f"\n📊 Total Employees: {len(employees)}\n")


def main():
    while True:
        print("===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Count Employees")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_all_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            count_employees()
        elif choice == "7":
            print("\n👋 Goodbye!\n")
            break
        else:
            print("❌ Invalid choice. Please enter 1-7.\n")


main()