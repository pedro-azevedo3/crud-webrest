import datetime

class Player: 
    def __init__(self, club, name, age, position):
        self.name = name
        self.position = position
        self.age = age
        self.club = club
        self.updatedAt = datetime.datetime.now()
        self.createdAt = datetime.datetime.now()
       
    def __repr__(self):
        return {k:str(v) for k,v in self.__dict__.items()}

    def save(self, collection):
        collection.insert_one(self.__repr__())
        return self
    
    @staticmethod
    def get(players, id):
        for player in players:
            if str(player.get("_id")) == id:
                return Player(player.get("name"))
        return None

    def update(self, body, name, collection):
        attributes_to_update = ["name","age","club","position"]
        
        
        for attribute in attributes_to_update:
            setattr(self, attribute, body.get(attribute))

        self.updatedAt = datetime.now()
        collection.update_one({"name":name},{"$set":self.__repr__()})
        return self


    def delete(self,collection):
        collection.delete_one({"name":self.name})
        return self
