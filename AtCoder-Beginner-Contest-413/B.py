# n = int(input())
# count = 0
# A = []

# for i in range(n):
#     A[i] = input()



# 正解コード
N = int(input())

S = [input() for i in range(N)]
# N 回ループを繰り返し、1行ずつ文字列を読み取る
# 読み取った N 個の文字列を S という名前のリストに格納
# 例えば、N が 4 なら、4つの文字列がリスト S に格納される


# 連結した文字列を格納する「セット」を用意
ans = set()
# set （セット）は「重複する値を持たない」という性質を持つ特殊な入れ物。
# ここに連結後の文字列を入れていくことで、同じ文字列が複数回できても自動的に1つとして扱ってくれえう。

for s in S:
    for t in S:
        if s != t: # 異なる 2 つの文字列を
            ans.add(s + t) # 連結して追加

# set の大きさが答え
print(len(ans))
