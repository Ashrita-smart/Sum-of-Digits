def digitsum(count,n):
    if n==0:
        return 0
    if n==1:
        return 1
    if count==0:
        return 0
    if count==1:
        return 1
    return digitsum(count+n)
print(digitsum(0,int(input("Enetr the number"))))