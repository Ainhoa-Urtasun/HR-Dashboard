from graphviz import Digraph
G = Digraph()
G.node('Support',r'Finance (Unit 2)\nAccounting (Unit 4)\nManagement (Unit 5)')
G.node('Primary',r'Production (Unit 3)\nMarketing (Unit 6)')
G.edge('Support','Primary')
G
