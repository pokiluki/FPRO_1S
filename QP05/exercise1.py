def rm_letter_rev(ch, s):
    resul = ""
    for c in s:
        if c != ch:
            resul = c + resul
    
    return resul


