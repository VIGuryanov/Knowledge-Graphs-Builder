from Environment import Environment
from lib.standard_predicates import StandardPredicates

class DBModelBase:
    table_name = ''    

    def get_insert_values() -> dict:
        pass
    def get_update_values(self) -> dict:
        pass

class GraphModelBase(DBModelBase):
    graph_entity_type = None

    def get_insert_values(self) -> dict:
        res = {}
        if self.id != 0:
            res['Id'] = self.id
        if self.iri is None:
            res['iri'] = ''
        else:
            res['iri'] = self.iri
        return res

    def get_update_values(self) -> dict:
        res = {}
        res['iri'] = self.iri
        return res
    
    def refresh_iri(self):
        pass

class Entities(GraphModelBase):
    table_name = 'Entities'
    graph_entity_type = StandardPredicates._entity

    def __init__(self, id = 0, iri = None):
        self.id = id
        self.iri = iri
        # if iri is None:
            
        # else:
        #     self.iri = iri
    
    def refresh_iri(self):
        if self.iri is None and self.id != 0:
            self.iri = f'{Environment.domain}/entities#{self.id}'

class Predicates(GraphModelBase):
    table_name = 'Predicates'
    graph_entity_type = StandardPredicates._predicate

    def __init__(self, id = 0, iri = None):
        self.id = id
        self.iri = iri
        # if iri is None:
        #     self.iri = f'{Environment.domain}/predicates#{id}'
        # else:
        #     self.iri = iri

    def refresh_iri(self):
        if self.iri is None and self.id != 0:
            self.iri = f'{Environment.domain}/predicates#{self.id}'