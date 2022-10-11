from graphviz import Digraph
G = Digraph()
G.node('Support',r'Finance\nAccounting\nManagement')
def Core(label):
  G.node('Core',label)
G.edge('Support','Core')


from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.onprem.database import PostgreSQL # Would typically use RDS from aws.database
from diagrams.onprem.inmemory import Redis # Would typically use ElastiCache from aws.database

with Diagram("Simple Website Diagram") as diag:
  dns = Route53("dns")
  load_balancer = ELB("Load Balancer")
  database = PostgreSQL("User Database")
  def CCore(label):
    cache = Redis(label)
  svc_group = [EC2("Webserver 1"),EC2("Webserver 2"),EC2("Webserver 3")]
