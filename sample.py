class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # time:O(n)
        # space:O(1)
        MAX = pow(2, 31) - 1
        MIN = -pow(2, 31)
        result = ""
        if len(str) == 0:
            return 0
        for i in range(len(str)):
            if str[i] == ' ':
                continue
            if str[i] == '+' or str[i] == '-':
                result = result + str[i]
                break
            if '0' <= str[i] <= '9':
                result = result + str[i]
                break
            else:
                return 0
        for j in range(i + 1, len(str)):
            if '0' <= str[j] <= '9':
                result = result + str[j]
                # print(result)
            else:
                break
        if len(result) == 0 or result == "+" or result == "-":
            return 0
        else:
            result_i = int(result)
        # print(result_i)
        if MIN <= result_i <= MAX:
            return result_i
        elif result_i > 0:
            return MAX
        else:
            return MIN
