from flask import Flask, render_template, request, jsonify
import datetime
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

class Event:
    def __init__(self, title, description, date, time):
        self.title = title
        self.description = description
        self.date = date
        self.time = time


class EventScheduler:
    def __init__(self):
        self.events = []

    def create_event(self, title, description, date, time):
        # Method to create a new event and add it to the list of events
        event = Event(title, description, date, time)
        self.events.append(event)
        return True

    def view_all_events(self):
        return [vars(event) for event in self.events]

    def delete_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                return True
        return False

    def search_events(self, keyword):
        found_events = []
        for event in self.events:
            if keyword in event.title or keyword in event.description:
                found_events.append(event)
        return [vars(event) for event in found_events]

    def edit_event(self, title, new_title, new_description, new_date, new_time):
        for event in self.events:
            if event.title == title:
                event.title = new_title if new_title else event.title
                event.description = new_description if new_description else event.description
                event.date = new_date if new_date else event.date
                event.time = new_time if new_time else event.time
                return True
        return False


event_scheduler = EventScheduler()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/events', methods=['GET'])
def get_events():
    events = event_scheduler.view_all_events()
    return jsonify(events)


@app.route('/events/create', methods=['POST'])
def create_event():
    try:
        data = request.json
        if isinstance(data, dict):
            title = data.get('title')
            description = data.get('description')
            date = data.get('date')
            time = data.get('time')

            if title and description and date and time:
                success = event_scheduler.create_event(title, description, date, time)
                if success:
                    return 'Event created successfully', 201
                else:
                    return 'Error: Date or time format is incorrect. Please use YYYY-MM-DD format for date and HH:MM format for time.', 400
            else:
                return 'Error: Missing required fields.', 400
        else:
            return 'Error: Data must be in JSON format.', 400
    except Exception as e:
        return f'Error: {str(e)}', 500


@app.route('/events/<title>', methods=['DELETE'])
def delete_event(title):
    success = event_scheduler.delete_event(title)
    if success:
        return f'Event "{title}" deleted successfully', 200
    else:
        return f'Event with title "{title}" not found', 404


@app.route('/events/search')
def search_events():
    keyword = request.args.get('keyword')
    events = event_scheduler.search_events(keyword)
    return jsonify(events)


@app.route('/events/edit/<title>', methods=['PUT'])
def edit_event(title):
    data = request.json
    new_title = data.get('new_title')
    new_description = data.get('new_description')
    new_date = data.get('new_date')
    new_time = data.get('new_time')

    success = event_scheduler.edit_event(title, new_title, new_description, new_date, new_time)
    if success:
        return f'Event "{title}" edited successfully', 200
    else:
        return f'Event with title "{title}" not found', 404


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
