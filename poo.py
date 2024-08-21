class Montadora:
    def __init__(self, p1,p2,p3,p4,p5): # Metudo construtor 
        self.cor = p1
        self.qtdPassageiros = p2
        self.tipocombustivel = p3
        self.velocidadde = p4
        self.litros = p5

objeto_1 = Montadora("Branca",5,"flex",160,42) # Estou intaciando um objeto!

objeto_2 = Montadora("Preta",6,"disel",200,60) # Quando vc instancia um objeto, o metudo costrutor da class é chamado caso exista 


print(objeto_1.cor, objeto_2.litros)