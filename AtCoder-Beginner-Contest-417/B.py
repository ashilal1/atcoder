# n, m = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# for i in B:
#     for j in A:
#         # if B[i] == A[j]: これだとB、Aに入っている要素自体が入っていることになっちゃう
#         if i == j:
#             A.remove(j)
#         else:
#             break
            
# print(A)

# # remove() メソッド : 指定した 値 をリストから削除
# # pop() メソッド : 指定したインデックス の要素を削除


n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for value_b in B:
    if value_b in A:
        A.pop(value_b)

print(*A) # 空白区切りで出力
