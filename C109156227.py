import os
#print(os.getcwd())

fp=open("test2.csv","r")
tmp=fp.readline()
#print(tmp)
class Student:
    def __init__(self,cls,id,name,git):
        self.cls=cls
        self.id=id
        self.name=name
        self.git=git

aaaa=[]
while tmp !="":
    tmp=fp.readline()
    if tmp =="":
        continue
    tmp1=tmp.replace("?"," ").split(",")
    tmp1[3]=tmp1[3].replace("\n"," ")
    tmp2=Student(tmp1[0], tmp1[1], tmp1[2], tmp1[3]) 
    aaaa.append(tmp2)
 
fp.close()
for i in range(len(aaaa)): 
    print(aaaa[i].cls,aaaa[i].id,aaaa[i].name,aaaa[i].git)