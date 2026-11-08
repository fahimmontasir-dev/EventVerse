import json
# Event Analytics and Reports

import json


# SECTION: Overall System Summary
def view_overall_summary():

    print("\n========================================")
    print("          OVERALL SYSTEM SUMMARY")
    print("========================================")

    # Load student records
    with open("data/users.json", "r") as file:
        students = json.load(file)

    # Load event records
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Calculate total numbers
    total_students = len(students)
    total_events = len(events)
    total_registrations = len(registrations)

    # Display summary
    print("\nTotal Registered Students:", total_students)
    print("Total Events Created:", total_events)
    print("Total Event Registrations:", total_registrations)


# SECTION: Event Analytics
def view_event_analytics():

    print("\n========================================")
    print("             EVENT ANALYTICS")
    print("========================================")

    # Load event records
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Check whether events exist
    if len(events) == 0:
        print("\nNo events available.")
        return

    total_registrations = 0
    most_popular_event = None
    highest_registrations = 0

    # Analyse each event
    for event in events:

        event_registrations = 0

        for registration in registrations:

            if registration["event_id"] == event["event_id"]:
                event_registrations += 1

        total_registrations += event_registrations

        # Calculate capacity usage
        capacity = event["capacity"]

        if capacity > 0:
            capacity_usage = (event_registrations / capacity) * 100
        else:
            capacity_usage = 0

        print("\nEvent:", event["name"])
        print("Registrations:", event_registrations)
        print("Capacity:", capacity)
        print("Capacity Usage:", round(capacity_usage, 2), "%")

        # Identify the most popular event
        if event_registrations > highest_registrations:
            highest_registrations = event_registrations
            most_popular_event = event["name"]

    # Display overall event statistics
    print("\n----------------------------------------")
    print("Total Registrations:", total_registrations)

    if most_popular_event is not None:
        print("Most Popular Event:", most_popular_event)
    else:
        print("Most Popular Event: No registrations yet")


# SECTION: Attendance Analytics
def view_attendance_analytics():

    print("\n========================================")
    print("          ATTENDANCE ANALYTICS")
    print("========================================")

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Check whether registrations exist
    if len(registrations) == 0:
        print("\nNo registration records available.")
        return

    # Initialize attendance counters
    total_present = 0
    total_absent = 0
    total_not_marked = 0

    # Analyse attendance records
    for registration in registrations:

        if registration["attendance"] == "Present":
            total_present += 1

        elif registration["attendance"] == "Absent":
            total_absent += 1

        else:
            total_not_marked += 1

    # Calculate attendance percentage
    total_marked = total_present + total_absent

    if total_marked > 0:
        attendance_percentage = (total_present / total_marked) * 100
    else:
        attendance_percentage = 0

    # Display attendance report
    print("\nTotal Registrations:", len(registrations))
    print("Students Present:", total_present)
    print("Students Absent:", total_absent)
    print("Attendance Not Marked:", total_not_marked)

    print("\nAttendance Percentage:",
          round(attendance_percentage, 2), "%")


# SECTION: Reports & Analytics
def reports_and_analytics():

    while True:

        print("\n========================================")
        print("          REPORTS & ANALYTICS")
        print("========================================")

        print("\n1. Overall System Summary")
        print("2. Event Analytics")
        print("3. Attendance Analytics")
        print("4. Back to Admin Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_overall_summary()

        elif choice == "2":
            view_event_analytics()

        elif choice == "3":
            view_attendance_analytics()

        elif choice == "4":
            break

        else:
            print("\nInvalid choice!")

