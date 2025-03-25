from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main() :
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    sha3_text = sha3(text)
    
    print("Mã băm SHA-3 của chuỗi '{}' là: {}".format(text.decode('utf-8'), sha3_text.hex()))
    
if __name__ == "__main__":
    main()

