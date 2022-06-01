# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

n = int(input())
arr = list(map(int, input().split()))
z=max(arr)
while max(arr)==z:
    arr.remove(max(arr))
c=max(arr)
print(c)


#  input
# 5
# 2 3 6 6 5
#  output
# 5
