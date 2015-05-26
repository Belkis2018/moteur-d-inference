#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
from string import *



'''

# # voici une description bref sur le projet 

# # une regle est composÃ© d'une premisse et une action 
# # chaque premisse peut Ãªtre unaire ou multiple encore la meme chose pour une action.
# # premisse   action
# # A,B,C   -> D,E
# # E       -> FG
# # D       -> k

# # les fonctions dans la classe regles:
# # l'initialision de regle
# # la decompostion d'une regle entre premisse et action 
# # la recherche d'une premisse 
# # la recherche d'une action 
# # //**************** dans ce qui suit ****
# # l"ajout d"une regles
# # la verification de la validitÃ© d'une regle
# # la suppression d'une regle 
# # la mise Ã  jour d'une regle




# # les regles se trouve dans une fichier input
# #  
# # ouvrir une fichier 
# # fermer une fichier 
# # extraire les regles 



 '''






class File():
	"""docstring for File"""

	def __init__(self, arg):
		self.arg = arg

	def read(self):# conversion d'un fichier Ã  une chaine de caractere 
		res = {}
		with open(self.arg,"r") as text: # lire 
			for line in text:
				key, value = line.split("->", 1)
				res[key] = value.replace('\n','', 1)
		#print res
		return res
			
	def update(self, arg,regle):
		text=open(arg,"a+") # ajouter une regle du fichier 
		text.write(regle)
		text.close()









class Regle(File,object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Regle,self).__init__( arg)
		self.arg = arg


	def chainageAvant(self, entree, chaine ):#  fonction recursive pour faire le chainge avant 
		#recursif 
		dic=super(Regle,self).read()
		#print dic
		if dic.__contains__(entree):
			#extraire la regle 

			# print "************************"
			axiome=dic[entree]
			# print axiome
			# print "************************"
			# # axiome -> liste 
			ListeAxiome = axiome.rsplit(',')
			# print ListeAxiome

			# print "************************"
			ListeEntree = entree.rsplit(',')
			# print ListeEntree
			# print "************************"

			for l in ListeAxiome :
				if "<"+l+">" in chaine :# pour eleminer bouclage infini de  a->c et c->a 
					chaine = chaine.replace("<","")
					chaine = chaine.replace(">","")
					chaine = chaine.replace("-","->")
					print chaine
						
				else : 
					self.chainageAvant(l, chaine+"-<"+l+">")# appel recursif 

			
		else : 
			chaine = chaine.replace("<","")
			chaine = chaine.replace(">","")
			chaine = chaine.replace("-","->")
			print chaine


	def chainageAriere(self , entree , chaine): 
		#recursif 
		dic=super(Regle,self).read()
		c=[]
		recherche = lambda dic, chaine: [c for c,v in dic.items() if v.__contains__(chaine)!=0]
		if recherche(dic , entree).__len__()!=0 : 
			for l in recherche(dic , entree):
				if "<"+l+">" not in chaine :
					print l
					self.chainageAriere(l , "<"+l+">"+chaine)
				
		else : 
			if chaine==entree:
				print "rien"







x = Regle("BF.txt")
res=x.read()

while 1:
	print "Voulez vos faire un chainage avant ou arriÃ¨re (1,2) ? exit 0"
	choix =-1 # cchoix de l'utilisateur 
	entree = "" # l'entree de l'utilisateur 
	while choix >2 or choix <0 :

		choix = int(raw_input())
		if choix >2 or choix <0: 
			print "votre choix hors [0-2]"
	
	if choix ==2 : 
		print "Saisissez que voulez vous avoir ?"
		entree= raw_input()
		print "Vous devez avoir  : "
		x.chainageAriere(entree,entree)
	elif choix ==1: 
		print "Saisissez dâ€™oÃ¹ voulez vous partir ?"
		entree= raw_input()
		print "Vous devez avoir  : "
		x.chainageAvant(entree,entree)
	else : 
		exit(0)	
