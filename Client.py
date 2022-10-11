from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram('Client', show=False) as flow:
    ELB("Support") >> EC2("Core")
def explain(label):
    print(label)
