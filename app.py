import tkinter as tk
from tkinter import ttk
import requests

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoData App")

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Label pour les données des utilisateurs
        users_label = ttk.Label(main_frame, text="Utilisateurs:")
        users_label.grid(row=0, column=0, sticky="w")

        # Zone de texte pour afficher les données des utilisateurs
        self.users_text = tk.Text(main_frame, height=10, width=50)
        self.users_text.grid(row=1, column=0, padx=10, pady=5)

        # Label pour les données des lieux
        locations_label = ttk.Label(main_frame, text="Lieux:")
        locations_label.grid(row=2, column=0, sticky="w")

        # Zone de texte pour afficher les données des lieux
        self.locations_text = tk.Text(main_frame, height=10, width=50)
        self.locations_text.grid(row=3, column=0, padx=10, pady=5)

        # Label pour les données des événements
        events_label = ttk.Label(main_frame, text="Événements:")
        events_label.grid(row=4, column=0, sticky="w")

        # Zone de texte pour afficher les données des événements
        self.events_text = tk.Text(main_frame, height=10, width=50)
        self.events_text.grid(row=5, column=0, padx=10, pady=5)

        # Label pour les données des commentaires
        comments_label = ttk.Label(main_frame, text="Commentaires:")
        comments_label.grid(row=6, column=0, sticky="w")

        # Zone de texte pour afficher les données des commentaires
        self.comments_text = tk.Text(main_frame, height=10, width=50)
        self.comments_text.grid(row=7, column=0, padx=10, pady=5)

        # Bouton pour rafraîchir les données
        refresh_button = ttk.Button(main_frame, text="Rafraîchir", command=self.refresh_data)
        refresh_button.grid(row=8, column=0, pady=10)

        # Appeler la méthode refresh_data pour charger les données lors du démarrage
        self.refresh_data()

    def refresh_data(self):
        # Récupérer les données des endpoints de l'API Flask
        users_response = requests.get('http://127.0.0.1:5000/users')
        locations_response = requests.get('http://127.0.0.1:5000/locations')
        events_response = requests.get('http://127.0.0.1:5000/events')
        comments_response = requests.get('http://127.0.0.1:5000/comments')

        # Effacer les anciennes données dans les zones de texte
        self.users_text.delete('1.0', tk.END)
        self.locations_text.delete('1.0', tk.END)
        self.events_text.delete('1.0', tk.END)
        self.comments_text.delete('1.0', tk.END)

        # Mettre à jour les zones de texte avec les nouvelles données
        self.users_text.insert(tk.END, users_response.text)
        self.locations_text.insert(tk.END, locations_response.text)
        self.events_text.insert(tk.END, events_response.text)
        self.comments_text.insert(tk.END, comments_response.text)