#!/usr/bin/env bash

#-VARIAVEIS INFO-----------------------------------------------------#

NOME_PROGRAMA="$(basename $0 | cut -d. -f1)"
VERSAO="1.0"
AUTOR="Totem System"
CONTATO="https://github.com/leticiaNCosta18/TotemSystem"
DESCRICAO="Script para executar o .jar do projeto"
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

instalar_pacotes(){

	echo "\nInstalando e verificando todos os pacotes...\n"
	sleep 1
	sudo apt-get update && sudo apt-get upgrade -y
	[ ! -x $(which java) ] && sudo apt-get install openjdk-11-jdk
	sudo apt-get install xrdp lxde-core lxde tigervnc-standalone-server -y
	[ ! -x $(which git) ] && sudo apt-get install git-all

}
criar_urubu100(){

	echo "\nCriando usuário urubu100...\n"
	sleep 1
	sudo su
	exit
	adduser urubu100
	usermod -aG sudo urubu100
	su urubu100
	exit
	cd

}
clonar_github(){


	echo "\nClonando github e criando pastas...\n"
	cd
	wget https://github.com/leticiaNCosta18/TotemSystem/blob/main/Java/totemSistem/out/artifacts/totemSitem_jar/totemSitem.jar
	mkdir totem && mv ./totemSitem.jar totem/totemsystem.jar && cd totem
	echo "\nTudo pronto meu chefe...\n"
}

main(){


	criar_urubu100
	instalar_pacotes
	clonar_github

}

#-EXECUÇÃO-------------------------------------------------------------------------#

if [ -z "$varEXE" ]; then
	# Coloca o main do programa aqui
	main
fi
