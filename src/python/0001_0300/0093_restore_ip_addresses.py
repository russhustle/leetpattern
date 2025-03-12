from typing import List


def restoreIpAddresses(s: str) -> List[str]:
    result = []

    def backtracking(start_index, point_num, current, result):
        # stop condition
        if point_num == 3:
            if is_valid(s, start_index, len(s) - 1):
                current += s[start_index:]
                result.append(current)
            return

        for i in range(start_index, len(s)):
            if is_valid(s, start_index, i):
                sub = s[start_index : i + 1]
                backtracking(i + 1, point_num + 1, current + sub + ".", result)
            else:
                break

    def is_valid(s, start, end):
        if start > end:
            return False

        if s[start] == "0" and start != end:
            return False

        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True

    backtracking(0, 0, "", result)

    return result


print(restoreIpAddresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']
