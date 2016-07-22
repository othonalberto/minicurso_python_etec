#!/usr/bin/env python
# -*- coding: utf-8 -*-

numeros = [54, 82, 65, 98212, 51212, 413, 43, 67, 94]
maior = 0

for elemento in numeros:
	if elemento > maior:
		maior = elemento

print(maior)