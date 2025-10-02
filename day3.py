my_dict={"name":"sylvia", "age":29,"tribe":"kikuyu"}
print(my_dict)

backup=my_dict.copy()
print(backup)

keys=["name","age","city"]
values="unknown"
default=dict.fromkeys(keys,values)
print(default)

getting=backup.get("age")
print(getting)

key1=backup.keys()
print(key1)

value1=my_dict.values()
print(value1)

all_items=backup.items()
print(all_items)

popping=backup.pop("tribe")
print(popping)

print(backup)

pop_item=my_dict.popitem()
print(pop_item)
print(my_dict)

new_dict={"name":"dylon", "country":"kenya"}
setdefault=new_dict.setdefault("name", "Mjaka")#ignored as name key already has avalue
print(setdefault)

#update
updating=my_dict.update(new_dict)#we updated the old dict here
print(my_dict)

#merging the keys with values
new_keys=["school","gender","class"]
new_values=["Barani","Male",8]
complete_dict=dict(zip(new_keys,new_values))
print(complete_dict)





