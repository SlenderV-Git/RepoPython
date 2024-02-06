import sqlite3

class Database():
    def __init__(self, db_file) -> None:
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        
    def execute_query(self, *query):
        self.cursor.execute(*query)
        self.conn.commit()
    
    def execute_query_result(self, *query):
        self.cursor.execute(*query)
        return self.cursor.fetchall()