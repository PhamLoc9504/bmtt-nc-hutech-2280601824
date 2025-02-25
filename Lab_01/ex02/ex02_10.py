def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string= input("Mời nhập chuỗi cần đão: ")
print("Chuỗi đã được đão: ",dao_nguoc_chuoi(input_string))