from pymongo import MongoClient
from faker import Faker
import logging
from random import choice

class GeoData:
    def __init__(self, num_users=20, num_locations=20, num_events=20, num_comments=20):
        self.num_users = num_users
        self.num_locations = num_locations
        self.num_events = num_events
        self.num_comments = num_comments
        self.fake = Faker()
        
        # Configure logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # Method to generate fake users
    def generate_users(self):
        users = []
        for _ in range(self.num_users):
            users.append({
                "username": self.fake.user_name(),
                "email": self.fake.email()
            })
        self.logger.info("Utilisateurs générés avec succès!")
        return users

    # Method to generate fake locations
    def generate_locations(self):
        locations = []
        for _ in range(self.num_locations):
            locations.append({
                "name": self.fake.city(),
                "latitude": self.fake.latitude(),
                "longitude": self.fake.longitude()
            })
        self.logger.info("Locations générées avec succès!")
        return locations

    # Method to generate fake events
    def generate_events(self, locations):
        events = []
        for _ in range(self.num_events):
            events.append({
                "name": self.fake.catch_phrase(),
                "category": choice(["Music", "Business", "Sport", "Conference"]),
                "location": choice(locations)["name"]
            })
        self.logger.info("Événements générés avec succès!")
        return events

    # Method to generate fake comments
    def generate_comments(self, users, locations, events):
        comments = []
        for _ in range(self.num_comments):
            comment_type = choice(["location", "event"])
            if comment_type == "location":
                entity = choice(locations)["name"]
            else:
                entity = choice(events)["name"]
            comments.append({
                "user": choice(users)["username"],
                "text": self.fake.text(),
                comment_type: entity
            })
        self.logger.info("Commentaires générés avec succès!")
        return comments

    # Method to insert generated data into MongoDB
    def generate_and_insert_data(self):
        try:
            client = MongoClient('localhost', 27017)
            db = client.geospatial_database

            users_collection = db.users
            locations_collection = db.locations
            events_collection = db.events
            comments_collection = db.comments

            users_data = self.generate_users()
            locations_data = self.generate_locations()
            events_data = self.generate_events(locations_data)
            comments_data = self.generate_comments(users_data, locations_data, events_data)

            users_collection.insert_many(users_data)
            locations_collection.insert_many(locations_data)
            events_collection.insert_many(events_data)
            comments_collection.insert_many(comments_data)

            self.logger.info("Base de données remplie avec succès!")
        except Exception as e:
            self.logger.error(f"Une erreur s'est produite lors de l'insertion des données : {str(e)}")

# Use the class to generate and insert data
generator = GeoData(num_users=20, num_locations=20, num_events=20, num_comments=20)
generator.generate_and_insert_data()
