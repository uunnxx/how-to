class TV:
    def __init__(self):
        self.status = 'off'
        self.channel = 1
        self.volume = 40


    def __str__(self):
        return f"TV Status: {self.status}, channel: {self.channel}, volume: {self.volume}"



class TV1:
    def __init__(self):
        self._status = 'off'
        self._channel = 1
        self._volume = 40


    def __str__(self):
        return f"TV Status: {self._status}, channel: {self._channel}, volume: {self._volume}"


class TV2:
    def __init__(self):
        self.__status = 'off'
        self.__channel = 1
        self.__volume = 40


    def __str__(self):
        return f"TV Status: {self.__status}, channel: {self.__channel}, volume: {self.__volume}"





tv1 = TV2()

print(tv1)

print(tv1._TV2__channel)
