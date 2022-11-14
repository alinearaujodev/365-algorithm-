"""

📌 **Idade Atual**

Dado o nome e ano que nasceu, calcule quantos anos você tem atualmente


🧠 **Minha Solução:**

- :import *datetime: mod -*  importa o módulo datetime, que fornece as classes para manipulação de *datas e horas*;
- :variavel *name: str* - nome do usuário;
- :parametro *year: int* - convertir *str* para *int* com a função `int()`;
- :variavel *today: date* - fornece a data de hoje com o médoto `today()`;
- :return *idade: int* - retorno do cálculo do ano atual menos o parâmetro `year`;
- :variavel *idade: int* - recebe o valor do retorno da funçao `age()`;

"""

import datetime
def age (year: int) -> int:
    today = datetime.date.today()
    idade = today.year - year
    return idade
    

name = input("Qual seu nome? ")
year = int(input(f"Em qual ano você nasceu, {name}: "))

print("============================")
idade = age(year)
print(f"Então {name}, acredito que você tenha, {idade} anos, ou vai fazer em breve 🎂")
