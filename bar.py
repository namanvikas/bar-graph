import matplotlib.pyplot as plt
import psutil as p
app_name_list=[]
cpupercentage_list=[]
count=0




for process in p.process_iter():
  count=count+1
  
  if count<=6:
      name=process.name()
      cpu_usage=p.cpu_percent()
      print("name:",name,"--","cpuusage:",cpu_usage)
      
      
      app_name_dict.update({name:cpu_usage})
      keymax=max(app_name_dict,key=app_name_dict.get)
      name_list=[keymax,keymin]
      app=app_name_dict.values()
      max_app=max(app)
      
plt.figure(figsize=(15,7))
plt.xlabel("application")
plt.ylabel("usage")
plt.bar(app_name_list,cpupercentage_list,width=0.6,color=("yellow","red","blue","green","orange","voilet"))
plt.show()