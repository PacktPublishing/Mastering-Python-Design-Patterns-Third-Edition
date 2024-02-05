from abc import ABC, abstractmethod


class RemoteServiceInterface(ABC):
    @abstractmethod
    def read_file(self, file_name):
        pass

    @abstractmethod
    def write_file(self, file_name, contents):
        pass

    @abstractmethod
    def delete_file(self, file_name):
        pass


class RemoteService(RemoteServiceInterface):
    def read_file(self, file_name):
        # Implementation for reading a file from the server
        return "Reading file from remote server"

    def write_file(self, file_name, contents):
        # Implementation for writing to a file on the server
        return "Writing to file on remote server"

    def delete_file(self, file_name):
        # Implementation for deleting a file from the server
        return "Deleting file from remote server"


class ProxyService(RemoteServiceInterface):
    def __init__(self):
        self.remote_service = RemoteService()

    def read_file(self, file_name):
        print("Proxy: Forwarding read request to RemoteService")
        return self.remote_service.read_file(file_name)

    def write_file(self, file_name, contents):
        print("Proxy: Forwarding write request to RemoteService")
        return self.remote_service.write_file(file_name, contents)

    def delete_file(self, file_name):
        print("Proxy: Forwarding delete request to RemoteService")
        return self.remote_service.delete_file(file_name)


if __name__ == "__main__":
    proxy = ProxyService()
    print(proxy.read_file("example.txt"))
