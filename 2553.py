nums = [13,25,83,77]
answer = []
string = ""
# convert into string
for i in nums:
    string += f"{i}"
# appending one value at a time
for i in string:
    answer.append(int(i))

return answer