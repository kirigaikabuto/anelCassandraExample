from cassandra.cluster import Cluster


class CassandraConnect:
    def __init__(self, keyspace):
        cluster = Cluster()
        self.session = cluster.connect(keyspace)

    def execute(self, query):
        data = self.session.execute(query)
        return data

    def allCities(self):
        data = self.execute("select * from cities")
        return data.all()

    def createCity(self, name, country):
        data = self.allCities()
        id = 1
        if len(data) > 0:
            numerics = []
            for i in data:
                numerics.append(i.id)
            id = max(numerics) + 1
        query = f"insert into cities (id,name,country) values ({id},'{name}','{country}')"
        newCity = self.execute(query)
        return "City is created"

    def getCityById(self, id):
        data = self.allCities()
        isFind = False
        element = None
        for i in data:
            if i.id == id:
                isFind = True
                element = i
                break
        if isFind:
            return element
        else:
            return "No data"

    def update(self, name="", country="", id=0):
        query = "update cities set "
        if name != "" and country != "":
            query += f"name='{name}',country='{country}' "
        elif name != "":
            query += f"name='{name}' "
        elif country != "":
            query += f"country='{country}' "
        else:
            return "No data to update"
        if id == 0:
            return "No id"
        query += f"where id={id}"
        self.execute(query)
        return "data is updated"

    def delete(self, id):
        query = f"delete from cities where id={id}"
        self.execute(query)
        return "Data was deleted"
