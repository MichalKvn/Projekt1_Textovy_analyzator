
#projekt_1.py: První projekt do Engeto Online Python Akademie
#author: Michal Kavan
#email: kavan1@centrum.cz
#discord: Michal K.#5207

from collections import Counter

TEXTS = ('''
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
garpike and stingray are also present.''',)

CARA = "-----------------------------------------------------------"
user_and_password = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}


def verify_credentials(username, password):
    if username in user_and_password and user_and_password[username] == password:
        return True
    else:
         print(f"username: {username}")
         print(f"password: {password}")
         print(CARA)
         print("Uživatelské jméno nebo heslo je chybné. Zkontrolujte své údaje.")
         exit()
         
username = input("Zadej uživatelské jméno: ")
password = input("Zadej heslo: ")

if verify_credentials(username, password):
    print("Přihlášení úspěšné")
    print(CARA)
    print("$ python projekt1.py""\n"
    "username:", username,"\n" 
    "password:", password,"\n")
    print(CARA)
    text_choice = input("Přihlášení proběhlo úspěšně, vítejte v analyzátoru textů ""\n"
    "Máme na výběr ze 3 textů k testové analýze""\n")
    print(CARA)

if text_choice.isdigit() and int(text_choice) <= len(TEXTS):
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
cisla = []
for slovo in fixed:
    if slovo.isdigit():
          cisla.append(int(slovo))

pocet_cisel = len(cisla)
suma_cisel = sum(cisla)

pocet_slov = len(fixed)
pocet_slov_velke_pismeno = sum(1 for slovo in fixed if slovo[0].isupper())
pocet_slov_velka_pismena = sum(1 for slovo in fixed if slovo.isupper())
pocet_slov_mala_pismena = sum(1 for slovo in fixed if slovo.islower())
    

print("Počet slov:", pocet_slov)
print("Počet slov začínajících velkým písmenem:", pocet_slov_velke_pismeno)
print("Počet slov psaných velkými písmeny:", pocet_slov_velka_pismena)
print("Počet slov psaných malými písmeny:", pocet_slov_mala_pismena)
print("Počet čísel:", pocet_cisel)
print("Suma čísel:", suma_cisel)
print(CARA)
    
print("LENGTH |  OCCURRENCES  | NUMBER")
delky_slov = [len(slovo) for slovo in fixed]
ct = Counter(delky_slov)
seřazené_ct = sorted(ct.most_common(len(ct)))
for delka, pocet in seřazené_ct:
    hvezdy = pocet * "*"
    print(f" {str(delka):5s} | {hvezdy.ljust(13)} | {str(pocet):2s}")
print("\nDěkujeme za využití našeho textového analyzátoru")
print("Přeji hezký den")



    