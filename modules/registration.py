import json
import secrets
# Event Registration System


# SECTION: Register for an Event
def register_for_event(student, selected_event):

    print("\n========================================")
    print("          EVENT REGISTRATION")
    print("========================================")

    # Load existing registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Check for duplicate registration
    for registration in registrations:

        if (registration["student_id"] == student["student_id"]
                and registration["event_id"] == selected_event["event_id"]):

            print("\nYou have already registered for this event!")
            return

    # Check event capacity
    event_registrations = []

    for registration in registrations:

        if registration["event_id"] == selected_event["event_id"]:
            event_registrations.append(registration)

    if len(event_registrations) >= selected_event["capacity"]:
        print("\nSorry! This event is fully booked.")
        return

    # Generate Registration ID
    registration_id = f"REG{len(registrations) + 1:03d}"

    # Generate Ticket ID
    ticket_id = "TKT" + secrets.token_hex(4).upper()

    # Create registration record
    new_registration = {
        "registration_id": registration_id,
        "ticket_id": ticket_id,
        "student_id": student["student_id"],
        "event_id": selected_event["event_id"],
        "attendance": "Not Marked"
    }

    # Save registration
    registrations.append(new_registration)

    with open("data/registrations.json", "w") as file:
        json.dump(registrations, file, indent=4)

    print("\nRegistration successful!")
    print("Registration ID:", registration_id)
    print("Ticket ID:", ticket_id)
    print("Event:", selected_event["name"])




# SECTION: View My Registered Events
def view_my_registrations(student):

    print("\n========================================")
    print("          MY REGISTERED EVENTS")
    print("========================================")

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Find registrations belonging to the logged-in student
    my_registrations = []

    for registration in registrations:

        if registration["student_id"] == student["student_id"]:
            my_registrations.append(registration)

    # Check whether the student has registered for any events
    if len(my_registrations) == 0:
        print("\nYou have not registered for any events yet.")
        return

    # Load event information
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Display registered events
    for registration in my_registrations:

        for event in events:

            if event["event_id"] == registration["event_id"]:

                print("\n----------------------------------------")
                print("Registration ID:", registration["registration_id"])
                print("Ticket ID:", registration["ticket_id"])
                print("Event Name:", event["name"])
                print("Date:", event["date"])
                print("Time:", event["time"])
                print("Venue:", event["venue"])
                print("Attendance:", registration["attendance"])
                print("----------------------------------------")

                break

    print("\nTotal Registered Events:", len(my_registrations))





# SECTION: Cancel Event Registration
def cancel_registration(student):

    print("\n========================================")
    print("          CANCEL REGISTRATION")
    print("========================================")

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)

    # Find registrations belonging to the logged-in student
    my_registrations = []

    for registration in registrations:

        if registration["student_id"] == student["student_id"]:
            my_registrations.append(registration)

    # Check whether the student has any registrations
    if len(my_registrations) == 0:
        print("\nYou have no registrations to cancel.")
        return

    # Load event information
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Display student's registrations
    for i, registration in enumerate(my_registrations, start=1):

        for event in events:

            if event["event_id"] == registration["event_id"]:

                print("\n----------------------------------------")
                print("Registration Number:", i)
                print("Registration ID:", registration["registration_id"])
                print("Ticket ID:", registration["ticket_id"])
                print("Event Name:", event["name"])
                print("Event Date:", event["date"])
                print("----------------------------------------")

                break

    # Ask which registration to cancel
    choice = input("\nEnter registration number to cancel (0 to go back): ")

    if choice == "0":
        return

    try:
        registration_number = int(choice)

        if registration_number < 1 or registration_number > len(my_registrations):
            print("\nInvalid registration number!")
            return

    except ValueError:
        print("\nPlease enter a valid number.")
        return

    # Get selected registration
    selected_registration = my_registrations[registration_number - 1]

    # Confirm cancellation
    confirmation = input(
        "\nAre you sure you want to cancel this registration? (yes/no): "
    ).strip().lower()

    if confirmation != "yes":
        print("\nCancellation aborted.")
        return

    # Remove registration from original records
    registrations.remove(selected_registration)

    # Save updated registration records
    with open("data/registrations.json", "w") as file:
        json.dump(registrations, file, indent=4)

    print("\nRegistration cancelled successfully!")
    print("Registration ID:", selected_registration["registration_id"])
    print("Your event seat is now available again.")

