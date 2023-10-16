class usuario:
    def __init__(self,nombre, balance):
        self.nombre = nombre
        self.balance = balance
        
    def hacer_retiro(self, amount):
        self.balance -= amount
        
    def hacer_deposito(self, amount):
        self.balance += amount
    
    def trasfer_dinero(self, other_user, amount):
        self.balance -= amount
        other_user.balance += amount
        
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")
        
usuario1 = usuario("Guido van Rossum", 100)
usuario2 = usuario("Donald Knuth", 200)
usuario3 = usuario("Ada Lovelace", 300)

# primera tarea del usuario 1 
usuario1.hacer_deposito(100)
usuario1.hacer_deposito(110)
usuario1.hacer_deposito(200)
usuario1.hacer_retiro(300)
usuario1.mostrar_balance_usuario()

#segunda tarea de usuario 2
usuario2.hacer_deposito(233)
usuario2.hacer_deposito(115)
usuario2.hacer_retiro(60)
usuario2.hacer_retiro(20)
usuario2.mostrar_balance_usuario()

#tercera tarea de usuaruio 3 
usuario3.hacer_deposito(487)
usuario3.hacer_retiro(90)
usuario3.hacer_retiro(100)
usuario3.hacer_retiro(20)
usuario3.mostrar_balance_usuario()

#bonus
usuario1.trasfer_dinero(usuario3, 120)
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()