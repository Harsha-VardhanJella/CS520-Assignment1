from math import comb

def pass_at_k(n, c, k):
    if c == 0: 
        return 0.0
    k = min(k, n)
    return 1 - comb(n - c, k) / comb(n, k)

print("LLaMA:", [pass_at_k(5, 4, k) for k in (1,2,3)])
print("ChatGPT:", [pass_at_k(5, 2, k) for k in (1,2,3)])
