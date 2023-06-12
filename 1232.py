coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

# Line should have same slope
# y2-y1 / x2-x1 == y3-y2 / x3-x2

x_diff = coordinates[1][0] - coordinates[0][0]
y_diff = coordinates[1][1] - coordinates[0][1]

current_x_diff = 0
current_y_diff = 0

for i in range(2,len(coordinates)):
    current_x_diff = coordinates[i][0] - coordinates[i-1][0]
    current_y_diff = coordinates[i][1] - coordinates[1][i-1]
    
    if y_diff * current_x_diff != x_diff * current_y_diff:
        return False
return True
    
