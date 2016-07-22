#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import os

sorteado = random.randint(1,50)
chute = ''
contador = 0

while chute != sorteado:
	chute = int(input("Chute: "))
	contador += 1
	if chute == sorteado:
		print("\n\nParabéns!")
	elif chute > sorteado:
		print("Alto.\n")
	else:
		print("Baixo.\n")