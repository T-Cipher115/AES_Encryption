from cryptography.fernet import Fernet

#Fonction chiffrer un fichier
def chiffrer_fichier(file_name="secret.txt"):
    ma_cle = Fernet.generate_key()
    print(f"La clé de chiffrement est : {ma_cle}")
    machine_aes = Fernet(ma_cle)

    #On ouvre le fichier en mode Lecture d'octet via rb 
    with open(file_name, "rb") as file_toencrypt :
        #On Stocke les données à chiffrer dans une variable
        données_à_chiffrer = file_toencrypt.read()
        #On passe cette Variable dans la fontion d'Encryption
        données_chiffrés = machine_aes.encrypt(données_à_chiffrer)
        print(f"Le chiffrement du fichier est terminé")
        
    #Une fois les données chiffrés on les stocke en écrasant le fichier
    with open (file_name,"wb") as fichier_verrouillé :
        fichier_verrouillé.write(données_chiffrés)
        
    #On retourne la clé
    return ma_cle

#Fonction pour déchiffrer le fichier avec la clé
def déchiffrer_fichier(cle_secrete, file_name="secret.txt"):
    print("Lancement protocole de déchiffrement...")
    machine_aes = Fernet(cle_secrete)
    
    with open(file_name,"rb") as file_todecrypt :
        données_à_dechiffrer = file_todecrypt.read()
        données_propre = machine_aes.decrypt(données_à_dechiffrer)
        print(f"Le dechiffrement du fichier est terminé")
   
    with open(file_name,"wb") as file_decrypt :
        file_decrypt.write(données_propre)
        print(f"Données restaurées avec succès !")

if __name__ == "__main__":
    print("☠️ Lancement du crypteur T-Cipher115...")
    
    # 1. On lance l'attaque et on récupère la clé
    cle_sauvee = chiffrer_fichier() 
    
    input("Appuyez sur entrée pour soigner le virus T...")
    
    # 2. On lance l'antidote avec la clé sauvée
    déchiffrer_fichier(cle_sauvee)