# -*- coding: utf-8 -*-
"""Encryptation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QYF-0rjPX4fGdojzpwG---XaIytHvwPw
"""

"""Cesar encryptation"""
print("Escribe A si quieres encriptar")
print("Escribe B si quieres decifrar")
print("Escribe Exit para salir")
option=input(": ") #Se escoje cuál instancia del programa se ejecutará


alphabet= "!$012345AaáBbCcDdEeéFfGgHhIiíJjKkLl:MmNnO&oóPp;q][RrS€sTtUuúVvWwXxYyZz‘)“”( ?\'\",.6789’-" #Alfabeto...

if option.lower()=='a':
  text_e=input('Introduce el texto a encriptar: ')
  """ En caso que se quiera limpiar el texto, se activan las siguientes lineas, 
  y se sacan los caracteres del alfabeto
  text_e=text_e.replace(",","")
  text_e=text_e.replace(".","")
  text_e=text_e.replace(","")
  """

  for char in text_e:# Characters in text en minúsculas
    p=(alphabet.index(char)+3)# Encriptado romano, se desplazan 3.
    if p<len(alphabet):# Cuando se llega al límite de la lista. Aunque los index vayan del desde 0, el len empieza desde 1.
      print(alphabet[p], end="")
    else:
      p-=len(alphabet)#Cuando se pasa de la lista, para empiece del inicio.
      print(alphabet[p], end="")
if option.lower()=='b':
  text_u=input('Introduce el texto a Decifrar: ')
  for char in text_u:
    p=(alphabet.index(char)-3)#Traducción de la encriptación.
    print(alphabet[p], end="")
if option.lower()=='exit':
  print("fin")