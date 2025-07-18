# tuple is immutable(we cannot modify the tuple)

abc=(1,9.3,"nick",["money",9,"ten",5.7])

#packing
# storing multiple values in a single container

ironman=("iron man","tony stark","Robert Downey Jr","brain and money",["captainamerica","Hulk","Spiderman"])
for i in ironman:
    print(i)

#unpacking
movie,charactername,actor,power,friends=ironman
print(movie,charactername,actor,power,friends)

#slicing
#getting/printing all the values

a=("cars","cash","crime","criminal","cookie","cake","controller")
print(a)
print(a[:])
print(a[0:])

print(a[0:7])
print(a[:7],a[:-1])

print(a[1:-1],a[1:6])

print(a[-6:-1],a[-6:6])

print(a[-1:1])




# tuple
a=(12,23,43,45)
b=[12,43,36,75]
print(a,b)
b=tuple(b)
print (b)
c=()
print (c)
# c.append(23)
print(a[-1])

# packing
addr=("hn 2","officer's accomodation","cgra","somnath","gj","india",362269)
print(addr)

# unpacking
h,line,place,city,state,country,pin=addr
print(h,line,place,city,state,country,pin)

abc=("alex",13,9.8,[9,8,9.3,9.9,10],{"addr":{"school":"abc","home":"xyz"}})
abc[3].append(20)
for i in abc[3]:
    abc[3].remove(i)
print(abc[3])

# if "alex" in abc:
#     print("yes")
# for i in abc:
#     print( i)