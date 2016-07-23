#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

sorteado = random.randint(1,50)
chute = ''

while chute != sorteado:
	chute = int(input("Chute: "))
	if chute == sorteado:
		print("\n\nParabéns!")
	elif chute > sorteado:
		print("Alto.\n")
	else:
		print("Baixo.\n")