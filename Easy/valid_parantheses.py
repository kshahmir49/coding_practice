input = "(({})){}[]"
lst = [0]
for i in input:
    if (lst[-1] == "(" and i==")") or (lst[-1] == "[" and i=="]") or (lst[-1] == "{" and i=="}"):
        lst.pop()
    else:
        lst.append(i)

if len(lst) == 1:
    print("Valid parantheses")
else:
    print("Not valid")