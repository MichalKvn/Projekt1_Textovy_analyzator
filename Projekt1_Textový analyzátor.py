
#projekt_1.py: První projekt do Engeto Online Python Akademie
#author: Michal Kavan
#email: kavan1@centrum.cz
#discord: Michal K.#5207

TEXTS = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''

TEXT1 = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. '''
TEXT2 = '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.'''
TEXT3 = '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''

TEXTS = [TEXT1, TEXT2, TEXT3]
CARA = "-----------------------------------------------------------"
user = ["bob", "ann", "mike", "liz"]
password = ["123", "pass123", "password123", "pass123"]

otazka_jmeno = input("Zadejte prosím své přihlašovací jméno:\n")
otazka_heslo = input("Zadejte prosím své přihlašovací heslo:\n")

if (otazka_jmeno == user[0] and otazka_heslo == password
    [0]) or (otazka_jmeno == user[1] and otazka_heslo == password
             [1]) or (otazka_jmeno == user[2] and otazka_heslo == password
                      [2]) or (otazka_jmeno == user[3] and otazka_heslo == password
                               [3]):
    print(CARA)
    print("$ python projekt1.py""\n"
    "username:", otazka_jmeno,"\n" 
    "password:", otazka_heslo,"\n")
    print(CARA)
    text_choice = input("Přihlášení proběhlo úspěšně, vítejte v analyzátoru textů ""\n"
        "Máme na výběr ze 3 textů k testové analýze""\n")
    print(CARA)
    if text_choice.isdigit() and 1 <= int(text_choice) <= 3:
        text_index = int(text_choice) - 1
        selected_text = TEXTS[text_index]
        print(f"K analýze jste zvolili text číslo {text_choice}")
        print(CARA)
    else:
        print("Zadali jste nesprávné číslo, nebo znak, který neodpovídá textu určeného k analýze")
        exit()
    
    words = selected_text.split()
    fixed = []
    for slova in words:
            fix = slova.replace(".","").replace(",","").replace("-","")
            fixed.append(fix)

    pocet_slov = len(fixed)
    pocet_slov_velke_pismeno = sum(1 for slovo in fixed if slovo[0].isupper())
    pocet_slov_velka_pismena = sum(1 for slovo in fixed if slovo.isupper())
    pocet_slov_mala_pismena = sum(1 for slovo in fixed if slovo.islower())
    cisla = []

    for slovo in fixed:
            if slovo.isdigit():
                cisla.append(int(slovo))

    pocet_cisel = len(cisla)
    suma_cisel = sum(cisla)

    print("Počet slov:", pocet_slov - pocet_cisel)
    print("Počet slov začínajících velkým písmenem:", pocet_slov_velke_pismeno)
    print("Počet slov psaných velkými písmeny:", pocet_slov_velka_pismena)
    print("Počet slov psaných malými písmeny:", pocet_slov_mala_pismena)
    print("Počet čísel:", pocet_cisel)
    print("Suma čísel:", suma_cisel)
    print(CARA)
    for index,pocet_znaku in enumerate(fixed):
             znaky = (len(pocet_znaku))
             hvezdicky1 = str(znaky * "*" )
             print( f'{index+1:5d}'". |", f'{hvezdicky1:<17s}' f'{znaky}')
    print(CARA,"\n""Děkujeme za využití našeho textového analyzátoru""\n"
              "Přeji hezký den")
    
else:
    print(CARA)
    print("$ python projekt1.py""\n"
    "username:", otazka_jmeno,"\n" 
    "password:", otazka_heslo,"\n"
    , CARA)
    print("Uživatelské jméno nebo heslo je chybné. Zkontrolujte své údaje.")
    exit()