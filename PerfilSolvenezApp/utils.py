import random
from django.db import connection

def transferir_fondos(referencias, descripciones, tipo_transacciones, emisor_id, receptor_id, montos):
    with connection.cursor() as cursor:
        cursor.execute("SELECT transferir_fondos(%s,%s, %s, %s, %s, %s)", [referencias, descripciones, tipo_transacciones, emisor_id, receptor_id, montos])

