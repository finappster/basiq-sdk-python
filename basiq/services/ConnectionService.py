class Connection:
    def __init__(self, service):
        self.service = service

    def forConnection(self, id):
        self.id = id
        return self

    def refresh(self):
        return self.service.refresh(self.id)

class Job:
    def __init__(self, service):
        self.service = service

    def forJob(self, id):
        self.id = id
        return self

class ConnectionService:
    def __init__(self, session, user):
        self.session = session
        self.user = user

    def forConnection(self, id):
        return Connection(self).forConnection(id)

    def get(self, id):
        r = self.session.api.get("users/" + self.user.id + "/connections/" + id)

        c = Connection(self)
        c.id = r["id"]
        c.status = r["status"]
        c.last_used = r["lastUsed"]
        c.institution = r["institution"]
        c.accounts = r["accounts"]
        c.links = r["links"]

        return c

    def getJob(self, id):
        r = self.session.api.get("jobs/" + id)

        j = Job(self)
        j.id = r["id"]
        j.created = r["created"]
        j.updated = r["updated"]
        if "steps" in r:
            j.steps = r["steps"]

        return j

    def create(self, connection_data):
        if "loginId" not in connection_data:
            raise Exception("Login id needs to be suplied")
        if "password" not in connection_data:
            raise Exception("Password id needs to be suplied")
        if "institution" not in connection_data:
            raise Exception("Institution data needs to be suplied")
        if "id" not in connection_data["institution"]:
            raise Exception("Institution id needs to be suplied")

        r = self.session.api.post("users/" + self.user.id + "/connections", json=connection_data)

        j = Job(self)
        j.id = r["id"]

        return j

    def update(self, id, password):
        r = self.session.api.post("users/" + self.user.id + "/connections/" + id, json={password: password})

        j = Job(self)
        j.id = r["id"]

        return j

    def delete(self, id):
        self.session.api.delete("users/" + self.user.id + "/connections/" + id)

        return None

    def refresh(self, id):
        r = self.session.api.post("users/" + self.user.id + "/connections/" + id + "/refresh")

        j = Job(self)
        j.id = r["id"]

        return j