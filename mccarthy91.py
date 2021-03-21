def beolvasas():
  return int(input())

def mccarthy(n):
    if n > 100:
        M = n - 10 
    else:
        M = mccarthy(mccarthy(n+11))
    return M

M = mccarthy(1)

print(mccarthy(3))