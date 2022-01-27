#!/usr/bin/env bash

#-VARIAVEIS INFO-----------------------------------------------------#

NOME_PROGRAMA="$(basename $0 | cut -d. -f1)"
VERSAO="1.5"
AUTOR="Don616"
CONTATO="https://github.com/Don616"
DESCRICAO="Cria relatórios diários para o usuário"
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
varFILE="/home/$USER/relatorio.md"

#-TESTES--------------------------------------------------------------------------#

if [ ! -e "$varFILE" ]; then touch $varFILE; fi

#-LOOP PARA RODAR MAIS PARAMETROS---------------------------------------------------#

while test -n "$1"; do

	case $1 in

		-i |  --info)  	echo "$varINFO" 											;;		
		-h |  --help)  	echo "$varHELP"												;;
		-d | --debug)	bash -x $0													;;
				   *) 	echo "\nComando inválido. Digite -h ou --help para ajuda\n"	;;

	esac
	shift

done
#-FUNÇÕES--------------------------------------------------------------------------#



#-EXECUÇÃO-------------------------------------------------------------------------#

if [ -z "$varEXE" ]; then

	echo " " >> $varFILE
	date "+%A, %d %B %Y" >> $varFILE
	echo " " >> $varFILE
	vim $varFILE

fi