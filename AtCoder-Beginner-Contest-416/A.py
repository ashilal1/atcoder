n, l, r = map(int, input().split())
strings = input()

checkList = strings[l - 1:r] # 問題での数の数え方が１からになってるっぽい

# print(checkList)

if 'x' in checkList:
    print("No")
else:
    print("Yes")    

