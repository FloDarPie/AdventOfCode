def snafu_to_decimal(snafu):
    snafu_values = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
    decimal = 0
    for i, char in enumerate(reversed(snafu)):
        decimal += snafu_values[char] * (5 ** i)
    return decimal

def decimal_to_snafu(decimal):
    snafu_values = {0: '0', 1: '1', 2: '2', 3: '=', 4: '-'}
    snafu = ''
    while decimal > 0:
        snafu = snafu_values[decimal % 5] + snafu
        decimal = decimal // 5 + (1 if decimal % 5 > 2 else 0)
    return snafu if snafu else '0'



file = open('day25input.txt', 'r')
content = file.read()
file.close()

snafu_numbers = content.split("\n")[:-1]
decimal_sum = sum(snafu_to_decimal(snafu) for snafu in snafu_numbers)
snafu_sum = decimal_to_snafu(decimal_sum)

print(f"The SNAFU number to supply to Bob's console is: {snafu_sum}")
