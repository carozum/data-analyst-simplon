

"""
Exercices de pseudo code / algorithmie

"""

# ********* 1. Ecrire un algorithme qui affiche tous les numéros de 1 à 9
for loop in range(1, 10):
    print(loop)
print("\n*******************\n")


# ********* 2. Ecrire un algorithme qui échange la valeur de 2 variables
"""
alphabet = « abcdefghijklmnopqrstuvwxyz »
i =26
tant que i différent de 0 :
	affichet i-ème élément de alphabet
	i = i -1
"""
a = 3
b = 5
print(a)
print(b)
c = a
a = b
b = c
print(a)
print(b)
print("\n*******************\n")


# ****** 3. Ecrire un algorithme qui affiche l'alphabet à l'envers
""" 
alphabet = « abcdefghijklmnopqrstuvwxyz »
i =26
tant que i différent de 0 :
	affichet i-ème élément de alphabet
	i = i -1
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
count = 26
while count > 0:
    print(alphabet[count-1])
    count -= 1
print("\n*******************\n")


# ****** 4. Ecrire un algorithme permettant d'épeler un mot en affichant chaque lettre les unes après les autres

""" 
mot= « salut »
pour i de 1 à la longueur de mot :
	afficher i-ème élément de mot
"""

word = input("Which word do you want to spell ? ")
for letter in word:
    print(letter)
print("\n*******************\n")


# ***** 5. Ecrire un algorithme qui affiche les différentes lettres nécessaires pour écrire un mot et le nombre de fois
""" 
mot = "hello"
pour i de 1 à longueur de mot:
    count = 1
    pour j de i+1 à longueur de mot - 1
    ajouter la lettre au dictionnaire si elle n'existe pas avec 
"""

new_word = "carolinefaure"

for i in range(len(new_word)):
    count = 1
    for j in range(i+1, len(new_word)):
        if new_word[i] == new_word[j]:
            count += 1
    print(new_word[i], count)


# ************ 6. Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu'à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : “Plus petit !”, et inversement, “Plus grand !” si le nombre est inférieur à 10.


# ******* 7. Écrire un algorithme qui calcule et affiche la surface d’un triangle connaissant sa base et sa hauteur.


# ******** 8. Écrire un algorithme qui, étant donné le prix unitaire d’un produit (hors TVA), le taux de TVA (en %) et la quantité de produit vendue à un client, calcule et affiche le prix total à payer par ce client.


# ******* 9.Écrire un algorithme qui, étant donné les résultats (note entière sur 20) de trois examens passés par un étudiant (exprimés par six nombres, à savoir, la note et la pondération de chaque examen), calcule et affiche la moyenne globale exprimée en pourcentage.


# ********* 10. Écrire un algorithme qui affiche toutes les combinaisons de deux nombre entre 0 et 99, dans l’ordre croissant au format “00 01, 00 02, 00 03 … 00 99, 01 02, … 97 99, 98 99”. Ne pas oublier les espaces et virgules !


# ******* 11. Écrire un algorithme qui calcule la somme des chiffres d’un nombre entier de 3 chiffres. Réflexion : l’algorithme est-il aussi valide pour les entiers inférieurs à 100 ?


# ******* 12. Écrire un algorithme itératif et un algorithme récursif qui affiche la somme de 1 à n


# ******** 13. Écrire un algorithme itératif et un algorithme récursif qui affiche le produit de 1 à n (ce qu’on appelle la factorielle n et noté n!)


# ******** 14. Écrire un algorithme itératif et un algorithme récursif qui affiche le n-ème terme de la suite de Fibonacci