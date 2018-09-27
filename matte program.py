 #imports
import time
import random
 #no more imports
 #prints
print ("Velkommen til Matteprogram!")
print ("Meny:")
print ("Nummer 1: Pluss")
print ("Nummer 2: Minus")




## start menu
menytilbakemelding = input ("Velg et nummer:")
if menytilbakemelding == "1":
    print ("Fint! La oss plusse!")
    print ("OK, hva er 214+632?")
    svar1 = input ("Svar til spørsmål:")
    if svar1 == "846":
       print ("Veldig bra!")
       print ("Du skal vente 5 sekunder før den andre oppgaven kommer.")
       time.sleep(5)
    else:
        print("Feil! Prøv på nytt.")
        time.sleep(5)
        print ("Lukk igjen programmet for å prøve på nytt.")
    print ("Hva er")
if menytilbakemelding == "2":
    print ("Fint! La oss ta vekk nummere!")
    print ("Hva er 3731 - 1978?")
    minussvar1 = input ("Svar til spørsmål:")
    if minussvar1 == "1753":
       print ("Veldig bra!")
       time.sleep(5)
    
