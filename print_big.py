def print_big(letter):
    ident_determination = []
    ident_a = ['00100', '01010', '11111', '10001', '10001']
    ident_b = ['11100', '10100', '11111', '10001', '11111']
    ident_c = ['11111', '10000', '10000', '10000', '11111']
    ident_d = ['11110', '10001', '10001', '10001', '11110']
    ident_e = ['11111', '10000', '11111', '10000', '11111']
    ident_f = ['11111', '10000', '11111', '10000', '10000']
    ident_g = ['11111', '10000', '10011', '10001', '11111']
    ident_h = ['10001', '10001', '10101', '10001', '10001']
    ident_i = ['01110', '00100', '00100', '00100', '01110']
    ident_j = ['11111', '00100', '00100', '10100', '01000']
    ident_k = ['10001', '10010', '10100', '10010', '10001']
    ident_l = ['10000', '10000', '10000', '10000', '11111']
    ident_m = ['10001', '10101', '10001', '10001', '10001']
    ident_n = ['10001', '11001', '10101', '10011', '10001']
    ident_o = ['01110', '10001', '10001', '10001', '01110']
    ident_p = ['11111', '10001', '11111', '10000', '10000']
    ident_r = ['11111', '10001', '11111', '10010', '10001']
    ident_s = ['01111', '10000', '01110', '00001', '11110']
    ident_t = ['11111', '00100', '00100', '00100', '00100']
    ident_u = ['10001', '10001', '10001', '10001', '01110']
    ident_v = ['10001', '10001', '10001', '01010', '00100']
    ident_w = ['10001', '10001', '10101', '11011', '10001']
    ident_x = ['10001', '01010', '00100', '01010', '10001']
    ident_z = ['11111', '00010', '00100', '01000', '11111']
    index = 0
    step = 0
    space = ' '
    star = '*'
    final_list = []
    list_alphabet = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    list_alphabet = list(alphabet)
    letter = letter.lower()
    for i in list_alphabet:
        if list_alphabet[index] == letter:
            break
        index += 1
    ident_determination.append('ident_')
    ident_determination.append(letter)
    ident_formed = ''.join(ident_determination)
    s = eval(ident_formed)
    for c in s:
        for x in s[step]:
            if x == '0':
                final_list.append(space)
            if x == '1':
                final_list.append(star)
        step += 1
    final_string = ''.join(final_list)
    print(final_string[0:5])
    print(final_string[5:10])
    print(final_string[10:15])
    print(final_string[15:20])
    print(final_string[20:25])
