#!/usr/bin/env bash

#-VARIAVEIS INFO-----------------------------------------------------#

NOME_PROGRAMA="$(basename $0 | cut -d. -f1)"
VERSAO="1.0"
AUTOR="Don616"
CONTATO="https://github.com/Don616"
DESCRICAO="Mostra os repositórios de um usuario no Github"
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


#-TESTES--------------------------------------------------------------------------#

[ ! -x $(which lynx) ] && echo 'sim'

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
	echo "Digite o usuário do Github que deseja mostrar os repositórios: "
	read USERGITHUB
	echo " "
	varSTATUSCODE="$(curl -Is https://github.com/$USERGITHUB | head -1 | cut -d' ' -f2)"
	if [ $varSTATUSCODE -eq 200 ]; then

		echo "Buscando repositórios encontrados para o usuario $USERGITHUB..."
		sleep 1
		echo " "
		lynx -source "https://github.com/$USERGITHUB" | grep '<span class="repo" title="' | cut -d'"' -f4
		echo " "
	else
		echo " "
		echo "Usuario não encontrado"
		echo " "
	fi
fi