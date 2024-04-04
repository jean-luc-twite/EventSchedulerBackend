import unittest
from event_scheduler import Event, EventScheduler

class TestEventScheduler(unittest.TestCase):
    def setUp(self):
        self.event_scheduler = EventScheduler()

        # Create some sample events for testing
        self.event1 = Event("Meeting", "Team meeting", "2024-04-05", "09:00")
        self.event2 = Event("Presentation", "Project presentation", "2024-04-07", "14:00")
        self.event3 = Event("Interview", "Job interview", "2024-04-10", "11:00")

        # Add sample events to the event scheduler
        self.event_scheduler.events = [self.event1, self.event2, self.event3]

    def test_create_event(self):
        # Test creating a new event
        self.event_scheduler.create_event("Training", "Training session", "2024-04-15", "10:00")
        self.assertEqual(len(self.event_scheduler.events), 4)

    def test_view_all_events(self):
        # Test viewing all events
        expected_output = "All Events:\n1. Meeting - Team meeting - 2024-04-05 - 09:00\n" \
                          "2. Presentation - Project presentation - 2024-04-07 - 14:00\n" \
                          "3. Interview - Job interview - 2024-04-10 - 11:00\n"
        self.assertEqual(self.event_scheduler.view_all_events(), expected_output)


    def test_search_events(self):
        # Test searching for events by keyword
        expected_output = "Found Events:\n1. Presentation - Project presentation - 2024-04-07 - 14:00\n"
        self.assertEqual(self.event_scheduler.search_events("Presentation"), expected_output)

    def test_delete_event(self):
            # Test deleting an event
            self.event_scheduler.delete_event("Presentation")
            self.assertEqual(len(self.event_scheduler.events), 2)

    def test_edit_event(self):
        # Test editing an existing event
        new_title = "Updated Meeting"
        new_description = "Updated team meeting"
        new_date = "2024-04-06"
        new_time = "10:00"
        self.event_scheduler.edit_event("Meeting")
        self.assertEqual(self.event_scheduler.events[0].title, new_title)
        self.assertEqual(self.event_scheduler.events[0].description, new_description)
        self.assertEqual(self.event_scheduler.events[0].date, new_date)
        self.assertEqual(self.event_scheduler.events[0].time, new_time)


if __name__ == "__main__":
    unittest.main()
