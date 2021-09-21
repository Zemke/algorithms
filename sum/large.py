s = """12384971234702134798569023694213498723
90078071823476872134021783490721903474"""


# Sum equally large sums
# https://www.geeksforgeeks.org/sum-two-large-numbers/


ss = [i[::-1] for i in s.split('\n')]
str_res = ''
carry = 0
for i in range(len(ss[0])):
  sum_ss = 0
  for s in ss:
    n = s[i]
    sum_ss += int(n)
  sum_ss += carry
  str_res += str(sum_ss % 10)
  carry = sum_ss // 10
if carry:
  str_res += str(carry)


print(str_res[::-1])

