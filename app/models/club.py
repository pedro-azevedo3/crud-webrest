from datetime import datetime

class Club: 
    def __init__(self, name):
        self.name = name
        self.updatedAt = datetime.now()
        self.createdAt = datetime.now()
       
    def __repr__(self):
        return {k:str(v) for k,v in self.__dict__.items()}

    def save(self, collection):
        collection.insert_one(self.__repr__())
        return self
    
    @staticmethod
    def get(id, clubs):
        for club in clubs:
            if str(club.get("_id")) == id:
                return Club(club.get("name"))
        return None

    def update(self, body, name, collection):
        attributes_to_update = ["name"]
        
        for attribute in attributes_to_update:
            setattr(self, attribute, body.get(attribute))
        
        self.updatedAt = datetime.now()
        collection.update_one({"name":name},{"$set":self.__repr__()})
        return self

    def delete(self, collection):
        collection.delete_one({"name":self.name})
        return self
