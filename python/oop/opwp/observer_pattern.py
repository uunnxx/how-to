class Subject:
    def __init__(self) -> None:
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class Observer:
    def update(self, subject):
        pass


class ConcreteObserverA(Observer):
    def update(self, subject):
        print("ConcreteObserverA received the update.")


class ConcreteObserverB(Observer):
    def update(self, subject):
        print("ConcreteObserverB received the update.")


subject = ConcreteSubject()
observer1 = ConcreteObserverB()
observer2 = ConcreteObserverA()
subject.attach(observer1)
subject.attach(observer2)
subject.state = 123
