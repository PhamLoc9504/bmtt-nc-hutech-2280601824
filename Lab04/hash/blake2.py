import hashlib 
def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.hexdigest()

def main() :
    text = input("Nhập chuỗi cần băm: ").encode('utf-8')
    blake2_text = blake2(text)
    
    print("Mã băm BLAKE2 của chuỗi '{}' là: {}".format(text.decode('utf-8'), blake2_text))
    
if __name__ == "__main__":
    main()