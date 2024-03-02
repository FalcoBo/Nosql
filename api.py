from flask import Flask, jsonify
from pymongo import MongoClient

class GeoDataAPI:
    def __init__(self):
        self.app = Flask(__name__)
        
        # Connect to MongoDB
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.geospatial_database

        # Methode to get all users
        @self.app.route('/users', methods=['GET'])
        def get_users():
            users_collection = self.db.users
            users = list(users_collection.find({}, {'_id': 0}))
            return jsonify(users)

        # Methode to get all locations
        @self.app.route('/locations', methods=['GET'])
        def get_locations():
            locations_collection = self.db.locations
            locations = list(locations_collection.find({}, {'_id': 0}))
            return jsonify(locations)

        # Methode to get all events
        @self.app.route('/events', methods=['GET'])
        def get_events():
            events_collection = self.db.events
            events = list(events_collection.find({}, {'_id': 0}))
            return jsonify(events)

        # Methode to get all comments
        @self.app.route('/comments', methods=['GET'])
        def get_comments():
            comments_collection = self.db.comments
            comments = list(comments_collection.find({}, {'_id': 0}))
            return jsonify(comments)

    # Methode to run the API
    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    geo_api = GeoDataAPI()
    geo_api.run()
