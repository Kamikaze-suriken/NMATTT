from encrypt import encrypt
from decrypt import decrypt
import sys
def menu():
    print("USEAGE: python main [command]")
    print("\t\-h\t:\tHelp menu")
    print("\t\tdecrypt\t:\tDecrypt with public key")
    print("\t\tencrypt\t:\tEncrypt with input public key")
    print("\t\tencrypt -r\t:\tEncrypt with random public key")
if __name__ == "__main__":
    if len(sys.argv)>= 2:
        if sys.argv[1] == '-h':
            menu()
        elif sys.argv[1] == 'decrypt':
            cipher = input("Input cipher text(hex code):")
            n = int(input("Input public key n:"))
            e = int(input("Input public key e:"))
            print("Decrypt text : ", decrypt.decrypt(decrypt, cipher, n, e))
        elif sys.argv[1] == 'encrypt':
            if len(sys.argv) == 3 and sys.argv[2] == "-r":
                plain = input("Input plain text:")
                print("Encrypt hex code:",encrypt.encrypt_r(encrypt, plain))
            elif len(sys.argv) == 2:
                plain = input("Input plain text:")
                n = int(input("Input public key n:"))
                e = int(input("Input public key e:"))
                print("Encrypt hex code:", encrypt.encrypt(encrypt, plain, n, e))
            else:
                print("Unknown command")
                menu()
        else:
            print("Unknown command")
            menu()
    else:
        print("Unknown command")
        menu()
