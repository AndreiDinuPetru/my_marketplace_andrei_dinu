"""

Utilizatorii ar trebui sa aiba structura:
("id_utilizator": {
    "nume": "Numele" - string,
    "email": "EmailAddress" - string,
    "data_inregistrare": "DataInregistrare" - string,
})

"""
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
import hashlib
from datetime import datetime
from pprint import pprint
from common.util import genereaza_id , sterge , listeaza
from pytz import country_timezones, timezone

#
# def adauga_un_utilizator():
#     """
#     Introdu de la tastatura cu textul 'Introduceti numele produsului de adaugat: '
#         Daca limitele lungimii numelui unui produs e intre 1 si 50 caractere
#         Daca nu se incadreaza printati 'Nume Invalid - Lungimea numelui trebuie sa fie intre 1 si 50 de caractere'
#     Introdu de la tastatura cu textul 'Introduceti mailul produsului de adaugat: '
#     Generam ID-ul unic produsului
#     Generam data inregistrarii
#     Citim din baza de date
#     Generam structura dictionarului
#     Scriem in baza de date
#     """
#     nume, email = "" , ""
#     while len(nume) < 1 or len(nume)>50:
#         nume = input("Introduceti numele utilizatori de adaugat:\n")
#         if len(nume) < 1 or len(nume)>50:
#             print("Nume invalid, trebuie sa aiba intre 1 si 50 de caractere")
#     while len(email) < 1:
#         email = input("Introduceti mailul utilizator de adaugat: \n")
#     id_utilizator = genereaza_id(nume, email)
#     data_inregistrare = datetime.now(tz = timezone(country_timezones.get("RO")[0]))
#     datele_noastre = citeste_datele_din_baza_de_date()
#     datele_noastre["utilizatori"][id_utilizator] = {
#         "nume":nume,
#         "email":email,
#         "data_inregistrare":data_inregistrare.isoformat()
#     }
#     scrie_datele_in_baza_de_date(datele_noastre)
#
#
# def listeaza_toti_utilizatorii():
#     """
#     Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
#     Afisarea ar trebui sa contina toate informatiile utilizatorilor
#     """
#     listeaza("utilizatori")
#
# def sterge_un_utilizator():
#     utilizator_pt_sters = input("intrrodu id pt sters\n")
#     sterge(utilizator_pt_sters, "utilizatori")

def adauga_un_utilizator_flask(user_name, email_address):
    id_utilizator = genereaza_id({user_name: email_address})
    data_inregistrare = datetime.now(tz=timezone(country_timezones.get("RO")[0]))
    datele = citeste_datele_din_baza_de_date()
    datele["utilizatori"][id_utilizator] = {
        "nume": user_name,
        "email": email_address,
        "data_inregistrare": data_inregistrare.isoformat()
    }
    scrie_datele_in_baza_de_date(datele)
    return id_utilizator


def listeaza_toti_utilizatorii_flask():
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    :return:
    """
    datele = citeste_datele_din_baza_de_date()
    utilizatori = datele.get('utilizatori')
    if len(utilizatori) > 0:
        return utilizatori
    else:
        return "Nu exista utilizatori"


def sterge_un_utilizator_flask(user_id):
    return sterge(user_id, "utilizatori")