from datetime import date


def idade(data_nascimento, hoje=date.today()) -> int:
    anos = hoje.year - data_nascimento.year
    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        anos = anos - 1
    return anos


def dias_que_faltam(data_futura, hoje=date.today()) -> int:
    return (data_futura - hoje).days


# print(idade(date(2008, 5, 12)))
# print(dias_que_faltam(date(2026, 12, 31)))
