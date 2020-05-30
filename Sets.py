#sets are immutable
set1={"apple","banana","mango"}
set1.add("grapes")
print(set1)
set1.update(["apple","orange","falsa"])
print(set1)
#operations on sets
s1={1,2,3,4,5}
s2={5,6,7,8,9}
s3=s1.union(s2)
print(s3)
s4=s1.intersection(s2)
print(s4)
s5=s1.difference(s2)
print(s5)