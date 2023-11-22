p_amount = float(input())
int_rate = float(input())
p_freq = float(input())

int1 = 1 + (int_rate/p_freq)

int2 = p_freq*2

int3 = int1**int2

out = p_amount * int3

out = round(out, 3)
#out = p_amount*((1+(int_rate/p_freq))**(int_rate*2))

print(out)