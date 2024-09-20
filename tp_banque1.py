def  ajouterClient (numCl,  MPC,  numC,  SoldeC  ) :
    Client[numCl] = MPC
    Compte[numC] = SoldeC
    ClientCompte[numCl] = numC

def  SupprimerClient  ( numCl ):
    Client.pop(numCl)       #utiliser la fonction pop pour supprimer le client ayant le numéro numCl
    x=ClientCompte[numCl]      #récupérer le numéro de compte du client à partir du dictionnaire
                                                    #  ClientCompte
    Compte.pop(x)              #utiliser la fonction pop pour supprimer le compte du client en question
    ClientCompte.pop(numCl)


#cette fonction permet de vérifier si un client ayant un numéro numCl existe
def rechercheClient( numCl):
    if int(numCl) in ClientCompte: #vérifier si numClest une clé dans ClientCompte
         return True
    else:
         return False

#cette fonction permet de vérifier si le MP du client est correct
def  VerifMPClient ( numCl, MP):
    if Client[int(numCl)] == MP:
        print("MP Correcte")
        return True
    else :
        print(Client[int(numCl)])
        print("MP inCorrecte!")
    return False

def  modifierMPClient ( numCl, ancienMP, nouveauMP):
    if Client[numCl] == ancienMP: 		 #traiter le cas où l’ancienMP est correcte
        Client[numCl] = nouveauMP
    else:   					  	  #traiter le cas où l’ancienMP est incorrecte
        print("MP incorrecte")

def  deposer (NumCl, soldeD):
    x=ClientCompte[NumCl] 			#récupérer le numéro de compte du client
    Compte[x] = Compte[x] + soldeD		#ajouter le solde au compte
    print("Nouveau solde= " +  Compte[x])

def  retirer (NumCl, soldeR):
    x=ClientCompte[NumCl]
    if (Compte[x] -soldeR) <0:			 #vérifier si le retrait est permis
        print("solde Insuffisant!")
    else:
        Compte[x] = Compte[x]- soldeR		#retirer le solde
        print("retrait effectué avec succès! ")
        print("Nouveau solde= " +  Compte[x])

#Question 3 :

import math
import random
LambdaNumCompte= lambda numcl: str(numCl) + str(math.floor(random.uniform(0 , 100))) 
#math.floor envoie le plus grand entier inférieur ou égal à un nombre donné, random.uniffform(0,100) retourne un nombre aléatoire entre 0 et 100   

#Question 4 :
import csv
def  EcrireFichierCSV ( ):
    fichier = open("client.csv", "w")
    ecrivainCSV= csv.writer(fichier, delimiter=";")
    ecrivainCSV.writerow(["Numéro Client", "Code Secret"])   # On écrit la ligne d'en-tête avec le
    # titre des colonnes
    for x, y in  Client.items():
        ecrivainCSV.writerow([str(x), str(y)])
    fichier.close()

#Question 5 :
def  manipSTS( ) :
    listC= [] 					 #initialiser la liste
    setC=set({}) 					#initialiser le set
    for x, y in ClientCompte.items(): 		#parcourir les éléments de ClientCompte
        listC.append(y) 				#ajouter le numéro de compte à la liste
        setC.add(y) 					#ajouter le numéro de compte au set
    print("*Liste*")
    print(listC)
    print("*Set*")
    print(setC)
    print("**Tuple")
    tupleC=tuple(listC) #transformer la liste en tuple
    print(tupleC)


#Question 6 :
#Programme principal :
#iinitailiastion des dictionnaires
Compte = {1: 20,2: 19,3: 100}
Client = {1: '123',2: '566',3: '999'}
ClientCompte= {1:1,2: 2,3: 3}

choixAC= input("Si vous êtes un agent bancaire tapez 1\n "
                    "si vous êtes un client tapez 2 \n")
resultat= False
resultatMP= False
r = False
numCl= 3
if choixAC== "1": 			#vérifier s'il s'agit d'un agent
    mp= input("Donner votre mot de passe:")
    if (mp== "0000"):
        continuer=True
        while(continuer):
            print("**************Menu**************")
            print("1-Ajouter un compte Cient")
            print("2-Supprimer un compte client")
            print("3-Générer un fichier Client")

            Choix = False
            while(Choix == False):
                numchoix= input("*********Tapez le numéro de votre choix*******\n")
                if numchoix== "1":
                    Choix = True
                    numCl= numCl+ 1
                    numC= LambdaNumCompte(numCl)
                    solde = input("Donner le solde:")
                    ajouterClient(numCl, "6666", int(numC), int(solde))
                    print("client ajouté avec succès!")
                elif numchoix== "2":
                    Choix = True
                    numclientSup= input("Donner le numéro du client à supprimer")
                    SupprimerClient(int(numclientSup))
                    print("client supprimé avec succès!")
                elif numchoix=="3":
                    Choix = True
                    print("Fichier Client généré avec succès")
                    EcrireFichierCSV()
                else:
                    print("Tapez 1 ou 2")
    else: 	# c'est le cas où le mot de passe de l'agent est incorrecte
        print("Mpincorrect")

elif choixAC== "2":    #vérifier s'il s'agit d'un client
    print(Client)
    ChoixNumC = False
    while (ChoixNumC == False):
        s = input("Tapez votre numero\n")
        if (rechercheClient(int(s)) == True):
            ChoixNumC = True  # numClient est correcte
            ChoixMp = False
            while (ChoixMp == False):
                mp = input("Donner votre mot de passe \n")
                if (VerifMPClient(s, mp) == True):
                    ChoixMp = True
                    ChoixCorrecte = False
                    while (ChoixCorrecte == False):
                        print("*************Tapez un numéro au choix**************\n")
                        print("1-Afficher solde")
                        print("2-Déposer un montant")
                        print("3-Retirer un montant")
                        print("4-Modifier mot de passe")
                        numchoix = input("*******************Tapez le numéro de votre choix****************************\n")
                        if numchoix == "1":
                            ChoixCorrecte = True
                            x = ClientCompte[int(s)]
                            print("Votre solde= ", Compte[x], "D")
                        elif numchoix == "2":
                            ChoixCorrecte = True
                            soldeD = input("Donner le montant à déposer:")
                            deposer(int(s), float(soldeD))
                            print(Compte)
                            print("Solde déposé avec succès!")
                        elif numchoix == "3":
                            ChoixCorrecte = True
                            soldeD = input("Donner le montant à retirer:")
                            retirer(int(s), float(soldeD))
                            print(Compte)
                            print("Solde retiré avec succès!")
                        elif numchoix == "4":
                            print(Client)
                            ChoixCorrecte = True
                            nouveauMP = input("Donner votre nouveau MP")
                            modifierMPClient(int(s), mp, nouveauMP)
                            print("mot de passe modifié avec succès!")
                        else:
                            print("Tapez 1, 2, 3 ou 4")

                else:  # MP incorrecte
                    print("Veuillez vérifier votre mot de passe")
            else:  # numéro de client inexistant
                print("Veuillez vérifier votre numéro")

else:  # c'est le cas où le client où l'agent n'a pas saisi 1 ou entrer à son menu
    print("Tapez 1 ou 2")





