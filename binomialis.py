def binom (N, K):
    if int(K) == 0 or int(K) == int(N):
        return 1
    else:
        return binom(int(N) - 1, int(K) - 1) + binom(int(N) - 1, K)


N = 5
K = 2
print(binom(N , K)) 

