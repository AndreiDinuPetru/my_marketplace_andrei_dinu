import json
from baza_de_date.functii import citeste_datele_din_baza_de_date, scrie_datele_in_baza_de_date
import hashlib
from datetime import datetime
from pprint import pprint
from produse.functii import adauga_un_produs
from common.util import genereaza_id , sterge , listeaza

from pytz import country_timezones, timezone
#
# def introducere_comanda():
#     datele_noastre = citeste_datele_din_baza_de_date()
#     id_utilizator = input("Introduceti id_utilizator.\n")  # introducerea produsului
#     id_comanda = input("Introduceti comanda de adaugat -id_comanda.\n")
#     nume_utilizator = datele_noastre["utilizatori"][id_utilizator]
#     nume_comanda = datele_noastre["comenzi"][id_comanda]
#     nume_utilizator.update ({"comanda_facuta" : nume_comanda})
#     scrie_datele_in_baza_de_date(datele_noastre)
#
#
#
