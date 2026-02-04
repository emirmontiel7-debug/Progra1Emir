class Animales:
    def __init__(self, nombre, color, patas):
        self.nombre=nombre
        self.color=color
        self.patas=patas

    def sonido(self):
        print("sonido generico")

class Conejo(Animales):
    def sonido2(self):
        print("snif snif")
    def carac(self):
        print(f"Mi conejo se llama {self.nombre}, es color {self.color} y tiene {self.patas} patas")

class Ornitorrinco(Animales):
    def __init__(self, pico):
        self.pico=pico
    def sonido3():
        print("grrrr")
    def caracte():
        print(f"Mi ornito se llama {}")
    
    