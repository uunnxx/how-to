# Read only region start
class UserMainCode:

    @classmethod
    def move_apple(cls, inp1: int, inp2: list) -> int:
        avg = sum(inp2) // inp1
        res = 0
        for i in range(inp1):
            res += abs(avg - inp2[i])

        return res // 2
