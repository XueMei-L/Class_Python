# class Account

# Atributos:
# - número de la cuenta (int)
# - número de la tarjeta (int)
# - titular de la cuenta  (str)
# - fecha de caducidad  (date)
# - código de seguridad cvv 3 digitos (int)
# - saldo (int)
# - información de ingreso, trasferencia, y retiro, (una lista de informaciones) [lista]

# Metodos:
# - Mostrar saldo
# - Hacer una transferencia
# - Hacer un ingreso
# - Retirar/sacar dinero

import random
from datetime import datetime, date

# clase Cuenta
class Account:
    # Atributos
    def __init__(self, accountNumber, holderName:str, password:int, balance: float = 0.0):
        self.accountNumber = accountNumber
        self.holderName = holderName
        self.password = password
        self.balance = balance
        self.cvv = random.randint(0,999)

        # fecha de caducidad de la tarjeta
        today = datetime.now()
        fiveYearsLate = today.year + 5
        self.expirationDate = date(fiveYearsLate, today.month, today.day)
        # print(self.expirationDate)

    # Metodos:
    # Mostrar saldo
    def displayInformation(self) -> None:
        print("\n=================Información de la cuenta=================")
        print(f"Número de la cuenta: {self.accountNumber}")
        print(f"Titular de la cuenta: {self.holderName}")
        print(f"Saldo de la cuenta: {self.balance} euros" )

    def displayInformationSecret(self) -> None:
        password = int(input("Introduzca su contraseña para ver información: "))
        if password == self.password:
            print("\n================Información secreta de la cuenta===============")
            print(f"Número de la cuenta: {self.accountNumber}")
            print(f"Fecha de caducidad: {self.expirationDate}")
            print(f"cvv: {self.cvv}")
    
    def transfer(self):
        print("==============Transferencias==============")
        iban = input("Iban del destinatario: ")
        beneficiaryName = input("Nombre del beneficiario: ")
        amount = float(input("Introduzca el importe: "))
        concept = input("Concepto: ")
        password = int(input("Introduzca su contraseña para hacer la trasnferencia: "))
        if password == self.password:
            if amount <= self.balance:
                print("==============Mensaje de éxito==============")
                print("Hiciste una transferencia con los siguientes datos:")
                print(f"Número de iban: {iban}")
                print(f"Nombre del beneficiario: {beneficiaryName}")
                print(f"Importe: {amount}")
                print(f"Concepto: {concept}")
            else:
                print(f"No se puede hacer la transferencia, puesto que su saldo es: {self.balance}")
        else:
            print("La contraseña está mal.")

# funcion principal
def main():
    objAccount = Account("1234 5678 1010 9999 ","Juan", 123456)
    # objAccount.displayInformation()
    # objAccount.displayInformationSecret()
    objAccount.transfer()

if __name__ == "__main__":
    main()