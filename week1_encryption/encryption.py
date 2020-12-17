# 알파벳 수는 26개
# a의 코드는 97, z의 코드는 122
# A의 코드는 65, Z의 코드는 90

def dec(passwd, shift):

    result = ''

    for i in passwd:

        code = ord(i)

        # 빈 칸이라면
        if code == 32:
            result += ' '
        else:
            # 대문자라면
            if code >= 65 and code <= 90:
                # Z보다 큰 값이라면
                if code + shift > 90:
                    result += chr(code + shift - 26)
                else:
                    result += chr(code + shift)

            # 소문자라면
            elif code >= 97 and code <= 122:
                # z보다 큰 값이라면
                if code + shift > 122:
                    result += chr(code + shift - 26)
                else:
                    result += chr(code + shift)

    return result

def enc(s, shift):
    result = ''
    for i in s:
        code = ord(i)
        if code == 32:
            result += ' '
        else:
            # 대문자라면
            if code >= 65 and code <= 90:
                # A보다 작은 값이라면
                if code - shift < 65:
                    result += chr(code - shift + 26)
                else:
                    result += chr(code - shift)

            # 소문자라면
            elif code >= 97 and code <= 122:
                # a보다 작은 값이라면
                if code - shift < 97:
                    result += chr(code - shift + 26)
                else:
                    result += chr(code - shift)

    return result

pass1 = "Hsle ozpd l mwzddzx mpnzxp"
pass2 = "Cngz oy znk yvuxz zngz oy vrgekj hkzckkt zcu zkgsy ul krkbkt vrgekxy cozn g hgrr"
pass3 = "Patm labgxl bg max gbzam ldr"
pass4 = "Epib qa bpm vium wn i tqycql bpib gwc kivvwb tqdm eqbpwcb"
pass5 = "Ufyr kyicq y zgpb djw"


print('##################################################')
for n in range(0,50):
    print("pass1 " + str(n) + ":" + dec(pass1, n))

print('##################################################')
for n in range(0,50):
    print("pass2 " + str(n) + ":" + dec(pass2, n))

print('##################################################')
for n in range(0,50):
    print("pass3 " + str(n) + ":" + dec(pass3, n))


print('##################################################')
for n in range(0,50):
    print("pass4 " + str(n) + ":" + dec(pass4, n))

print('##################################################')
for n in range(0,50):
    print("pass5 " + str(n) + ":" + dec(pass5, n))

print('##################################################')

ans1 = "fruit"
print(enc(ans1, 15))

ans2 = "football"
print(enc(ans2, 20))

ans3 = "starts and the moon"
print(enc(ans3, 7))

ans4 = "water"
print(enc(ans4, 18))

ans5 = "feather"
print(enc(ans5, 2))


