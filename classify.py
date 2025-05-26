def result(data):
    total = 0

    for page_answer in data:
        for user_answer in page_answer:
            total += user_answer

    if total <= 5:
        categoria = "Validação"
    elif total <= 11:
        categoria = "Início da Escala"
    else:
        categoria = "Escala com Liberdade"

    return categoria