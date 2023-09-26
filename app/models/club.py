from datetime import datetime

clubs = []

class Club: 
    def __init__(self, id, name):
        self.id = id
        self.user = name
        self.updatedAt = datetime.now()
        self.createdAt = datetime.now()
       
    def __repr__(self):
        return self.__dict__

    def save(self, clubs):
        clubs.append(self)
        return self
    
    def get(clubs, club_id):
        for club in clubs:
            if club.id == club_id:
                return club
        return None

    def update(self, body):
        attributes_to_update = ["id"]
        
        for attribute in attributes_to_update:
            setattr(self, attribute, body.get(attribute))
        
        self.updatedAt = datetime.now()
        return self

    def delete(self, clubs):
        clubs.remove(self)
        return self
