title = "First leTTeR of EACH Word"

ans = []

ans = title.split()
for i in range(len(ans)):
    if len(ans[i]) == 1 or len(ans[i]) == 2:
        ans[i] = ans[i].lower()
        continue
    ans[i]= ans[i].title()
# return " ".join(ans)
print(" ".join(ans))