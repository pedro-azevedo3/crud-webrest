
class PDF:
    def __init__(self, name, url, user):
        self.name = name
        self.url = url
        self.user = user

    def __repr__(self):
        return self.__dict__

    def save(self):
        return self
    
    def udpate(self):
        return self
    
    def delete(self):
        return self
    
    def get(self):
        return self