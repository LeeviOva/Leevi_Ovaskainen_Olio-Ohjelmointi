import random

def kpsk():
    print("Pelaa KPS (kivi, paperi vai sakset? toimii myös K, P ja S)")
    user_input = input("Valitse: ")
    if user_input == "kivi" or user_input == "k":
        kpsp = 1
    if user_input == "paperi" or user_input == "p":
        kpsp = 2
    if user_input == "sakset" or user_input == "s":
        kpsp = 3
    return kpsp
   
def kpst():
    kone_numero = random.randint(1,3)
    if kone_numero == 1:
        print("Kone valitsi kiven")
    if kone_numero == 2:
        print("Kone valitsi paperin")
    if kone_numero == 3:
        print("Kone valitsi sakset")    
    return kone_numero


def pcheck(kpsp, kone_numero, pwins):
    if kpsp == 1 and kone_numero == 3:
        pwins = pwins +1
    elif kpsp == 2 and kone_numero == 1:
        pwins = pwins + 1
    elif kpsp == 3 and kone_numero == 2:
        pwins = pwins +1
    elif kpsp == kone_numero:
        print("Tasapeli otetaas uusiks")
    print("pwins: ", pwins)
    return pwins


def ccheck(kpsp, kone_numero, cwins):
    if kpsp == 3 and kone_numero == 1:
        cwins = cwins + 1
    if kpsp == 1 and kone_numero == 2:
        cwins = cwins + 1
    if kpsp == 2 and kone_numero == 3:
        cwins = cwins + 1
    print("cwins: ", cwins)
    return cwins
    

def victoryscreen(pwins, cwins):
    if pwins > cwins:
        print("Voitit, onnea!")
    else:
        print("Hävisit, parempi onni ensikerralla.")

pwins = 0
cwins = 0
while True:
    kpsp = kpsk()
    kone_numero = kpst()
    pwins = pcheck(kpsp, kone_numero, pwins)
    cwins = ccheck(kpsp, kone_numero, cwins)
    print("------------------------")
    if pwins == 3 or cwins == 3:
        break
victoryscreen(pwins, cwins)
