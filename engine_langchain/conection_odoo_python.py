import xmlrpc.client
import psycopg2
import sys
url = 'http://44.201.4.61:8069/'
username = 'admin'
password = 'admin'
db = 'prueba'
common =xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
print('USER',uid)
print('UID ',uid)
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
records = models.execute_kw(db, uid, password,
    'crm.lead',  # Nombre del modelo (tabla)
    'search_read',  # Método de búsqueda y lectura
    [[('expected_revenue', '>', 35000)]],  # Criterio de búsqueda (en este caso, vacío para obtener todos los registros)
    {'fields': ['contact_name','expected_revenue','stage_id']}  # Campos a recuperar
)

# Imprimir los registros obtenidos
for record in records:
    print("Contact Name:", record['contact_name'])
    print("Expected Revenue:", record['expected_revenue'])
    print("Stage:", record['stage_id'])
    print("-----------------------------")