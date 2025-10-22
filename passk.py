import math

def pass_at_k(n, c, k):
    if c == 0:
        return 0.0
    if n - c < k:
        return 1.0
    return 1.0 - math.comb(n - c, k) / math.comb(n, k)

# Problem 1 example:
n = 5
c_llama = 3
c_chatgpt = 5

print("LLAMA  pass@1:", pass_at_k(n, c_llama, 1))
print("LLAMA  pass@5:", pass_at_k(n, c_llama, 5))
print("ChatGPT pass@1:", pass_at_k(n, c_chatgpt, 1))
print("ChatGPT pass@5:", pass_at_k(n, c_chatgpt, 5))
