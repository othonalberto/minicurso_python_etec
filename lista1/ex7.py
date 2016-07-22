#!/usr/bin/env python
# -*- coding: utf-8 -*-

numeros = [54, 82, 65, 98212, 51212, 413, 43, 67, 94]

pares = []
impares = [] 

for x in numeros:
	if x % 2 == 0:
		pares.append(x)
	else:
		impares.append(x)

print("Pares: {0}" .format(pares))
print("Ímpares: {0}" .format(impares))
