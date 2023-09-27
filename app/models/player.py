import datetime

players = []


class Player: 
    def __init__(self, id, name, age, position):
        self.id = id
        self.name = name
        self.position = position
        self.age = age
        self.updatedAt = datetime.now()
        self.createdAt = datetime.now()
       
    def __repr__(self):
        return self.__dict__

    def save(self):
        players.append(self)
        return self
    
    def get(self, id):
        for player in players:
            if player.id == id:
                return player
        return None

    def update(self, body):
        attributes_to_update = ["club"]
        
        for attribute in attributes_to_update:
            setattr(self, attribute, body.get(attribute))

        self.updatedAt = datetime.now()
        return self

    def delete(self, players):
        players.remove(self)
        return self
