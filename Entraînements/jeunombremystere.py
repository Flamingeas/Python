import random 

nombre_mystere = random.randint(1, 100)

trouve = False
essais = 0

print("Bienvenue dans le jeu du Nombre Mystère !")
print("Devinez le nombre entre 1 et 100")

while not trouve: 
   try:
      essai = int(input("Entrez un nombre : "))
      essais += 1
      if essai > nombre_mystere :
        print("C'est trop grand !")
      elif essai < nombre_mystere :
        print("C'est trop petit !")
      else:
        print(f"Bravo ! Vous avez trouvé le nombre mystère en {essais} essais.")
        trouve = True  
   except ValueError:
     print("Veuillez rentrer un nombre.")
