#!/bin/bash

reset
echo 'Digite seu nome'
read _NOME
echo "Olá ${_NOME}, tudo bem? Qual sua idade?"
_NUM=1
while [ ${_NUM} -eq "1" ]
do
read _IDADE

if [ "${_IDADE}" -gt "65" ]
then
    echo "${_NOME} é um Idoso!"
    _NUM=0

elif [ "${_IDADE}" -gt "25" ]
then
    echo "${_NOME} é um Adulto!"
    _NUM=0

elif [ "${_IDADE}" -gt "19" ]
then
    echo "${_NOME} é um Jovem Adulto!"
    _NUM=0

elif [ "${_IDADE}" -gt "13" ]
then
    echo "${_NOME} é um Adolescente!"
    _NUM=0

elif [ "${_IDADE}" -gt "5" ]
then
    echo "${_NOME} é uma Criança!"
    _NUM=0

elif [ "${_IDADE}" -gt "0" ]
then
    echo "${_NOME} é uma Bebê!"
    _NUM=0

else
    echo "${_NOME} você forneceu uma idade inválida!"
    echo "Digite novamente sua idade: "

fi
done