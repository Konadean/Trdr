import sqlite3
import random

class Towns:

    def __init__(self, db_conn : sqlite3.Connection, map_length : int, map_width : int):
        # Town - Database Variables
        self.db_conn = db_conn
        self.table_name = "towns"
        self.cols = {"name" : "TEXT", "specialty" : "TEXT", "x_coord" : "INTEGER", "y_coord" : "INTEGER"}

        # Town - Map Relational Variables
        self.map_length = map_length
        self.map_width = map_width
        self.total_num_towns = int(map_length * map_width * 0.05)

        # Town - Static Variables
        self.name_settlement_type = ["Village", "Town", "City", "Capital", "Principality", "Barony", "Dutchy", "County", "State", "Land", "Fotress"]
        self.name_start = ["Atlo", "Bri", "Cire", "Davvi", "Equ", "Fuo", "Go", "Halsa", "Iili", "Juru", "Kyzi", "Lany", "Mory", "Niero", "Oora"]
        self.name_end = ["bolv", "cros", "driyo", "fosla", "gazo", "hulvi", "joka", "kov", "las", "mirr", "nyst"]
        self.town_specialties = ["Agricultural", "Pastoral", "Mining", "Smithing", "Fishing", "Textiles"]
        self.towns_index = {}

    def __generate_town_names(self) -> list[str]:
        names = []
        for i in range(self.total_num_towns):
            name = self.name_settlement_type[random.randint(0,len(self.name_settlement_type)-1)] + " of " + self.name_start[random.randint(0,len(self.name_start)-1)] + self.name_start[random.randint(0,len(self.name_end)-1)]
            while name in names:
                name = self.name_settlement_type[random.randint(0,len(self.name_settlement_type)-1)] + " of " + self.name_start[random.randint(0,len(self.name_start)-1)] + self.name_start[random.randint(0,len(self.name_end)-1)]
            names.append(name)
        return names

    def __generate_town_specialties(self) -> list[str]:
        specialties = []

        return specialties

    def __generate_town_locations(self) -> list[tuple[int]]:
        locations = []
        for i in range(self.total_num_towns):
            loc = (random.randint(0,self.map_length), random.randint(0,self.map_width))
            while loc in locations:
                loc = (random.randint(0,self.map_length), random.randint(0,self.map_width))
            locations.append(loc)
        return locations