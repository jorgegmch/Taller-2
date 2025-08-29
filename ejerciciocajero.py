import os

os.system("cls")

print("BIENVENIDO A SU CAJERO BANCARROTA S.A.")

def mostrar_menu():
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("0. Salir")

isActive=True
while isActive:
    os.system