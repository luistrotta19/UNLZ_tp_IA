# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 20:42:01 2023

@author: Luis
"""
'''
Introducción:
Ejemplos de Condicionales

Los condicionales if, else, elif en python se utilizan para ejecutar 
una instrucción en caso de que una o más condiciones se cumplan! 
Un condicional es como el momento en que se debe tomar una decisión,
 en nuestro programa o script. 
 Dependiendo la decisión que se tome ocurrirá una cosa u otra, o ninguna.
'''
nota_fisica=2

if 2 < 3.0:
    print('su resultado fue BAJO')
elif  2 >= 3 and 2 <=4:
           print('su resultado fue BASICO')
else:
               print('su resultado fue EXCELENTE')
            
#%%

a = 2 + 3
if a == 4: #condicion si a es exactamente cuatro, entonces(:)
    print ("A es igual a cuatro") # Imprimir
elif a == 5:
    print ("A es igual a cinco")
elif a == 6:
    print ("A es igual a seis")
else:
    print ("No se cumple la condición")
#Resultado: "A es igual a cinco"
#%%
#Funciones en Python

#%%
def suma(a,b,g):
    c = a+b+g
    return c

resultado = suma(3,5,6)

print(resultado)

#%%
'''
Pandas
Pandas es una herramienta de manipulación y análisis de datos de código abierto rápida, 
potente, flexible y fácil de usar,construida sobre el lenguaje de programación Python .

DataFrame
Un dataframe es una herramienta de organización de datos que se utiliza para almacenar 
cualquier tipo de información. 
Pero cuando se habla de Data Science, estos suelen contener información relevante del Big Data. 
Es utilizado por los científicos de datos para clasificar 
la información que necesitan según los objetivos establecidos por la empresa

'''

#%%
import pandas as pd


base_datos_mineria = pd.read_excel('Matrices_BaseDatos/Matrices Grupo Mineria_tp.xlsx')

base_datos_mineria.iat[2,2]

#%%
import ejercicio
ejercicio.lista_camion_mineria[6]

# %%
'''
Análisis Minería
Derivabilidad Minería

ejercicio.lista_camion_mineria [6]
Out[13]: 
{'Origen': 'LA CARLOTA',
 'ID origen': 3,
 'Destino': 'CABA',
 'ID destino': 2,
 'Carga': 1325674,
 'Distancia': 750}

Origen	    ID origen	Destino	ID destino	Carga	Distancia
LA CARLOTA	  3	        CABA	    2	   1325674	  750

#Análisis de las distancias
'''
#%%

if 300 > 750 >= 200:
    print('hola')
    
print('chau')    

#%%

if 400 > 750 >= 300:
    print('hola')
    
print('chau')    

#%%

if 500 > 750 >= 400:
    print('hola')
    
print('chau')    

#%%

if 750 >= 500:
    print('hola')
    
print('chau')   

#%% 

''' Análisis de las cargas Mineria

criterio_mineria.iat[2,0]
Out[18]: 44670

criterio_mineria.iat[3,0]
Out[19]: 7000

'''
#%%

if 44670 > 1325674 >= 7000:
    print('hola')
    
print('chau')    


#%%
if 82333 > 1325674 >= 44670:
    print('hola')
    
print('chau')    

#%%
'''
criterio_mineria.iat[0,0]
Out[6]: 120000

criterio_mineria.iat[1,0]
Out[7]: 82333
'''


if 120000 > 1325674 >= 82333:
    print('hola')
    
print('chau')    


#%%
if  1325674 >= 120000:
    print((1325674*0.51))
    
print('chau')    

#%%
'''
Completar las comprobaciones de las derivabilidades faltantes,
de Minería y Granos.
'''
#%%






