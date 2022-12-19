import random

import oldal1
import oldal137
import oldal215
import oldal270
import oldal293
import oldal373
import oldal387
import oldal56
import oldal66
ugyesseg = 0
eletero = 0
szerencse = 0
arany = 0
c = 0


def dobokocka(dobasok_szama):
    i = 0
    dobasok = 0
    while i < dobasok_szama:
        dobas = int(random.random()*6)+1
        dobasok += dobas
        i += 1
    return dobasok


def halal_labirintus():
    global c
    global ugyesseg
    global eletero
    global szerencse
    global arany
    ugyesseg = dobokocka(1) + 6
    eletero = dobokocka(2) + 12
    szerencse = dobokocka(1) + 6
    print(f"Ennyi ügyességed: {ugyesseg} \néleterőd: {eletero} \nés szerencséd: {szerencse} van!")
    while c < 10:
        valasztas = oldal1.oldal1()
        c += 1
        if valasztas == 270:
            c += 1
            arany = oldal270.oldal270(arany)
            valasztas = oldal66.oldal66()
            if valasztas == 293:
                c += 1
                valasztas = oldal293.oldal293()
                if valasztas == 137:
                    c += 1
                    oldal137.oldal137()
                elif valasztas == 387:
                    c += 1
                    oldal387.oldal387()
                    harc()
            elif valasztas == 56:
                c += 1
                valasztas = oldal56.oldal56()
                if valasztas == 373:
                    c += 1
                    oldal373.oldal373()
                elif valasztas == 215:
                    c += 1
                    oldal215.oldal215(eletero)
        elif valasztas == 66:
            c += 1
            valasztas = oldal66.oldal66()
            if valasztas == 293:
                c += 1
                valasztas = oldal293.oldal293()
                if valasztas == 137:
                    c += 1
                    oldal137.oldal137()
                elif valasztas == 387:
                    c += 1
                    oldal387.oldal387()
                    harc()
            elif valasztas == 56:
                c += 1
                valasztas = oldal56.oldal56()
                if valasztas == 373:
                    c += 1
                    oldal373.oldal373()
                elif valasztas == 215:
                    c += 1
                    eletero = oldal215.oldal215(eletero)
                    print(f'Ennyi életed maradt: {eletero}')
    print(f'A játék véget ért! Ezek a statjaid: \nÜgyesség: {ugyesseg} \nÉleterö: {eletero} \nSzerencse: {szerencse} \nArany: {arany} \nGratulálunk a játék teljesítéséhez!')


def harc():
    global c
    global ugyesseg
    global eletero
    global szerencse
    szorny_ugyesseg = 7
    szorny_eletero = 7
    szorny_ugyesseg += dobokocka(2)
    ugyesseg += dobokocka(2)
    while szorny_eletero > 0 and eletero > 0:
        statok = f'Az életerőd: {eletero} \nAz ügyességed: {ugyesseg} \nA szerencséd: {szerencse}' \
                 f'\nSzörny életereje: {szorny_eletero} \nSzörny ügyessége: {szorny_ugyesseg}'
        print(statok)
        if ugyesseg > szorny_ugyesseg:
            sz = ''
            while sz != 'igen' and sz != 'nem':
                sz = input('Használod a szerencsét? ')
            if sz == 'igen':
                if szerencsenk():
                    szorny_eletero -= 4

                else:
                    szorny_eletero -= 1

            elif sz == 'nem':
                szorny_eletero -= 2

        elif ugyesseg == szorny_ugyesseg:
            print('Kivédtétek egymást!')
        else:
            sz = ''
            while sz != 'igen' and sz != 'nem':
                sz = input('Használod a szerencsét? ')
                if sz == 'igen':
                    if szerencsenk():
                        eletero -= 1
                    else:
                        eletero -= 3

                elif sz == 'nem':
                    eletero -= 2

    if eletero <= 0:
        print('\nMeghaltál!')
        quit()
    elif szorny_eletero <= 0:
        print('\nTúlélted a csatát!')
        c += 1


def szerencsenk():
    global szerencse
    if dobokocka(2) < szerencse:
        szerencse -= 1
        return True
    else:
        szerencse -= 1
        return False

halal_labirintus()