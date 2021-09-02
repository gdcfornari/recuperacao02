class UnidadeFederativa:
    def __init__(self):
        self.sigla= ''
        self.nome= ''

    def principal(self):
        estadoSelecionado = str(input("Escreva uma sigla"))

        lista = [["Acre","AC"],
                           ["Alagoas", "AL"],
                           ["Amapá", "AP"],
                           ["Amazonas", "AM"],
                           ["Bahia", "BA"],
                           ["Ceará", "CE"],
                           ["Espiro Santo", "ES"],
                           ["Goias", "GO"],
                           ["Maranhão", "MA"],
                           ["Mato Grosso", "MT"] ,
                           ["Mato Grosso do Sul", "MS"],
                           ["Minas Gerais", "MG"],
                           ["Pará", "PA"],
                           ["Paraíba", "PB"],
                           ["Paraná", "PR"],
                           ["Pernambuco", "PE"],
                           ["Piauí", "PI"],
                           ["Rio de Janeiro", "RJ"],
                           ["Rio grande do Norte", "RN"],
                           ["Rio Grande do Sul", "RS"],
                           ["Rondônio", "RO"],
                           ["Roraima", "RR"],
                           ["Santa Catarina", "SC"],
                           ["São Paulo", "SP"],
                           ["Sergipe", "SE"],
                           ["Tocantins", "TO"],
                           ["Distrito Federal", "DF"]]

        for i in lista:
            if(estadoSelecionado == i[1]):
                print("A sigla e o estado digitados foram: " + str(i))

UnidadeFederativa().principal()
