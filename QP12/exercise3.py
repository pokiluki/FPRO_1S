from cards import create_deck, deal_hands, choose, player_order
import random


def play(seed_value) -> None:
    random.seed(seed_value)
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    wins = [0, 0, 0, 0]
    while hands[start_player]:
        lista = []
        for name in turn_order:
            card = choose(hands[name])
            lista.append(card_value(card))
            hands[name].remove(card)
        max1 = max(lista)
        for i in range(len(lista)):
            if lista[i] == max1:
                wins[i] += 1
    max2 = max(wins)
    res = ""
    if wins[turn_order.index("P1")] == max2:
        res += "P1 "
    if wins[turn_order.index("P2")] == max2:
        res += "P2 "
    if wins[turn_order.index("P3")] == max2:
        res += "P3 "
    if wins[turn_order.index("P4")] == max2:
        res += "P4 "

    return res[:-1]


def card_value(card):
    val = 0
    if card[1].isdigit():
        val += int(card[1])
    elif card[1] == "A":
        val += 11
    else:
        val += 10
    if card[0] == "♠" or card[0] == "♣":
        val *= 2
    return val
