class Service:
    def __init__(self, repository):
        self.repository = repository

    def vote(self, kandidat, suara):
        candidate = self.repository.find_candidate(kandidat)
        if len(candidate) > 0:
            self.repository.update_suara(kandidat, suara)
        else:
            self.repository.insert_kandidat(kandidat, suara)

    def get_table_from_db(self, drop):
        if not drop:
            return self.repository.get_table()
        else:
            return self.repository.get_new_table()
