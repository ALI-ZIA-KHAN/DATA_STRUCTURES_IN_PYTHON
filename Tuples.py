#tuples are immutable
tuple1=()
tup2=(0,1,2,3,4)
tup3=("APPLE","BANANA","ORANGE")
tup4=tup2+tup3
print(tup4)
tup5=tup2,tup3
print(tup5)

# a way to make change in tuples
x=tup3

y=list(x)
y[1]="kiwi"
m=tuple(y)
print(m)


