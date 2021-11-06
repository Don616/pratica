#!/bin/bash

echo "Bem vindo ao programa!"
read -p "Digite seu nome: " NOME
echo "Olá, $NOME!"
read -p "Digite seu ano de nascimento: " NASCIMENTO
ANO=$(echo ${NASCIMENTO} | cut -d"/" -f3)
ANO_ATUAL=$(date +%Y)
IDADE=$(echo "$ANO_ATUAL - $ANO" | bc -l)
echo "${NOME}, você tem ${IDADE} anos!" 

MENSAGEM="Ok, vá à merda!"

read -p "Deseja ler nossa mensagem? (y/n) " CONFIRM1
if [ ${CONFIRM1} = "y" ]
then echo ${MENSAGEM}
else echo "Então vai toma no cu!"
fi

