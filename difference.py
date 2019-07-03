list1=[10,15,20,25,30,35,40]
list2=[25,40,35]
##l3=list(set(list1)-set(list2))
##
l3=[i for i in list1 + list2 if i not in list1 or i not in list2]
print(l3)
