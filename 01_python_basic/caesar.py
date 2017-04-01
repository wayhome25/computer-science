def caesar(target, magic_num, decode = False):
    if decode:
        magic_num = -magic_num
    ascii_dec_list = [ord(i) + magic_num for i in list(target)]
    ascii_char_list = [chr(i) for i in ascii_dec_list]
    return ''.join(ascii_char_list)


while True:
    magic_num = int(input('암호화를 위한 비밀숫자를 입력하세요 : '))
    target = input("암호화를 할 문자를 입력하세요 : ")
    encrypted_result = caesar(target, magic_num)
    decrypted_result = caesar(encrypted_result, magic_num, True)
    print("암호화된 문자:", encrypted_result)
    print("복호화된 문자:", decrypted_result)
    exit = input("종료 하시려면 'q'를 입력하세요 : ").lower()
    if 'q' in exit:
        break
