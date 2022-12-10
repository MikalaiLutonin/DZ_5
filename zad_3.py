
# Задача_3 ======================================================================================================================================================
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(s):
	encoding = "" 
	i = 0
	while i < len(s):
		count = 1
		while i + 1 < len(s) and s[i] == s[i + 1]:
			count = count + 1
			i = i + 1
		encoding += str(count) + s[i]
		i = i + 1
	return encoding

def decode(s):
    decoded_message = ""
    i = 0
    j = 0
    while (i <= len(s) - 1):
        run_count = int(s[i])
        run_word = s[i + 1]
        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message


data = open('input_data.txt', 'r')
for i in data:
    print(i)
    s = i
data.close()

enc = encode(s)

print(enc)

dec = decode(enc)

with open('output_data.txt', 'w') as data:  
    data.write(dec)

print(dec)