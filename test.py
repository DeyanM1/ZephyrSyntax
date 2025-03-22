from mpmath import mp, mpf, sqrt, factorial

def chudnovsky_pi(digits):
    mp.dps = digits  # Set precision (decimal places)
    C = mpf(426880) * sqrt(mpf(10005))
    K, M, X, S = mpf(6), mpf(1), mpf(1), mpf(13591409)

    for k in range(1, digits // 14):  # Each term adds ~14 digits
        M *= mpf((12*k - 6) * (12*k - 4) * (12*k - 2)) / mpf(k**3)
        K += 12
        X *= -mpf(640320**3)
        S += M * K / X

    return C / S

# Compute π to 10,000 decimal places
pi_10000 = chudnovsky_pi(99999)
print(pi_10000)
