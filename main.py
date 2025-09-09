import datetime
from utils import fibonacci 

if __name__ == "__main__":
    name = input("Quel est ton nom ? ")
    print(f"Bienvenue {name} dans le laboratoire Git + Python !")
a = 5
b = 7
print(f"La somme de {a} et {b} est {a+b}")

print(f"Bienvenue {name}, aujourd'hui nous sommes le {datetime.date.today()}")

print("Suite de Fibonacci (10 premiers termes):", fibonacci(10))
