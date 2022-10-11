from graphviz import Digraph
G = Digraph()
G.node('Support',r'Finance\nAccounting\nManagement')
def Core(label):
  G.node('Core',label)
G.edge('Support','Core')


from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
  
with Diagram("Simple Website Diagram") as ddd:
  svc_group = [EC2(label),EC2(label),EC2("Webserver 3")]
