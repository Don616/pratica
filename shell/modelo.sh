#!/usr/bin/env bash

#-VARIAVEIS BASICAS-----------------------------------------------------#

NOME_PROGRAMA=$(basename $0 | cut -d. -f1)
VERSAO="1.5"
AUTOR="Don616"
DESCRICAO="~~ EDITE AQUI COM SUA DESCRIÇÃO ~~"
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
	echo "Coloca o main do programa aqui"
fi