from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from datetime import datetime
from pprint import pprint

from pytz import country_timezones, timezone
import hashlib


def genereaza_id(nume_produs: object, pret: object) -> object:
    hash_object = hashlib.md5(bytes(nume_produs + pret, encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def sterge(identificatorul_pt_sters, key):
    datele_noastre = citeste_datele_din_baza_de_date()
    identificatorul_pt_sters = input("intrrodu id pt sters\n")
    datele_noastre[key].pop(identificatorul_pt_sters)
    scrie_datele_in_baza_de_date(datele_noastre)

def listeaza(key):
    """
    Functia trebuie sa afiseze toti utilizatorii prezenti in baza de date.
    Afisarea ar trebui sa contina toate informatiile utilizatorilor
    """
    datele_noastre = citeste_datele_din_baza_de_date()
    listing = datele_noastre[key]
    if listing:
        pprint (listing)
    else:
        print(f"Nu exista {key}")