import pypyodbc
import json
import env

tiendas = ['67']
invalidStatusCodes = [99, 100, 102]

def connectToDb(storeNumber):
  cnxn = pypyodbc.connect(f"Driver=SQL Server;Server=10.10.10.{storeNumber};Database={env.databaseName};uid={env.databaseUser};pwd={env.databasePassword}")
  return cnxn
