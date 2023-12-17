def tic_tac_toe(board, player):
    rows = board.split('\n')
    size = len(rows)

    for i in range(size):
        if rows[i].count(player) == size - 1 and rows[i].count(' ') == 1:
            col = rows[i].index(' ')
            return f"{chr(65 + i)}{col + 1}"

    for i in range(size):
        column = ''.join([rows[j][i] for j in range(size)])
        if column.count(player) == size - 1 and column.count(' ') == 1:
            row = column.index(' ')
            return f"{chr(65 + row)}{i+ 1}"

    diagonal = ''.join([rows[i][i] for i in range(size)])
    if diagonal.count(player) == size - 1 and diagonal.count(' ') == 1:
        index = diagonal.index(' ')
        return f"{chr(65 + index)}{index + 1}"

    reverse_diagonal = ''.join([rows[i][size - 1 - i] for i in range(size)])
    if reverse_diagonal.count(player) == size - 1 and reverse_diagonal.count(' ') == 1:
        index = reverse_diagonal.index(' ')
        return f"{chr(65 + (index))}{size - index}"





