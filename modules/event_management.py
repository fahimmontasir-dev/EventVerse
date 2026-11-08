import json
import secrets
# Event Management



# SECTION: Create New Event
def create_event():

    print("\n========================================")
    print("             CREATE NEW EVENT")
    print("========================================")

    # Collect event information
    event_name = input("Enter event name: ")
    description = input("Enter event description: ")
    event_date = input("Enter event date: ")
    event_time = input("Enter event time: ")
    venue = input("Enter event venue: ")

    # Collect and validate ticket price and capacity
    try:
        price = float(input("Enter ticket price (RM): "))
        capacity = int(input("Enter maximum participants: "))

        if price < 0 or capacity <= 0:
            print("\nError: Price cannot be negative and capacity must be positive.")
            return

    except ValueError:
        print("\nError: Please enter valid numbers for price and capacity.")
        return

    # Check required information
    if not event_name.strip() or not description.strip() or not event_date.strip() or not event_time.strip() or not venue.strip():
        print("\nError: All event details are required.")
        return

    # Read existing events
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Generate event ID
    event_id = f"EVT{len(events) + 1:03d}"

    # Create event information1
    new_event = {
        "event_id": event_id,
        "name": event_name,
        "description": description,
        "date": event_date,
        "time": event_time,
        "venue": venue,
        "price": price,
        "capacity": capacity
    }

    # Add the event to the list
    events.append(new_event)

    # Save events into JSON file
    with open("data/events.json", "w") as file:
        json.dump(events, file, indent=4)

    print("\nEvent created successfully!")
    print("Event ID:", event_id)
    print("Event Name:", event_name)





# SECTION: Edit Event
def edit_event():

    print("\n========================================")
    print("               EDIT EVENT")
    print("========================================")

    # Load existing events
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Check if events exist
    if len(events) == 0:
        print("\nNo events available to edit.")
        return

    # Ask for Event ID
    event_id = input("\nEnter Event ID: ").strip()

    # Find the event
    selected_event = None

    for event in events:
        if event["event_id"] == event_id:
            selected_event = event
            break

    # Check whether event was found
    if selected_event is None:
        print("\nEvent not found!")
        return

    # Display current information
    print("\nCurrent Event Details:")
    print("1. Name:", selected_event["name"])
    print("2. Description:", selected_event["description"])
    print("3. Date:", selected_event["date"])
    print("4. Time:", selected_event["time"])
    print("5. Venue:", selected_event["venue"])
    print("6. Ticket Price:", selected_event["price"])
    print("7. Capacity:", selected_event["capacity"])

    print("\nLeave a field empty to keep its current value.")

    # Collect updated information
    new_name = input("\nNew event name: ").strip()
    new_description = input("New description: ").strip()
    new_date = input("New date: ").strip()
    new_time = input("New time: ").strip()
    new_venue = input("New venue: ").strip()

    # Update text fields if provided
    if new_name:
        selected_event["name"] = new_name

    if new_description:
        selected_event["description"] = new_description

    if new_date:
        selected_event["date"] = new_date

    if new_time:
        selected_event["time"] = new_time

    if new_venue:
        selected_event["venue"] = new_venue

    # Update price
    new_price = input("New ticket price (RM): ").strip()

    if new_price:
        try:
            price = float(new_price)

            if price < 0:
                print("\nPrice cannot be negative.")
                return

            selected_event["price"] = price

        except ValueError:
            print("\nInvalid price!")
            return

    # Update capacity
    new_capacity = input("New maximum participants: ").strip()

    if new_capacity:
        try:
            capacity = int(new_capacity)

            if capacity <= 0:
                print("\nCapacity must be positive.")
                return

            selected_event["capacity"] = capacity

        except ValueError:
            print("\nInvalid capacity!")
            return

    # Save updated events
    with open("data/events.json", "w") as file:
        json.dump(events, file, indent=4)

    print("\nEvent updated successfully!")
    print("Event ID:", event_id)


# SECTION: Delete Event
def delete_event():

    print("\n========================================")
    print("              DELETE EVENT")
    print("========================================")

    # Load existing events
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Check if events exist
    if len(events) == 0:
        print("\nNo events available to delete.")
        return

    # Ask for Event ID
    event_id = input("\nEnter Event ID to delete: ").strip()

    # Find the event
    selected_event = None

    for event in events:
        if event["event_id"] == event_id:
            selected_event = event
            break

    # Check whether event exists
    if selected_event is None:
        print("\nEvent not found!")
        return

    # Display event information
    print("\nEvent Found!")
    print("Event ID:", selected_event["event_id"])
    print("Event Name:", selected_event["name"])
    print("Event Date:", selected_event["date"])

    # Ask for confirmation
    confirmation = input("\nAre you sure you want to delete this event? (yes/no): ").lower()

    if confirmation == "yes":

        # Remove event from the list
        events.remove(selected_event)

        # Save updated list into JSON
        with open("data/events.json", "w") as file:
            json.dump(events, file, indent=4)

        print("\nEvent deleted successfully!")

    else:
        print("\nDeletion cancelled.")



# SECTION: Manage Events
def manage_events():

    while True:
        print("\n========================================")
        print("             MANAGE EVENTS")
        print("========================================")

        print("\n1. View All Events")
        print("2. Edit Event")
        print("3. Delete Event")
        print("4. Back to Dashboard")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            view_events()

        elif choice == "2":
            edit_event()

        elif choice == "3":
            delete_event()

        elif choice == "4":
            break

        else:
            print("\nInvalid choice! Please try again.")





# SECTION: View Available Events
def view_events(student=None, register_function=None):

    print("\n========================================")
    print("             AVAILABLE EVENTS")
    print("========================================")

    # Read events from JSON
    with open("data/events.json", "r") as file:
        events = json.load(file)

    # Check whether events exist
    if len(events) == 0:
        print("\nNo events available at the moment.")
        return

    # Display every event
    for i, event in enumerate(events, start=1):

        print("\n----------------------------------------")
        print("Event Number:", i)
        print("Event ID:", event["event_id"])
        print("Event Name:", event["name"])
        print("Description:", event["description"])
        print("Date:", event["date"])
        print("Time:", event["time"])
        print("Venue:", event["venue"])
        print("Ticket Price: RM", event["price"])
        print("Maximum Participants:", event["capacity"])
        print("----------------------------------------")

    # Allow students to select an event
    if student is not None:

        choice = input("\nEnter event number to view details (0 to go back): ")

        if choice == "0":
            return

        try:
            event_number = int(choice)

            if event_number < 1 or event_number > len(events):
                print("\nInvalid event number!")
                return

        except ValueError:
            print("\nPlease enter a valid number.")
            return

        selected_event = events[event_number - 1]

        print("\n========== EVENT DETAILS ==========")
        print("Event Name:", selected_event["name"])
        print("Date:", selected_event["date"])
        print("Time:", selected_event["time"])
        print("Venue:", selected_event["venue"])
        print("Ticket Price: RM", selected_event["price"])

        print("\n1. Register for This Event")
        print("2. Back to Events")

        action = input("\nEnter your choice: ")

        if action == "1":
            register_function(student, selected_event)

        elif action == "2":
            return

        else:
            print("\nInvalid choice!")




