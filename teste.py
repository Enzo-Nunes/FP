def espelho(n):
    def aux(n, res):
        if n == 0:
            return res
        else:
            res += (n % 10) * (10 ** (len(str(n)) - 1))
            return res + aux(n//10, res)
    return aux(n, 0)

print(espelho(123))