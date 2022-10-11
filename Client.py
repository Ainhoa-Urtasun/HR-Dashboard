from graphviz import Digraph
def Client(description):
  G = Digraph()
  G.node('Support',r'Finance\nAccounting\nManagement')
  G.node('Core',description)
  G.edge('Support','Primary')
