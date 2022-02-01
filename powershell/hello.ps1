# =====================================================================
#
#    Comando para habilitar scripts:
#    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine
# 
# =====================================================================
# 
#
#    Nome do Programa: Hello World!
#    Criado por: Don616
#    Versão: 1.0
#    Contato: https://github.com/Don616
#    Descrição: Primeiro programa em PS1, para fins de teste.
# 
# 
# =====================================================================
# 

#    Testando primeiro script PowerShell

Write-Output "`nHello World!`n"
$nome = Read-Host "Digite seu nome"
Write-Output "`n==================`n"
Write-Output "Bem vindo ao mundo PowerShell, $nome!"
