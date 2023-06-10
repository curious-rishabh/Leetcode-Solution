counter = 1
missing = []

while len(missing) < k:
    if counter not in arr:
        missing.append(counter)
    
    counter += 1

return missing.pop() 