from my_module.gui import UI
from my_module.repository import Repository
from my_module.service import Service


class Container:
    def __init__(self):
        self.db = self.create_repository()
        self.service = self.create_service()
        self.gui = self.create_ui()

    def create_ui(self):
        return UI(self.service)

    def create_service(self):
        return Service(self.db)

    def create_repository(self):
        return Repository()

    def run(self):
        self.gui.run()
