#!/usr/bin/env bash
#--------------------------------------------------------------------------#

NOME_PROGRAMA=$(basename $0 | cut -d. -f1)
VERSAO="1.0"
AUTOR="Don616"
DESCRICAO="~~ EDITE AQUI COM SUA DESCRIÇÃO ~~"



#--------------------------------------------------------------------------#

case $1 in
	-i | --info)
		echo "
 ---------------------------------------------------
 Nome do Programa: $NOME_PROGRAMA
 Autor: $AUTOR
 Versão: $VERSAO
 Descrição do Programa: $DESCRICAO
 ---------------------------------------------------
 "
		;;
	* | -h | --help)
		echo "
----------------------------------------------------
 Instruções para Ajuda:
 	-h ou --help: Abre a ajuda de comandos do usuário;
	-i ou --info: Informações sobre o programa;
 
 
 
 ---------------------------------------------------
 "
		;;
esac
