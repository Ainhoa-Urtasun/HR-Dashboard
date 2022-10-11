from graphviz import Digraph
def Client():
  G = Digraph()
  G.node('Support',r'Finance (Unit 2)\nAccounting (Unit 4)\nManagement (Unit 5)')
  G.node('Core',r'Production (Unit 3)\nMarketing (Unit 6)')
  G.edge('Support','Primary')
