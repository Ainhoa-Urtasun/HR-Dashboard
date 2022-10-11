from graphviz import Digraph
G = Digraph()
G.node('Support',r'Finance\nAccounting\nManagement')
def Core(label):
  G.node('Core',label)
G.edge('Support','Primary')
