from common.util import genereaza_id , sterge , listeaza
from pytz import country_timezones, timezone
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from datetime import datetime

# """
# Comenzile ar trebui sa aiba structura:
# ("id_comanda": {
#     "id_comanda": "Idcomanda" - string,
#     "detalii_comanda":
#         [{"IdProdus": CantitateProdus}]
#         - lista de dictionare de forma IdProdus (string): CantitateProdus (numar intreg),
#     "data_inregistrare": "DataInregistrare" - string,
# })
#
# """
# import json
# from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
# import hashlib
# from datetime import datetime
# from pprint import pprint
# from produse.functii import adauga_un_produs
# from common.util import genereaza_id , sterge , listeaza
#
# from pytz import country_timezones, timezone
#
#
# def adauga_o_comanda():
#     """
#     Introdu de la tastatura cu textul: "Introduceti produsele din comanda. Pentru a termina, introduceti 'stop':\n"
#     Ca prim input dam Produsul, apoi Cantitatea
#     Generam ID-ul unic comenzii
#     Generam data inregistrarii
#     Citim din baza de date
#     Generam structura dictionarului
#     Scriem in baza de date
#     """
#
#     actiune = None
#     while actiune != "stop":
#         nume_produs = input("Introduceti produsele din comanda.\n") #introducerea produsului
#         cantitatea = float(input("Introduceti cantitatea din comanda.\n")) #introducerea cantitatii
#         actiune = input("Pentru a termina, introduceti:'stop' pentru a adauga o noua comanda apasa orice tasta si enter\n")
#         detalii_comanda = {nume_produs : cantitatea}
#         id_comanda = genereaza_id(nume_produs , str(cantitatea))
#         data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
#         datele_noastre = citeste_datele_din_baza_de_date() # citirea din fisier
#         datele_noastre["comenzi"][id_comanda] = { #structura dictionarului
#             "id_comanda": id_comanda,
#             "detali_comanda": detalii_comanda,
#             "data_inregistrare": data_inregistrare.isoformat()
#         }
#         scrie_datele_in_baza_de_date(datele_noastre)
#
# def modifica_comanda():
#     """
#     Introduceti de la tastatura textul: "Introduce??i identificatorul comenzii care se modifica: "
#     Creeam o logica care sa primeasca ca input de la tastatura 4 variante de actiune:
#         "Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#         Creeam logica pentru cele 4 variante
#         Ca input trebuie sa dam produsul si cantitatea pentru 'a' si 'm', pentru 's' dam identificatorul
#         Din nou, Citim, Actionam, Scriem
#     """
#     data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
#     datele_noastre = citeste_datele_din_baza_de_date() # citire din fisier
#     identificatorul = input("Introduce??i identificatorul comenzii care se modifica: \n")
#     if identificatorul in datele_noastre["comenzi"]: #verificare daca identificatorul este in fisier
#         print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#         actiune = "" #actiunea primeste un string gol pentru a-l putea verifica
#         while actiune != "e": # un while pentru actiuni multiple
#             actiune = input("\n")
#             if actiune.lower() == "e": # daca prima comanda este e se iese din
#                 pass
#             elif actiune.lower() == "a": # pentru adaugare produs am ales sa adaug si cantitatea,
#                 nume_produs = ""
#                 while len(nume_produs) < 1 or len(nume_produs) > 50:
#                     nume_produs = input("Introduceti numele produsului de adaugat:\n")
#                     if len(nume_produs) < 1 or len(nume_produs) > 50:
#                         print("Nume invalid, trebuie sa aiba intre 1 si 50 de caractere")
#                 cantitatea = float(input("Introduceti cantitate produsului de adaugat: \n"))
#                 datele_noastre["comenzi"][identificatorul] = {
#                 "id_comanda": identificatorul,
#                 "detali_comanda": {nume_produs : cantitatea},
#                 "data_inregistrare": data_inregistrare.isoformat()
#                  }
#                 print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#             elif actiune.lower() == "m":
#                 nume_produs = ""
#                 while len(nume_produs) < 1 or len(nume_produs) > 50:
#                     nume_produs = input("Introduceti numele produsului de adaugat:\n")
#                     if len(nume_produs) < 1 or len(nume_produs) > 50:
#                         print("Nume invalid, trebuie sa aiba intre 1 si 50 de caractere")
#                 cantitatea = float(input("Introduceti cantitate produsului de adaugat: \n"))
#                 if nume_produs in datele_noastre["comenzi"][identificatorul]["detali_comanda"]:
#                     datele_noastre["comenzi"][identificatorul] = {
#                         "id_comanda": identificatorul,
#                         "detali_comanda": {nume_produs: cantitatea},
#                         "data_inregistrare": data_inregistrare.isoformat()
#                     }
#                 else:
#                     print(f"produsul {nume_produs} nu este in comanda")
#                 print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#             elif actiune.lower() == "s":
#                 datele_noastre["comenzi"].pop(identificatorul)
#                 print("Alegeti actiunea ('a' - adaugare produs; 'm ' - modificare cantitate; 's'-sterge produs, 'e'-exit \n")
#             else:
#                 actiune = input("\n")
#     else:
#         print("Identificator gresit")
#     scrie_datele_in_baza_de_date(datele_noastre)
#
#
#
# def listeaza_toate_comenzile():
#     """
#     Functia trebuie sa afiseze toate comenzile prezente in baza de date.
#     Afisarea ar trebui sa contina toate informatiile comenzilor
#     """
#     listeaza("comenzi")
#
#
#
# def sterge_o_comanda():
#     """
#     Introdu de la tastatura cu textul  "Introduce??i identificatorul comenzii de sters: "
#     Cititi, stergeti, Scrieti
#
#     """
#     comanda_pt_sters = input("intrrodu id pt sters\n")
#     sterge(comanda_pt_sters, "comenzi")
#
#
# # def verificare_comanda():
# #     datele_noastre = citeste_datele_din_baza_de_date()
# #     nume_produs = datele_noastre["comenzi"]["detali_comanda"].keys()
# #     produs_de_verificat = datele_noastre["produse"]["nume_produs"]
# #     print(nume_produs)
# #    print(produs_de_verificat)
#     # if nume_produs == produs_de_verificat:
#     #     print(f"produsul {nume_produs} din comanda {identificatorul} este in stoc")
#     # else:
#     #     print(f"produsul {nume_produs} din comanda {identificatorul} NU este in stoc ")

def adauga_o_comanda_flask(id_produs, product_quantity):
    id_comanda = genereaza_id({id_produs: product_quantity})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    if id_produs in datele["produse"]:
        datele["comenzi"][id_comanda] = {
            "id_comanda": id_comanda,
            "detalii_comanda": [{id_produs : product_quantity}],
            "data_inregistrare": data_inregistrare.isoformat()
        }
    else:
        return f"produsul cu ID {id_produs} nu a fost gasit"
    scrie_datele_in_baza_de_date(datele)
    return id_comanda


def listeaza_toate_comenzile_flask():
    """
    Functia trebuie sa afiseze toate comenzile prezente in baza de date.
    Afisarea ar trebui sa contina toate informatiile comenzii
    :return:
    """
    datele = citeste_datele_din_baza_de_date()
    comenzi = datele.get('comenzi')
    if len(comenzi) > 0:
        return comenzi
    else:
        return "Nu exista comenzi"


def sterge_o_comanda_flask(id_comand):
    return sterge(id_comand, "comenzi")