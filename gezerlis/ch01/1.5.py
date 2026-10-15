names = ["Alice", "Bob", "Eve"]
target = input()

#1.5a (no forelse)
if target in names:
    print(target)
else:
    print(None)
    
#1.5b (returning the index)
for i, name in enumerate(names):
    if name == target:
        print(i, name)
        break
else:
    print(None)
    
#1.5c (making shorter)
def look_1(target, names): #first variant
    idx, val = None, None
    for i, name in enumerate(names):
        if name == target:
            idx, val = i, name
            break
    return idx, val
    
def look_2(target, names): #second variant
    for i, name in enumerate(names):
        if name == target:
            return i, name
    return None, None

#1.5d 
def look_3(target, names):
    for i, name in enumerate(names):
        if name == target:
            break
    else:
        raise ValueError(target, "not found in list")
    return i, name

print(look_1(target, names))
print(look_2(target, names))
print(look_2(target, names))