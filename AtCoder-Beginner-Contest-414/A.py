# listener, startTime, endTime = map(int, input().split())
# deliveryTime = endTime - startTime
# listenerCount = 0

# while 1:
#     a, b = map(int, input().split())
#     time = b - a
#     if a < startTime & time >= deliveryTime & endTime < b:
#         listenerCount += 1
#     else:
#         break

# print(listenerCount)





# 高橋君の配信時間全体が、各リスナーの視聴可能時間の中に完全に含まれているリスナーの数を数えることが目的
N, L, R = map(int, input().split())

listenerCount = 0

for _ in range(N): # 「N 回繰り返す」という回数だけが重要で、「今が何回目の繰り返しなのか」というインデックス自体は使わない場合いに「_」を使う
    a, b = map(int, input().split())

    if a <= L and R <= b: # & じゃなくて and
        listenerCount += 1

print(listenerCount)
