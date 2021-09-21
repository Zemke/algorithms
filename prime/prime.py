primes = [2, 3, 5, 7, 11, 13, 17, 19,
          23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79,
          83, 89, 97]
DP_prime = dict(enumerate([ (i in primes) for i in range(0, 101) ]))


def prime(n):
  """
  Dynamic programming prime.
  """
  if n in DP_prime:
    return DP_prime[n]
  for i in range(2, n):
    if n % i == 0:
      DP_prime[n] = False
      return DP_prime[n]
  DP_prime[n] = True
  return DP_prime[n]

