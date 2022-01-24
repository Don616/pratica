#!/usr/bin/env bash

# Pega numeros pares de um loop

for i in $(seq 10); do
	if [ $(($i % 2)) -eq 0 ]; then
		echo $i
	fi
done

