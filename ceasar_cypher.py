def encrypt(text,shift):
  
  lst=[]
  for i in text:
    i=ord(i)
    i=i+shift
    if(i>122):
        i=ord("a")+(i-123)
    lst.append(i)
    print(i)
  str=""
  for i in range(len(lst)):
    lst[i]=chr(lst[i])
    str+=lst[i]
  return str
  
def decrypt(text,shift):
  lst=[]
  for i in text:
    i=ord(i)
    i=i-shift
    if(i<97):
        i=ord("z")-(96-i)
    lst.append(i)
  str=""
  for i in range(len(lst)):
    lst[i]=chr(lst[i])
    str+=lst[i]
  return str

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift=(shift%26)
if( direction=="encode"):
    encrypted_txt=encrypt(text,shift)
    print(f"The encoded text is {encrypted_txt}")
else:
    decrypted_txt=decrypt(text,shift)
    print(f"The decoded text is {decrypted_txt}")
