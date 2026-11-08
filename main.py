import json
import hashlib
import secrets
import hmac
from modules.analytics import reports_and_analytics
from modules.rewards import (
    calculate_student_rewards,
    calculate_student_badges,
    view_my_rewards,
    save_student_rewards,
    calculate_student_level
)
from modules.user_management import (
    create_account,
    student_login,
    student_profile,
    reset_password
)
from modules.event_management import (
    create_event,
    manage_events,
    view_events,
    edit_event,
    delete_event
)
from modules.ticket_management import view_my_tickets
from modules.registration import (
    register_for_event,
    view_my_registrations,
    cancel_registration
)

# EventVerse - Main Application
# Day 1... Start with the main.
# Developed by Aaron.


# SECTION 1: Welcome Banner
def display_banner():
    print("========================================")
    print("       WELCOME TO EVENTVERSE")
    print("  Discover. Register. Experience.")
    print("========================================")


# SECTION 2: Main Menu
def display_menu():

    print("\n========================================")
    print("             EVENTVERSE")
    print("========================================")
    print("\n1. Student Login")
    print("2. Create Account")
    print("3. Forgot Password")
    print("4. Admin Login")
    print("5. Exit")
    print("\n========================================")


#Student Dashboard
def student_dashboard(student):

    while True:
        print("\n========================================")
        print("           STUDENT DASHBOARD")
        print("========================================")

        print("\n1. Browse Events")
        print("2. My Registered Events")
        print("3. Cancel Registration")
        print("4. My Tickets")
        print("5. My Profile")
        print("6. My Rewards")
        print("7. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_events(student, register_for_event)

        elif choice == "2":
            view_my_registrations(student)

        elif choice == "3":
            cancel_registration(student)

        elif choice == "4":
            view_my_tickets(student)

        elif choice == "5":
            student_profile(student)

        elif choice == "6":
            view_my_rewards(student)

        elif choice == "7":
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice!")
 























# SECTION 5: Admin Login Page
def admin_login():
    print("\n========== ADMIN LOGIN ==========")

    # Predefined admin credentials
    admin_username = "admin0001"
    admin_password = "1234"

    # Ask for login details
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    # Verify credentials
    if username == admin_username and password == admin_password:
        print("\nAccess granted!")
        print("Welcome, Administrator.")

        admin_dashboard()

    else:
        print("\nAccess denied!")
        print("Invalid username or password.")





































# SECTION: View Registered Students
def view_registered_students():

    print("\n========================================")
    print("         REGISTERED STUDENTS")
    print("========================================")

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Check whether registrations exist
    if len(registrations) == 0:
        print("\nNo students have registered for any events yet.")
        return

    # Load student information
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Display registered students
    for registration in registrations:

        for student in students:

            if student["student_id"] == registration["student_id"]:

                print("\n----------------------------------------")
                print("Student ID:", student["student_id"])
                print("Full Name:", student["full_name"])
                print("Username:", student["username"])
                print("Email:", student["email"])
                print("Event ID:", registration["event_id"])
                print("Attendance:", registration["attendance"])
                print("----------------------------------------")

                break

    print("\nTotal Event Registrations:", len(registrations))



# SECTION: Attendance Management
def attendance_management():

    while True:
        print("\n========================================")
        print("          ATTENDANCE MANAGEMENT")
        print("========================================")

        print("\n1. View Attendance Records")
        print("2. Mark Student Attendance")
        print("3. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_attendance_records()

        elif choice == "2":
            mark_event_attendance()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice! Please try again.")



# SECTION: View Attendance Records
def view_attendance_records():

    print("\n========================================")
    print("         ATTENDANCE RECORDS")
    print("========================================")

    # Load available events
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Check whether events exist
    if len(events) == 0:
        print("\nNo events available.")
        return

    # Display available events
    print("\nAvailable Events:")

    for event in events:
        print(event["event_id"], "-", event["name"])

    # Ask admin to select an event
    event_id = input("\nEnter Event ID: ").strip()

    # Find selected event
    selected_event = None

    for event in events:
        if event["event_id"] == event_id:
            selected_event = event
            break

    if selected_event is None:
        print("\nEvent not found!")
        return

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Find registrations for selected event
    event_registrations = []

    for registration in registrations:
        if registration["event_id"] == event_id:
            event_registrations.append(registration)

    # Check whether students are registered
    if len(event_registrations) == 0:
        print("\nNo students registered for this event yet.")
        return

    # Load student information
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Display attendance records
    print("\n========================================")
    print("Event:", selected_event["name"])
    print("========================================")

    present_count = 0
    absent_count = 0
    not_marked_count = 0

    for i, registration in enumerate(event_registrations, start=1):

        student_name = registration["student_id"]

        for student in students:
            if student["student_id"] == registration["student_id"]:
                student_name = student["full_name"]
                break

        attendance = registration["attendance"]

        if attendance == "Present":
            present_count += 1

        elif attendance == "Absent":
            absent_count += 1

        else:
            not_marked_count += 1

        print(f"{i}. {student_name} - {attendance}")

    # Calculate attendance rate
    total_students = len(event_registrations)
    attendance_rate = (present_count / total_students) * 100

    # Display attendance summary
    print("\n========================================")
    print("         ATTENDANCE SUMMARY")
    print("========================================")
    print("Total Registered:", total_students)
    print("Present:", present_count)
    print("Absent:", absent_count)
    print("Not Marked:", not_marked_count)
    print("Attendance Rate:", round(attendance_rate, 2), "%")
    print("========================================")



# SECTION: Mark Event Attendance
def mark_event_attendance():

    print("\n========================================")
    print("          MARK EVENT ATTENDANCE")
    print("========================================")

    # Load events
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Check available events
    if len(events) == 0:
        print("\nNo events available.")
        return

    # Display available events
    print("\nAvailable Events:")

    for event in events:
        print(event["event_id"], "-", event["name"])

    # Ask admin to select an event
    event_id = input("\nEnter Event ID: ").strip()

    # Find selected event
    selected_event = None

    for event in events:
        if event["event_id"] == event_id:
            selected_event = event
            break

    if selected_event is None:
        print("\nEvent not found!")
        return

    # Load registrations
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Find students registered for this event
    event_registrations = []

    for registration in registrations:
        if registration["event_id"] == event_id:
            event_registrations.append(registration)

    # Check registrations
    if len(event_registrations) == 0:
        print("\nNo students registered for this event yet.")
        return

    # Load student information
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Display attendance list
    print("\nEvent:", selected_event["name"])
    print("\nRegistered Students:")

    for i, registration in enumerate(event_registrations, start=1):

        student_name = registration["student_id"]

        for student in students:
            if student["student_id"] == registration["student_id"]:
                student_name = student["full_name"]
                break

        print(f"{i}. {student_name} - {registration['attendance']}")

    # Mark everyone present first
    print("\nMarking all students as Present...")

    for registration in event_registrations:
        registration["attendance"] = "Present"

    # Select students who are absent
    absent_input = input(
        "\nEnter the numbers of absent students (separated by commas).\n"
        "Press Enter if everyone is present: "
    ).strip()

    if absent_input:
        absent_numbers = absent_input.split(",")

        for number in absent_numbers:
            try:  #tells Python: Try executing this code.
                index = int(number.strip())

                if 1 <= index <= len(event_registrations):
                    event_registrations[index - 1]["attendance"] = "Absent"
                else:
                    print("Invalid student number:", number)

            except ValueError: #tells python: If an error occurs, execute this code instead.
                print("Invalid input:", number)

    # Save updated attendance
    with open("data/registrations.json", "w") as file:
        json.dump(registrations, file, indent=4)

    print("\nAttendance saved successfully!")


# SECTION: View All Student Accounts
def view_all_students():

    print("\n========================================")
    print("          ALL STUDENT ACCOUNTS")
    print("========================================")

    # Load student records
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Check whether student accounts exist
    if len(students) == 0:
        print("\nNo student accounts have been created yet.")
        return

    # Display all student accounts
    for i, student in enumerate(students, start=1):

        print("\n----------------------------------------")
        print("Student Number:", i)
        print("Student ID:", student["student_id"])
        print("Full Name:", student["full_name"])
        print("Username:", student["username"])
        print("Email:", student["email"])
        print("----------------------------------------")

    print("\nTotal Student Accounts:", len(students))


    # SECTION: View Students Menu
def view_students_menu():

    while True:

        print("\n========================================")
        print("             VIEW STUDENTS")
        print("========================================")
        print("1. View All Student Accounts")
        print("2. View Event Registrations")
        print("3. Back to Admin Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_all_students()

        elif choice == "2":
            view_registered_students()

        elif choice == "3":
            break

        else:
            print("\nInvalid choice. Please try again.")

# SECTION 6: Admin Dashboard
def admin_dashboard():
    print("\n========================================")
    print("           ADMIN DASHBOARD")
    print("========================================")

    while True:
        print("\nWelcome, Administrator!")
        print("\n1. Create New Event")
        print("2. Manage Events")
        print("3. View Students")
        print("4. Attendance Management")
        print("5. Reports & Analytics")
        print("6. Logout")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_event()

        elif choice == "2":
            manage_events()

        elif choice == "3":
            view_students_menu()

        elif choice == "4":
            attendance_management()

        elif choice == "5":
          reports_and_analytics()

        elif choice == "6":
            print("\nLogging out...")
            break

        else:
            print("\nInvalid choice! Please try again.")



# SECTION 7: Main Application
display_banner()

while True:

    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        student_login(student_dashboard)

    elif choice == "2":
        create_account()

    elif choice == "3":
        reset_password()

    elif choice == "4":
        admin_login()

    elif choice == "5":
        print("\nThank you for using EventVerse!")
        print("Goodbye!")
        break

    else:
        print("\nInvalid choice! Please try again.")
