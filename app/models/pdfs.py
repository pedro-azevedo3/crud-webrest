class PDF:
    def __init__(self, name, url, user, id):
        self.name = name
        self.url = url
        self.user = user
        self.id = id

    def __repr__(self):
        return self.__dict__

    def save(self):
        return self
   
    def update(self, body):
        self.name = body.get("name")
        self.url = body.get("url")
        return self
   
    def delete(self):
        return self
    
    def get(self):
        return self