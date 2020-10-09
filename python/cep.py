import requests

def retorna_cep(num):
    while "-" in num:
        num = input("Inválido: Digite sem o hífen: ")
    while not num.isnumeric():
        num = input("Inválido. Digite somente números: ")
    while not len(num) == 8:
        num = input("Inválido. O 'CEP' deve conter apenas 8 digitos. Digite novamente: ")

    req = requests.get("https://viacep.com.br/ws/{}/json/".format(num))
    json_list = req.json()
    saida = ""
    for k, v in json_list.items():
        saida += (f"{k.title()}: {v}\n")
    print()
    return print(saida)


if __name__ == "__main__":
    cep = input("Digite um CEP: ")
    retorna_cep(cep)