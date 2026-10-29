import pandas as pd
import numpy as np

serie_tablabilletes=["andrea","viviana","adrian","fernanda","aurora","alex","michelin"]
print("----serie listado de amigos NC 1374")
amigos=pd.Series(serie_tablabilletes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("----serie listado valor de billetes MX NC 1374")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","docientos","quinientos","mil"]
print("----serie listado nombre y valor de billetes MX NC 1374")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)
# diccionario dataframe 
# diccionario de valor monedas y nombre 
print("datos de diccionario a DataFrame en pandas")
dicc_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","docientos","quinientos","mil"]

}

tablabilletes=pd.DataFrame(dicc_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("casa de cambio de cristopher Lopez NC 1374")