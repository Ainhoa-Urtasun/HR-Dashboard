pip install diagrams

def Client(Core):
  labels = {0:Core,1:'SUPPORT ACTIVITIES\nManagement\nHRM\nFinance\nAccounting'
  colors = {0:'grey',1:'gold'}
  shapes = {0:'o',1:'o'}
  client = [(1,0)]
  fig = plt.figure(figsize=(5,5))

