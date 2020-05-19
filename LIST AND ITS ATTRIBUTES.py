#lists
##single list can have multiple datatypes
alist=["1","2",3,4,5,["pak","eng"],True,("hello","world")]
print(alist)

##append():can add any one element to last index
list_1=["khi","lhr","quta","isl","pshwr"]
list_1.append("gwdr")
print(list_1)
#exetnd():can add multiple items in a list ata time
list_1.extend(["fsl","mult","hyd"])
print(list_1)
#sort(): arrange in alphabetical order
list_1.sort()
print(list_1)
#sort(reverese=true) :arranges in alpha order (reverse)
list_1.sort(reverse=True)
print(list_1)
#.pop(): deletes last item of list
a=list_1.pop()
print(a)
#deletes  element at a particular index
del list_1[4]
print(list_1)
#index(): gives index of particular element
print(list_1.index("lhr"))
#max() gives maximum of the list
print(max(list_1))
#pops 2nd index element of list
print(list_1.pop(2))
#checking something
if "pshwr" in list_1:
    print("true")
#count(): counting occourrences of particular elements
print(list_1.count("lhr"))
#insert(ind,elem) inserts at given position
list_1.insert(4,"pakistan")
print(list_1)
#remove(): removes any particular element
list_1.remove("lhr")
print(list_1)
#to iterate  in list
for i in list_1:
 print(f"THE CITIES ARE: {i}")
for i in list_1:
 print("THE CITIES ARE:",i)
#to have all iterated elemrnts also in a list
lab=[]
for i in list_1:
    lab.append(i)
print(lab)
