import sqlalchemy as db

class VirtuosoSQL:
    def __init__(self, login, password):#, autocommit = False):
        self.engine = db.create_engine(f'virtuoso+pyodbc://{login}:{password}@VOS')
        self.metadata = db.MetaData()
        self.connection = self.engine.connect()

    def insert(self, table:str, values:dict) -> int:
        query = db.insert(db.Table(table, self.metadata, autoload_with=self.engine)).values(values)
        result = self.connection.execute(query).inserted_primary_key

        return result[0]
    
    def update(self, table:str, id, values:dict):
        table = db.Table(table, self.metadata, autoload_with=self.engine)
        query = db.update(table).where(table.c.Id == id).values(values)

        result = self.connection.execute(query)

    
    def find_by_id(self, table:str, id:int):
        db_table = db.Table(table, self.metadata, autoload_with=self.engine)
        query = db.select(db_table).where(db_table.c.Id == id)
        result = self.connection.execute(query).fetchall()
        
        return result
    
    def find_by_field(self, table:str, field_name:str, field_value):
        db_table = db.Table(table, self.metadata, autoload_with=self.engine)
        query = db.select(db_table).where(getattr(db_table.c, field_name) == field_value)
        result = self.connection.execute(query).fetchall()
        
        return result
    
    def commit(self):
        self.connection.commit()
        