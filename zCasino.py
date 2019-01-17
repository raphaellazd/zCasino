# coding:utf-8
from random import randrange
from math import ceil

recommencer = True
argentJoueur = 1000

while recommencer is True :

	numJoueur = input("Bonjour, bienvenue a cette table de roulette. Vous disposez d'un credit de "+str(argentJoueur)+"$. Veuillez choisir un numéro entre 0 et 49, merci.")
	try:
		numJoueur = int(numJoueur) 
	except :
		print("Vous n'avez pas saisi un nombre...")
	
	miseJoueur = input("Très bien, allons pour le "+str(numJoueur)+", combien desirez-vous parier?") # ca va pas marcher car je peux pas concatener un int avec un str
	miseJoueur = int(miseJoueur)
	numGagnant = randrange(0, 49)  # choisi un chiffre aléatoire

	print("Rien ne va plus.")		#  fin des mises, la sortie du numéro gagnant étant imminente
	print("Le numero gagnant est le "+str(numGagnant)+" !")
	if numJoueur == numGagnant:      # si le numero choisi est le numero gagant
		miseJoueur = miseJoueur * 3
		argentJoueur = argentJoueur + miseJoueur
		retry = input("Bien joué vous remportez la partie et gagnez "+str(miseJoueur)+"$ ! Vos gains s'élèvent donc à "+str(argentJoueur)+"$. Tapez r pour une nouvelle partie. Tapez q pour quitter la table.")
		
		if retry =="q":
			recommencer = False
		elif retry =="r":
			continue

	
	elif (numJoueur % 2 == 0 and numGagnant % 2 == 0) or (numJoueur % 2 == 1 and numGagnant % 2 ==1):  # si le numero choisi est de la meme couleur que le numero gagnant
		miseJoueur = miseJoueur / 2
		argentJoueur = argentJoueur - miseJoueur
		retry = input("Couleur ! Vous recuperez la moitié de votre mise soit "+str(miseJoueur)+"$. Vos gains s'élèvent donc à "+str(argentJoueur)+"$. Tapez r pour une nouvelle partie. Tapez q pour quitter la table.")
		
		if retry =="q":
			recommencer = False
		elif retry =="r":
			continue
 
	else :
		miseJoueur == 0
		argentJoueur = argentJoueur - miseJoueur
		retry = input("C'est raté, et vous perdez votre mise. Tapez r pour une nouvelle partie. Tapez q pour quitter la table.")
		
		if retry =="q":
			recommencer = False
		elif retry =="r":
			continue
