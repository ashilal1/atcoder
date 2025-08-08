n, a, b = map(int, input().split())
string = input()

# print(f"{string}")
# print(f"{string.slice(3)}")

# print(string[a:b])
print(string[slice(a, b + 1)]) # この書き方は間違い
# print(string[slice(a, b)])

# この問題は末尾から文字列を取り出したい。

print(string[slice(a, n - b)])
# or
print(string[a:n-b])