import math
import pandas as pd 
import matplotlib.pyplot as plt
import time

load=pd.read_excel("co.xlsx")
load.columns=["Name","Salary","Rating","Choice"]

l=[]

dic={"Name":load["Name"],
     "Salary":load["Salary"],
     "Rating":load["Rating"],
     "Choice":load["Choice"],
     "Distance":l
     }

# k=3
# ip1=4
# ip2=18000
k=int(input("Enter the value of k: "))
ip1=float(input("Enter the rating: "))
ip2=int(input("Enter the salary: "))

for j in range(0,len(dic["Name"])):
    sol=math.sqrt((ip1-dic["Rating"][j])**2 +(ip2-dic["Salary"][j])**2)
    l.append(sol)

new_df=(pd.DataFrame(dic))
new_df["Rank"]=new_df["Distance"].rank(ascending=True)
new_df.sort_values('Rank',inplace=True)


filter_df=new_df.head(k)

sol=max(set(filter_df["Choice"]))

c1=sol.count("Yes")
c2=sol.count("No")

if sol=="Yes":
    print("The customer will buy the product/service")
elif sol=="No":
    print("The customer will not buy the product/service")
elif c1==c2:
    print("The customer will buy the product/service")


def plotter():
    yes=load[load["Choice"]=="Yes"]
    no=load[load["Choice"]=="No"]

    plt.scatter(yes["Rating"],yes["Salary"],color="green",label="Yes")
    plt.scatter(no["Rating"],no["Salary"],color="red",label="No")
    plt.scatter(ip1,ip2,color="blue",label="Input")
    

    plt.xlabel("Rating")
    plt.ylabel("Salary")
    plt.title("Customer Classification")
    plt.legend()
    plt.show()
    
time.sleep(5)    
plotter()
