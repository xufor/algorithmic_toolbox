n, W = map(int, input().split())
value_weight_list = [[x for x in map(int, input().split())] for i in range(n)]
value_weight_list = [[v, w, v/w] for [v, w] in value_weight_list]
value_weight_list.sort(key=lambda l: l[2], reverse=True)
final_value = 0
for v, w, v_per_w in value_weight_list:
    amount = min(W, w)
    W -= amount
    final_value += amount * v_per_w
print(final_value)