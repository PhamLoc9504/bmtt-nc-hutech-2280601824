class PlayfairCipher:
    def __init__(self):
        self.matrix = []

    def create_playfair_matrix(self, key):
        # Chuẩn hóa khóa: thay "J" bằng "I", chuyển thành chữ in hoa, loại bỏ ký tự trùng lặp
        key = key.replace("J", "I").upper()
        key_set = []
        # Loại bỏ ký tự trùng lặp trong key, giữ nguyên thứ tự
        for char in key:
            if char.isalpha() and char not in key_set:
                key_set.append(char)
        
        # Bảng chữ cái, bỏ chữ "J"
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        remainder = [letter for letter in alphabet if letter not in key_set]
        
        # Tạo chuỗi hoàn chỉnh để tạo ma trận
        matrix_key = key_set + remainder
        
        # Cắt chuỗi thành ma trận 5x5
        self.matrix = []
        for i in range(0, 25, 5):  # Chỉ lấy tối đa 25 ký tự, bước nhảy 5
            self.matrix.append(matrix_key[i:i+5])
        
        return self.matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return (row, col)
        return None

    def encrypt(self, plain_text, key):
        # Tạo ma trận dựa trên khóa
        self.create_playfair_matrix(key)
        
        # Chuẩn hóa văn bản: thay "J" bằng "I", chuyển thành chữ in hoa, loại bỏ ký tự không phải chữ cái
        plain_text = plain_text.replace("J", "I").upper()
        plain_text = "".join(c for c in plain_text if c.isalpha())
        
        # Xử lý các cặp chữ cái giống nhau và đảm bảo độ dài chẵn
        processed_text = ""
        i = 0
        while i < len(plain_text):
            if i + 1 < len(plain_text):
                if plain_text[i] == plain_text[i + 1]:
                    processed_text += plain_text[i] + 'X'
                    i += 1
                else:
                    processed_text += plain_text[i] + plain_text[i + 1]
                    i += 2
            else:
                processed_text += plain_text[i] + 'X'
                i += 1
        
        encrypted_text = ""
        for i in range(0, len(processed_text), 2):
            pair = processed_text[i:i + 2]
            
            # Tìm tọa độ của hai ký tự
            row1, col1 = self.find_letter_coords(self.matrix, pair[0])
            row2, col2 = self.find_letter_coords(self.matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                encrypted_text += self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:  # Cùng cột
                encrypted_text += self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
            else:  # Khác hàng và khác cột
                encrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        return encrypted_text

    def decrypt(self, cipher_text, key):
        # Tạo ma trận dựa trên khóa
        self.create_playfair_matrix(key)
        
        # Chuẩn hóa văn bản: chuyển thành chữ in hoa
        cipher_text = cipher_text.upper()
        
        decrypted_text = ""
        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i + 2]
            
            # Tìm tọa độ của hai ký tự
            row1, col1 = self.find_letter_coords(self.matrix, pair[0])
            row2, col2 = self.find_letter_coords(self.matrix, pair[1])

            if row1 == row2:  # Cùng hàng
                decrypted_text += self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:  # Cùng cột
                decrypted_text += self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
            else:  # Khác hàng và khác cột
                decrypted_text += self.matrix[row1][col2] + self.matrix[row2][col1]

        return decrypted_text
