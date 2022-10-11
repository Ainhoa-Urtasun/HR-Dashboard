from graphviz import Digraph
G = Digraph()
G.node('Support',r'Finance\nAccounting\nManagement')
def Core(label):
  G.node('Core',label)
G.edge('Support','Core')


from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Making shoes", show=False) as flow:
    ELB("Support") >> EC2("Core")
