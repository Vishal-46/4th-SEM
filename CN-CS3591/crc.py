def crc(dividend, divisor):
    len_divisor = len(divisor)
    padded_dividend = dividend + '0' * (len_divisor - 1)
    padded_dividend = list(padded_dividend)

    for i in range(len(dividend)):
        if padded_dividend[i] == '1':
            for j in range(len_divisor):
                padded_dividend[i + j] = str(int(padded_dividend[i + j]) ^ int(divisor[j]))

    remainder = ''.join(padded_dividend[-(len_divisor - 1):])
    return remainder


data = '1101011'
divisor = '10011'
remainder = crc(data, divisor)
print("CRC Remainder:", remainder)

transmitted_data = data + remainder
print("Transmitted Data:", transmitted_data)
