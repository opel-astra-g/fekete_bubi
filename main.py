import random

jatekmod = int(input("1 vagy 2 játékos: "))

nev1 = ""
nev2 = ""

eredmeny = ""

if jatekmod == 1:
    nev1 = input("Játékos neve: ")
    nev2 = "Robot"
elif jatekmod == 2:
    nev1 = input("Első Játékos neve: ")
    nev2 = input("Második Játékos neve: ")

nev1_kartyak = [random.randint(2, 11) for _ in range(2)]
nev2_kartyak = [random.randint(2, 11) for _ in range(2)]

if (sum(nev1_kartyak) == sum(nev2_kartyak)):
    eredmeny = "Döntetlen"
elif (sum(nev1_kartyak) == 21):
    eredmeny = f"{nev1} nyert"
elif (sum(nev2_kartyak) == 21):
    eredmeny = f"{nev2} nyert"
elif (sum(nev1_kartyak) < 21 and sum(nev2_kartyak) < 21):
    if (sum(nev1_kartyak) > sum(nev2_kartyak)):
        eredmeny = f"{nev1} nyert"
    elif (sum(nev1_kartyak) < sum(nev2_kartyak)):
        eredmeny = f"{nev2} nyert"
elif (sum(nev1_kartyak) > 21 or sum(nev2_kartyak) > 21):
    if (sum(nev1_kartyak) < 22):
        eredmeny = f"{nev1} nyert"
    elif (sum(nev2_kartyak) < 22):
        eredmeny = f"{nev2} nyert"

print(f"{nev1} kártyái: {nev1_kartyak} Összesen {sum(nev1_kartyak)}")
print(f"{nev2} kártyái: {nev2_kartyak} Összesen {sum(nev2_kartyak)}")

print(eredmeny)