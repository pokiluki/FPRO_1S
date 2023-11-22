def mask_data(data, n_chr, position):
    resul = ""
    if n_chr > len(data) or n_chr < 0:
        resul = ("*"*len(data))
    
    elif n_chr == 0:
        resul  = data

    else:

        if position == "begin":
            begin = "*"*n_chr
            end = data[n_chr:]
            resul = begin + end

        if position == "end":
            begin = data[:-(n_chr)]
            end = "*"*n_chr
            resul = begin + end
    
    return resul

