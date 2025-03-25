import hashlib
def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(data.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Nhập chuỗi cần băm: ")
sha256_hash = calculate_sha256_hash(data_to_hash)
print("Mã băm SHA-256 của chuỗi '{}' là: {}".format(data_to_hash, sha256_hash))