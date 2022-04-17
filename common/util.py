from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from datetime import datetime
from pprint import pprint
from flask import Flask
from pytz import country_timezones, timezone
import hashlib


import hashlib
import json
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
from flask import Response

def genereaza_id(detalii_comanda):
    hash_object = hashlib.md5(bytes(json.dumps(detalii_comanda), encoding='UTF-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def sterge(identificator_de_sters, key):
    datele = citeste_datele_din_baza_de_date()
    if datele[key].get(identificator_de_sters):
        datele[key].pop(identificator_de_sters)
        scrie_datele_in_baza_de_date(datele)
        return 200, f"User or product: {identificator_de_sters} has been successfully deleted"
        # return Response(status=200, response=f"User: {identificator_de_sters} has been successfully deleted") # a doua varianta
    else:
        return 404, f"User: {identificator_de_sters} does not exist in the database"
        # return Response(status=404, response=f"User: {identificator_de_sters} does not exist in the database") # a doua varianta
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