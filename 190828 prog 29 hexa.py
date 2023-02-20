hex_in = input('Enter hex: ').strip()

hex_digit = '0123456789ABCDEF'
decimal_out = 0
p = len(hex_in)-1

for d in hex_in :
    if d in hex_digit :
        #k = 0
        #while k <= p :

        r = hex_digit.find(d)

        decimal_out += r*(16**(p))

        p -= 1
            
            #decimal_out += int(hex_in[k])*(16**(p-k))

            #decimal_out += int(hex_digit[k]) * 16**k
        #k += 1

    else :
        print ('Invalid hexadecimal number')
        exit(-1)

print(decimal_out)
