class Solution:

  def myAtoi(self, s: str) -> int:
    # Define 32-bit signed integer limits
    INT_MAX = 2**31 - 1
    INT_MIN = -(2**31)

    # 1. Strip leading whitespaces
    s = s.lstrip()

    if not s:
      return 0

    sign = 1
    index = 0

    # 2. Check optional sign
    if s[0] == "-":
      sign = -1
      index += 1
    elif s[0] == "+":
      index += 1

    result = 0

    # 3. Read valid digit characters
    while index < len(s) and s[index].isdigit():
      digit = int(s[index])

      # 4. Handle overflow/underflow clamping
      if result > (INT_MAX - digit) // 10:
        return INT_MAX if sign == 1 else INT_MIN

      result = result * 10 + digit
      index += 1

    return sign * result