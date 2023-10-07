import datetime
def auxilio(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento  

    if 4 <= idade <= 16:
        return True
    else:
        return False


def resultado(res):
    if res:
        print("O direito ao auxílio escolar é Autorizado.")
    else:
        print("O direito ao auxílio escolar é Negado.")

ano_nascimento = int(input("Digite o ano de nascimento: "))
resultado(auxilio(ano_nascimento))
