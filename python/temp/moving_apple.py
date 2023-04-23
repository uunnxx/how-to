# Read only region start
class UserMainCode:

    @classmethod
    def move_apple(cls, inp1: int, inp2: list) -> int:
        avg = sum(inp2) // inp1
        res = sum(abs(avg - inp2[i]) for i in range(inp1))
        return res // 2
