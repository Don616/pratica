#!/bin/bash
reset

echo "Digite a nota que deseja consultar:"


_CONTROLER=1
while [ ${_CONTROLER} -eq 1 ]
do
read _NOTA


if [ ${_NOTA} -gt "10" ]
then
    echo "Digite um valor válido!"

elif [ ${_NOTA} -gt "9" ]
then
    echo "Sua nota foi Excelente!"
    _CONTROLER=0

elif [ ${_NOTA} -gt "6" ]
then
    echo "Sua nota foi Boa"
    _CONTROLER=0

elif [ ${_NOTA} -gt "4" ]
then
    echo "Sua nota foi Regular"
    _CONTROLER=0

elif [ ${_NOTA} -ge "0" ]
then
    echo "Sua nota foi Ruim"
    _CONTROLER=0

else
    echo "Digite um valor válido!"

fi
done



