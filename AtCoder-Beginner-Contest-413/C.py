# n = int(input())
# A = []

# for i in range(n):
#     query = map(int, input().split()) # ここに入るのはmapオブジェクト
#     # if query == 1:
#     if list(query) == 1: # 値を使うにはlistにする必要がある
#         inputNum, howMany = map(int, input().split())
#         for j in range(howMany):
#             # A.add(inputNum)
#             A.append(inputNum)
#     else:
#         deleteNum = map(int, input().split())
#         deleteNum = list(deleteNum)
#         B = A[0:deleteNum]
#         print(sum(B))

""" 
この問題では制約（特に c や k が非常に大きくなること）から、単純にリストへ要素を追加・削除する方法では
時間切れになってしまうことを気づくべき。

map関数、mapオブジェクトの解説

・map関数は、第一引数の関数を第二引数以降の要素に適用する関数
・map関数は、mapオブジェクトと呼ばれるイテレータを返す。
    mapオブジェクトは、メモリ容量の効率化のため「どの関数をどの要素に適用するか」という情報のみを保持しており、いわば「計算の指示」を保持している
    
https://zenn.dev/yuto_mo/articles/d8ece3e443c557


append
appendはリスト(list)型のメソッドです。リストの末尾に一つの要素を追加します。

対象: list

動作: 引数に指定した要素をそのままリストの末尾に追加します。


add
addはセット(set)型のメソッドです。セットに一つの要素を追加します。セットは重複する要素を許容しないため、既に同じ要素が存在する場合は何も起こりません。

対象: set

動作: 引数に指定した要素をセットに追加します。重複する要素は追加されません。 

"""

# 正解例

"""
cが10億個もあるから普通にif分だとダメ。
→「どの数字(value)が、何個(count)あるか」というペアで管理する。
例えば、数列 A が (3, 3, 5, 5, 5, 5) のとき、これを普通のリストで持つのではなく
[ [3, 2], [5, 4] ]
のように、「3が2個の塊、その次に5が4個の塊」として管理する

collections.deque を使う。dequeは、リストの末尾への追加（append）と、先頭からの削除（popleft）がとても高速。
"""

from collections import deque

Q = int(input())
A = deque()

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        x = query[2]
        A.append([x, c]) # 何が何個あるかをここで管理する
        # Aの１つの要素が[x, c]で埋まる。A[0] = x, A[1] = cではない。
        # A[0] = [x, c]
    else:
        # 先頭 k 個の要素を削除し、合計を出力する 
        k = query[1]
        sum = 0
        # まだ削除すべき要素が残っている間ループを続ける
        while k > 0:
            value, count = A[0] # 1回目のループ: value=3, count=2
            if count > k: # 先頭の塊の一部だけを削除する場合 
            # 例：k=1, 先頭の塊が [5, 4] の場合。count(4) > k(1) なのでこっちが実行される
                sum += value * k 
                A[0][1] -= k # [5, 4] の個数を1減らして [5, 3] に更新
                k = 0 # # 削除したい個数が残り0になったので、ループを終了させる
            else: # 先頭の塊を丸ごと削除する場合
            # 例：k=3, 先頭の塊が [3, 2] の場合。count(2) <= k(3) だからこっちが実行される
                sum += value * count # total_sum に 3 * 2 を加算
                k -= count # 残り削除したい個数kを更新 (k = 3 - 2 = 1)
                A.popleft() # [3, 2] の塊は全て使い切ったので、dequeから完全に取り除く

        print(sum)