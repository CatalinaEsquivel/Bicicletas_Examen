class Carrito:
    def __init__(self, request): #permite mantener la sesión
        self.request = request 
        self.session = request.session #la sesión sea igual a la del request
        carrito = self.session.get("carrito") 
        if not carrito: 
            self.session["carrito"] = {} #diccionario vacío
            self.carrito = self.session.get("carrito")
        else: #si el carro no está vacío
            self.carrito = carrito
    
    def agregar(self, Bicicleta):
        idBicicleta = str(Bicicleta.idBicicleta)
        if idBicicleta not in self.carrito.keys():
            self.carrito[idBicicleta]={
                "producto_id" : Bicicleta.idBicicleta,
                "marca" : Bicicleta.marca,
                "acumulado" : Bicicleta.precio,
                "cantidad":1,
            }
        else: 
            self.carrito[idBicicleta]["cantidad"] += 1
            self.carrito[idBicicleta]["acumulado"] += Bicicleta.precio
            self.guardar_carrito()
            
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, Bicicleta):
        idBicicleta = str(Bicicleta.idBicicleta)
        if idBicicleta in self.carrito:
            del self.carrito[idBicicleta]
            self.guardar_carrito()
            
    def restar(self, Bicicleta):
        idBicicleta = str(Bicicleta.idBicicleta)
        if idBicicleta in self.carrito.keys():
            self.carrito[idBicicleta]["cantidad"] -= 1
            self.carrito[idBicicleta]["acumulado"] -= Bicicleta.precio
            if self.carrito[idBicicleta]["cantidad"] <=0: self.eliminar(Bicicleta)
            self.guardar_carrito()
    
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
                    
        