import numpy as np

# Fungsi ini mengonversi teks menjadi matriks 3x3.
def string_to_matrix(text):
    text = text.replace(" ", "").upper()  # Menghapus spasi dan mengonversi teks menjadi huruf kapital
    length = len(text)
    if length % 3 != 0:
        text += "X" * (3 - (length % 3))  # Menambahkan huruf 'X' jika panjang teks tidak kelipatan 3
    matrix = np.zeros((3, length // 3), dtype=int)  # Membuat matriks dengan ukuran yang sesuai
    i = 0
    for row in range(3):
        for col in range(length // 3):
            matrix[row][col] = ord(text[i]) - ord('A')  # Mengonversi huruf menjadi angka (0-25)
            i += 1
    return matrix

# Fungsi ini mengonversi matriks kembali menjadi teks.
def matrix_to_string(matrix):
    text = ""
    for col in range(matrix.shape[1]):
        for row in range(3):
            text += chr(matrix[row][col] + ord('A'))  # Mengonversi angka kembali menjadi huruf
    return text

# Fungsi untuk mengenkripsi teks menggunakan matriks kunci.
def encrypt(plain_text, key_matrix):
    plain_matrix = string_to_matrix(plain_text)
    result_matrix = np.dot(key_matrix, plain_matrix) % 26  # Enkripsi menggunakan modulus 26
    return matrix_to_string(result_matrix)

# Fungsi untuk mendekripsi teks menggunakan matriks kunci.
def decrypt(cipher_text, key_matrix):
    key_matrix_inv = np.linalg.inv(key_matrix)
    key_matrix_inv = np.round(key_matrix_inv * np.linalg.det(key_matrix) % 26)  # Mendapatkan matriks invers dan menggunakan modulus 26
    key_matrix_inv = key_matrix_inv.astype(int)
    
    cipher_matrix = string_to_matrix(cipher_text)
    result_matrix = np.dot(key_matrix_inv, cipher_matrix) % 26  # Dekripsi menggunakan modulus 26
    return matrix_to_string(result_matrix)

# Fungsi utama
def main():
    key_matrix_str = input("Masukkan matriks kunci 3x3 (misalnya: '0 17 8 4 11 5 0 9 0'): ")
    key_matrix = np.array([int(x) for x in key_matrix_str.split()]).reshape(3, 3)  # Mengonversi masukan matriks kunci menjadi array numpy

    plain_text = input("Masukkan kalimat yang ingin dienkripsi: ")
    encrypted_text = encrypt(plain_text, key_matrix)  # Mengenkripsi teks

    print(f"Hasil enkripsi: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key_matrix)  # Mendekripsi teks
    print(f"Hasil dekripsi: {decrypted_text}")

if __name__ == "__main__":
    main()