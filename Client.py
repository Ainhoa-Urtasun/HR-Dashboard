import matplotlib.pyplot as plt
from netgraph import Graph

def Client(Core):
  labels = {0:Core,1:'SUPPORT ACTIVITIES\nManagement\nHRM\nFinance\nAccounting'}
  colors = {0:'grey',1:'gold'}
  shapes = {0:'o',1:'o'}
  client = [(1,0)]
  fig = plt.figure(figsize=(5,5))
  Graph(client,node_size=30,node_labels=labels,node_color=colors,node_shape=shapes,node_edge_width=2,edge_width=2,arrows=True)
