import datetime

class Event:
    def __init__(self, title, description, date, time):
        # Constructor to initialize event attributes
        self.title = title
        self.description = description
        self.date = date
        self.time = time

class EventScheduler:
    def __init__(self):
        # Constructor to initialize EventScheduler object with an empty list of events
        self.events = []

    def create_event(self, title, description, date, time):
        try:
            # Attempt to parse date and time strings into datetime objects
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            event_time = datetime.datetime.strptime(time, "%H:%M")
        except ValueError:
            # Handle invalid date or time format
            print(
                "Error: Date or time format is incorrect. Please use YYYY-MM-DD format for date and HH:MM format for time.")
            return
        # Method to create a new event and add it to the list of events
        event = Event(title, description, event_date, event_time)
        self.events.append(event)

    def view_all_events(self):
        # Method to view all events in the list
        if not self.events:
            print("No events scheduled.")
        else:
            print("All Events:")
            for idx, event in enumerate(self.events, start=1):
                print(f"{idx}. {event.title} - {event.description} - {event.date} - {event.time}")

    def delete_event(self, title):
        # Method to delete an event with a specific title from the list
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                print(f"Event '{title}' deleted successfully.")
                return
        print(f"Event with title '{title}' not found.")

    def search_events(self, keyword):
        # Method to search events by keyword in title or description
        found_events = []
        for event in self.events:
            if keyword in event.title or keyword in event.description:
                found_events.append(event)
        if not found_events:
            print("No events found matching the keyword.")
        else:
            print("Found Events:")
            for idx, event in enumerate(found_events, start=1):
                print(f"{idx}. {event.title} - {event.description} - {event.date} - {event.time}")

    def edit_event(self, title):
        # Method to edit an existing event
        for event in self.events:
            if event.title == title:
                print("Editing Event:")
                print(f"Title: {event.title}")
                print(f"Description: {event.description}")
                print(f"Date: {event.date}")
                print(f"Time: {event.time}")
                new_title = input("Enter new title (press Enter to keep current): ")
                event.title = new_title if new_title else event.title
                new_description = input("Enter new description (press Enter to keep current): ")
                event.description = new_description if new_description else event.description
                new_date = input("Enter new date (YYYY-MM-DD) (press Enter to keep current): ")
                event.date = new_date if new_date else event.date
                new_time = input("Enter new time (HH:MM) (press Enter to keep current): ")
                event.time = new_time if new_time else event.time
                print("Event edited successfully.")
                return
        print(f"Event with title '{title}' not found.")

# Main function
def main():
    # Create an instance of EventScheduler
    event_scheduler = EventScheduler()

    # Main loop for the program
    while True:
        print("\nEvent Scheduler Menu:")
        print("1. Create Event")
        print("2. View All Events")
        print("3. Search Events")
        print("4. Edit Event")
        print("5. Delete Event")
        print("6. Exit")

        # Get user input for menu choice
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            # Create a new event
            title = input("Enter event title: ")
            description = input("Enter event description: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            event_scheduler.create_event(title, description, date, time)
            print("event has been create successfully!!")

        elif choice == "2":
            # View all events
            event_scheduler.view_all_events()

        elif choice == "3":
            # Search events
            keyword = input("Enter keyword to search: ")
            event_scheduler.search_events(keyword)

        elif choice == "4":
            # Edit an existing event
            title = input("Enter event title to edit: ")
            event_scheduler.edit_event(title)

        elif choice == "5":
            # Delete an event
            title = input("Enter event title to delete: ")
            event_scheduler.delete_event(title)

        elif choice == "6":
            # Exit the program
            print("Exiting...")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    # Run the main function if this script is executed directly
    main()
