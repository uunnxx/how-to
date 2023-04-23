class Sotrudniki:
    def __init__(sotrudnik, imya, familiya):
        sotrudnik.imya = imya
        sotrudnik.familiya = familiya

    def kto_eto(sotrudnik):
        print(f"{sotrudnik.imya} {sotrudnik.familiya}")


rabotnik1 = Sotrudniki('Andrey', 'Zorin')
rabotnik1.kto_eto()
