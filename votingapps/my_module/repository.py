import sqlite3
from sqlite3 import Error
from my_module.candidate_dto import CandidateDto


class Repository:
    def __init__(self):
        db_file = r"C:\votingapps\my_module\maju_mundur"
        self.conn = self.create_connection(db_file)
        if self.conn is not None:
            self.cursor = self.conn.cursor()

    def create_connection(self, db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn

        except Error as e:
            print(e)

        return conn

    def update_suara(self, kandidat, jumlah):
        sql_update_suara = f'''
        UPDATE hasil_vote
            SET jumlah_suara = (jumlah_suara+?) 
        WHERE nama_kandidat = ?'''

        returned_dto = []
        self.cursor.execute(sql_update_suara, (jumlah, kandidat,))
        rows = self.cursor.fetchall()
        for name, count in rows:
            dto = CandidateDto(name, count)
            returned_dto.append(dto)
        self.conn.commit()
        return returned_dto

    def insert_kandidat(self, nama_kandidat, suara):
        sql_insert_kandidat = f'''
        INSERT into hasil_vote
            (nama_kandidat,jumlah_suara)
        VALUES(?,?)'''
        returned_dto = []
        self.cursor.execute(sql_insert_kandidat, (nama_kandidat, suara,))
        rows = self.cursor.fetchall()
        for name, count in rows:
            dto = CandidateDto(name, count)
            returned_dto.append(dto)
        self.conn.commit()
        return returned_dto

    def get_table(self):
        sql_get_table = f'''
        SELECT *
        FROM hasil_vote
        ORDER BY jumlah_suara
        DESC'''
        returned_dto = []
        self.cursor.execute(sql_get_table)
        rows = self.cursor.fetchall()
        for name, count in rows:
            dto = CandidateDto(name, count)
            returned_dto.append(dto)
        self.conn.commit()
        return returned_dto

    def get_new_table(self):
        sql_get_new_table = f'''
        DELETE 
            FROM hasil_vote'''
        returned_dto = []
        self.cursor.execute(sql_get_new_table)
        rows = self.cursor.fetchall()
        for name, count in rows:
            dto = CandidateDto(name, count)
            returned_dto.append(dto)
        self.conn.commit()
        return returned_dto

    def find_candidate(self, name):
        sql_find_candidate = f'''
        SELECT nama_kandidat
        FROM hasil_vote
        WHERE hasil_vote.nama_kandidat = ?'''
        self.cursor.execute(sql_find_candidate, (name,))
        rows = self.cursor.fetchall()
        return rows
