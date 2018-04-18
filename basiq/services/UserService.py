class User:
    def __init__(self, service):
        self.service = service

    def forUser(self, id):
        self.id = id
        return self

    def get(self):
        r = self.service.get(self.id)
        self.email = r["email"]
        self.mobile = r["mobile"]
        return self

    def refreshAllConnections(self):
        return self.service.refreshAllConnections(self.id)

    def listAllConnections(self):
        return self.service.listAllConnections(self.id)

    def getTransaction(self, id):
        return self.service.getTransaction(self.id, id)

    def getTransactions(self):
        return self.service.getTransactions(self.id)

    def getAccount(self, id):
        return self.service.getAccount(self.id, id)

    def getAccounts(self):
        return self.service.getAccounts(self.id)


class UserService:
    def __init__(self, session):
        self.session = session
    
    def forUser(self, id):
        return User(self).forUser(id)

    def get(self, id):
        r = self.session.api.get("users/" + id)

        u = User(self)
        u.email = r["email"]
        u.mobile = r["mobile"]

        return u

    def create(self, email = None, mobile = None):
        json = {}
        if email == None and mobile == None:
            raise Exception("Neither email or mobile were provided")
        if email != None:
            json["email"] = email
        if mobile != None:
            json["mobile"] = mobile
            
        r = self.session.api.post("users/", json=json)

        u = User(self)
        u.email = r["email"]
        u.mobile = r["mobile"]

        return u

    def update(self, id, email = None, mobile = None):
        json = {}
        if email == None and mobile == None:
            raise Exception("Neither email or mobile were provided")
        if email != None:
            json["email"] = email
        if mobile != None:
            json["mobile"] = mobile
            
        r = self.session.api.post("users/" + id, json=json)

        u = User(self)
        u.email = r["email"]
        u.mobile = r["mobile"]

        return u

    def delete(self, id):            
        self.session.api.delete("users/" + id)

        return None

    def refreshAllConnections(self, id):
        r = self.session.api.post("users/" + id + "/connections/refresh")

        return r

    def listAllConnections(self, id):
        return self.session.api.get("users/" + id + "/connections")
        
    def getTransaction(self, user_id, id):
        return self.session.api.get("users/" + user_id + "/transactions/" + id)

    def getTransactions(self, user_id):
        return self.session.api.get("users/" + user_id + "/transactions")
        
    def getAccount(self, user_id, id):
        return self.session.api.get("users/" + user_id + "/accounts/" + id)

    def getAccounts(self, user_id):
        return self.session.api.get("users/" + user_id + "/accounts")