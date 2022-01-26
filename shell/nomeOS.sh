#!/usr/bin/env bash

#-VARIAVEIS BASICAS-----------------------------------------------------#

NOME_PROGRAMA=$(basename $0 | cut -d. -f1)
VERSAO="1.0"
AUTOR="Don616"
DESCRICAO=" Mostra o modelo do computador e a geração do processador + 
o sistema operacional onde ele está rodando."
varEXE=$1 # Se não tiver parametros ela executa normal

#-VARIAVEIS PARAMETRO----------------------------------------------------#

varINFO="
Nome do Programa: $NOME_PROGRAMA
Autor: $AUTOR
Versão: $VERSAO
Descrição do Programa: $DESCRICAO
"
varHELP="
Instruções para Ajuda:
	-h ou --help: Abre a ajuda de comandos do usuário;
	-i ou --info: Informações sobre o programa;
"
varMODEL=$(cat /proc/cpuinfo | grep "model name" | cut -d: -f2 | head -1)
varGERACAO=$(cat /proc/cpuinfo | grep "model name" | cut -d: -f2 | cut -d' ' -f4 | cut -d- -f2 | cut -b 1 | head -1 )
varNOME_OS=$(cat /etc/*-release | grep "PRETTY_NAME" | cut -d= -f2 | sed 's/"//g')

#-LOOP PARA RODAR MAIS PARAMETROS---------------------------------------------------#

while test -n "$1"; do

	case $1 in

		-i | --info) echo "$varINFO" 												;;		
		-h | --help) echo "$varHELP" 												;;
				  *) echo "\nComando inválido. Digite -h ou --help para ajuda\n"	;;

	esac
	shift

done

#-EXECUÇÃO-------------------------------------------------------------------------#

if [ -z "$varEXE" ]; then
	echo "
Usuário: $USER
Sistema Operacional: $varNOME_OS
Modelo: $varMODEL
Geração: $varGERACAOª Geração
	"
fi