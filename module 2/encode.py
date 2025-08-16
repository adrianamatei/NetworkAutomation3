#fiecare caracter are asociat un numar si fiecare numar are asociat un caracter
#cele doua functii de convertit
number_a=ord('a') #ne da codul ASCII pentru a
print(number_a)

number_ascii=chr(97)
print(number_ascii)

character_254=chr(254)
print(character_254)
print("_-----------------_")

#mai avem si alte operatii pe biti
#print(10 ^ 2)  #face XOR
# 1 0 1 0
# 0 0 1 0
# 1 0 0 0

enc= 10^5
print(enc)
dec=enc^5 #daca fac de doua ori ma intorc la acelasi numar
print(dec)
# putem sa luam un carcater , sa luam o cheie , sa obtinem un alt caracter


text="hello python"
key=129
enc=[]

print(text)
for letter in text:
    c=chr(ord(letter) ^ key)
    enc.append(c)

enc_text=''.join(enc)
print(enc_text)

dec=[]
for letter in enc_text:
    d=chr(ord(letter) ^ key)
    dec.append(d)

dec_text=''.join(dec)
print(dec)


#sa ne gandim la o metoda de cripatare si sa i aratam o varianta
