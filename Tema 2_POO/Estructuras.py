class Estructuras: 
    def __init__(self, lista, diccionario, set_):
        self.lista = lista
        self.diccionario = diccionario
        self.set_ = set_

est = Estructuras ([1,2,3], {"Francia":"Euro", "México":"Peso Mexicano", "Reino Unido": "Libra Esterlina"}, {1,2,3})

print(f"Lista: {est.lista}") #Salida: [1,2,3]
print(f"Diccionario: {est.diccionario}") #Salida {"a":1, "b":2, "c":3}
print(f"Set:{est.set_}") #Salida {1,2,3}

#Los conjuntos se definen al crear el objeto en este ejemplo
#Todas se usan para almacenar múltiples datos/valores
#Todas empiezan en índice [0]
