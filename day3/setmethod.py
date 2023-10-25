#sets and set methods
a={2,3,4,5}
b={4,5,6,7}
c=a.union(b)
print(c)
a.update(b)
print(a)

fruits={'apple','banana','mango','carrot'}
vegetables={'carrot','mushroom','beans','pumpkin'}

print(fruits)
print("union ",fruits.union(vegetables))
print("intersection",fruits.intersection(vegetables))
print("symmetric difference",fruits.symmetric_difference(vegetables))
print("difference",fruits.difference(vegetables))
print(fruits.isdisjoint(vegetables))
fruits.remove('mango')
print(fruits)

item=vegetables.pop()
print("Vegetables",vegetables)
print("Pop item is ",item)