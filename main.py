import random

jatekmod = int(input("1 vagy 2 játékos: "))

nev1 = ""
nev2 = ""

if jatekmod == 1:
    nev1 = input("Játékos neve: ")
    nev2 = "Robot"
elif jatekmod == 2:
    nev1 = input("Első Játékos neve: ")
    nev2 = input("Második Játékos neve: ")

nev1_kartyak = [random.randint(2, 11) for _ in range(2)]
nev2_kartyak = [random.randint(2, 11) for _ in range(2)]