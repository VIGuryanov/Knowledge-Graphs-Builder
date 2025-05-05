from lib.triple import Triple
import networkx as nx
import matplotlib.pyplot as plt
import copy
from lib.standard_predicates import StandardPredicates

class DrawGraph:

    def __init__(self):
        self.graph = nx.DiGraph()

    def replace_with_labels(self, data: list[Triple]):
        data = copy.deepcopy(data)

        labels = {}
        for triple in data:
            if triple.predicate.value == StandardPredicates._label or triple.predicate.value == 'http://xmlns.com/foaf/0.1/name':
                labels[triple.subject.value] = triple.object.value

        data = [a for a in data if a.predicate.value != StandardPredicates._label and a.predicate.value != 'http://xmlns.com/foaf/0.1/name']
        
        for triple in data:
            if triple.subject.value in labels:
                triple.subject.value = labels[triple.subject.value]
            
            if triple.object.value in labels:
                triple.object.value = labels[triple.object.value]

            if triple.predicate.value in labels:
                triple.predicate.value = labels[triple.predicate.value]
        
        return data

    def graph_add(self, data: list[Triple], labels_instead_iri = False):

        if labels_instead_iri:
            data = self.replace_with_labels(data)

        for tr in data:
            self.graph.add_edge(tr.subject.value, tr.object.value, val = tr.predicate.value)
    
    def draw_graph(self, size = 300, output_path = 'graph.png'):
        plt.figure(figsize=(size, size))
        pos = nx.fruchterman_reingold_layout(self.graph)
        nx.draw_networkx(self.graph, pos, with_labels=True)
        labels = nx.get_edge_attributes(self.graph, 'val')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.savefig(output_path)