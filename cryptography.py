from cryptography.fernet import Fernet

#Fonction chiffrer un fichier
def chiffrer_fichier(file_name = "secret.txt"):
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
    #Une fois les données chiffrés ont les stockes dans un nouveau fichier
    with open (file_name,"wb") as fichier_verrouillé :
        fichier_verrouillé.write(données_chiffrés)
    #On retourne la clé
    return ma_cle

if __name__ == "__main__":
    print("Lancement du crypteur...")
    
    #Clé deverouillage
    cle_secrete = chiffrer_fichier() 
    
