from typing import Protocol


class DBConnectionInterface(Protocol):
    def exec_query(self, query):
        ...


class DBConnection:
    def __init__(self):
        print("DB connection created")

    def exec_query(self, query):
        return f"Executing query: {query}"

    def close(self):
        print("DB connection closed")


class SmartProxy:
    def __init__(self):
        self.cnx = None
        self.ref_count = 0

    def access_resource(self):
        if self.cnx is None:
            self.cnx = DBConnection()
        self.ref_count += 1
        print(f"DB connection now has {self.ref_count} references.")

    def exec_query(self, query):
        if self.cnx is None:
            # Ensure the connection is created
            # if not already
            self.access_resource()

        result = self.cnx.exec_query(query)
        print(result)

        # Decrement reference count after
        # executing query
        self.release_resource()

        return result

    def release_resource(self):
        if self.ref_count > 0:
            self.ref_count -= 1
            print("Reference released...")
            print(f"{self.ref_count} remaining refs.")

        if self.ref_count == 0 and self.cnx is not None:
            self.cnx.close()
            self.cnx = None


if __name__ == "__main__":
    proxy = SmartProxy()
    proxy.exec_query("SELECT * FROM users")
    proxy.exec_query("UPDATE users SET name = 'John Doe' WHERE id = 1")
