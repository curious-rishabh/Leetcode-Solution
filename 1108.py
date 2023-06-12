# A defanged IP address replaces every period "." with "[.]"

address = "1.1.1.1"

add = address.replace('.', '[.]')

print(add)