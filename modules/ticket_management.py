import json

# Ticket and Attendance Management

# SECTION: View My Tickets
def view_my_tickets(student):

    print("\n========================================")
    print("               MY TICKETS")
    print("========================================")

    # Load registration records
    with open("data/registrations.json", "r") as file:
        registrations = json.load(file)


    # Find tickets belonging to the logged-in student
    my_tickets = []

    for registration in registrations:

        if registration["student_id"] == student["student_id"]:
            my_tickets.append(registration)


                # Check whether the student has any tickets
    if len(my_tickets) == 0:
        print("\nYou don't have any tickets yet.")
        return

        # Load event information
    with open("data/events.json", "r") as file:
        events = json.load(file)



            # Display student tickets
    for registration in my_tickets:

        for event in events:

            if event["event_id"] == registration["event_id"]:

                print("\n========================================")
                print("               EVENT TICKET")
                print("========================================")

                print("Ticket ID:", registration["ticket_id"])
                print("Registration ID:", registration["registration_id"])
                print("Event Name:", event["name"])
                print("Date:", event["date"])
                print("Time:", event["time"])
                print("Venue:", event["venue"])
                print("Attendance:", registration["attendance"])

                print("========================================")

                break