class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.salud = 5
        self.alimentacion = 5
        self.felicidad = 8
        
    def __str__(self):
        return f"{self.nombre} >> Estado Actual >> Alimentación: {self.alimentacion}/10 | Felicidad: {self.felicidad}/10 | Salud: {self.salud}/10"
    
    def alimentar(self):
        print (f"Estás alimentando a {self.nombre} ... (๑ᵔ⤙ᵔ๑)")
        self.alimentacion += 3
        if self.alimentacion >10:
            self.alimentacion =10
        self.salud +=1
        if self.salud >10:
            self.salud =10
        self.felicidad += 1
        if self.felicidad >10:
            self.felicidad = 10
            
    def jugar(self):
        print(f"Estás jugando con {self.nombre} ...◝(ᵔᗜᵔ)◜")
        self.felicidad += 3
        if self.felicidad >10:
            self.felicidad = 10
        self.alimentacion -=1
        if self.alimentacion <0:
            self.alimentacion =0
        
    
    def vacunar(self):
        print(f"Estás vacunando a {self.nombre} ... (ᗒᗣᗕ)՞")
        self.salud +=5
        if self.salud > 10:
            self.salud = 10
        self.felicidad -=2
        if self.felicidad >10:
            self.felicidad = 10
        self.alimentacion -=1
        if self.alimentacion <0:
            self.alimentacion =0
   
new_tama = Tamagotchi("Gonpachi")  
#print("¡Ha nacido! ₍ᐢ. ̫ .ᐢ₎", new_tama)             

mi_tama = new_tama

#mi_tama.jugar()
#print("1.", mi_tama)

#mi_tama.alimentar()    
#print ("2.", mi_tama)

mi_tama.vacunar()
print("3.",mi_tama )