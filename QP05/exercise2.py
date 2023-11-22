def camel_case(phrase):
    resul = phrase.title()
    for i in resul:
        w_spaces = ""
        if not i.isalpha():
            resul = resul.replace(i, "")

    
    first = resul[0].lower()
    resul = resul[1:]
    final = str(first) + str(resul)


    return final
