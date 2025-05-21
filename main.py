jatekmod = int(input("1 vagy 2 játékos: "))

nev1 = ""
nev2 = ""

if jatekmod == 1:
    nev1 = input("Játékos neve: ")
    nev2 = "Robot"
elif jatekmod == 2:
    nev1 = input("Első Játékos neve: ")
    nev2 = input("Második Játékos neve: ")