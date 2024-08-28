usuarios = {}

usuarios["gustavo"] = 400
usuarios["carlos"] = 200

def depositar():
    nombre = input("Introduce el nombre del usuario: ")
    
    if nombre in usuarios:
        monto = float(input("Introduce el monto a depositar: "))
        usuarios[nombre] += monto
    else:
        print(f"Usuario {nombre} no existe")
    
def registrar_usuario():
    nom_usuario = input("Introduce el usuario al que deseas registrar: ")
    
    if nom_usuario in usuarios:
        print("El usuario ya está registrado")
        return
    
    usuarios[nom_usuario] = 0
    print(f"el usuario{nom_usuario} agregado correctamente")
            
def retirar():
    nombre = input("Introduce el nombre del usuario: ")
    
    if nombre in usuarios:
        monto = float(input("Introduce el monto a retirar: "))
        if monto > usuarios[nombre]:
             print("Saldo insuficiente")
        else:
            usuarios[nombre] -= monto
           
print(usuarios)
retirar()
print(usuarios)