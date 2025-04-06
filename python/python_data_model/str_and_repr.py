class Taco:
    def __init__(self, shell, protein, toppings=[]):
        self.shell = shell
        self.protein = protein
        self.toppings = toppings

    def __str__(self):
        ...

    def __repr__(self):
        toppings = (f' with {", ".join(self.toppings)}') if self.toppings else ''

        return (f'{self.shell}shell {self.protein} taco {toppings} @ {id(self)}')


t1 = Taco('hard', 'chicken')
t2 = Taco('soft', 'tofu', toppings=['chees', 'lettuce', 'sour cream'])
