wealth = 0
for row in accounts:
    wealth = max(sum(row), wealth)
return wealth