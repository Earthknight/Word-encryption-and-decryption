alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(t,s):
    text_list =[]
    cipher_text =[]
    for n in t:
      text_list += n
    for n in text_list:
      j=0
      d=0
      f=26
      for m  in alphabet:
        if m == n:
          d=j+s
          print(d)
          if d >= f:
            d -= f
            cipher_text += alphabet[d]
          else:
            cipher_text += alphabet[d]
        j += 1
    print(f"{''.join(cipher_text)}")

def decrypt(t,s):
    text_list =[]
    decipher_text =[]
    for n in t:
      text_list += n
    for n in text_list:
      j=0
      for m  in alphabet:
        if m == n:
          print(j)
          decipher_text += alphabet[j-s]
        j += 1
    print(f"{''.join(decipher_text)}")
rerun = True
while rerun == True :
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == 'decode':
    decrypt(text,shift)
  elif direction == 'encode':
    encrypt(text,shift)
  else:
    print("Wrong type again")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  rerun2 = input('do you want to contiune:\n').lower
  if rerun2 == 'yes':
    rerun = True
  else:
    rerun == False
