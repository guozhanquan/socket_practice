import base64
import json
#加密部分
def base64_jiami(s):
    miwen=base64.b64encode(bytes(s,'utf-8'))
    return miwen

#加密
def weijiniya(plaintext,key):
    ascii="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|`+-=\/"
    keylen=len(key)
    ptlen=len(plaintext)
    ciphertext =''
    i =0
    while i < ptlen:
        j = i % keylen
        k = ascii.index(key[j])
        m = ascii.index(plaintext[i])
        ciphertext += ascii[(m+k)%(len(ascii))]
        i +=1
    return ciphertext

def encrypt(plainText,key):
    cipher2 = base64_jiami(plainText)
    cipher2=str(cipher2,encoding="utf-8")
    cipher=weijiniya(cipher2,key)
    return cipher
#解密部分
#维吉尼亚加密算法 解密
def weijiniyajiemi(ciphertext,key):
    ascii="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789|`+-=\/"
    keylen=len(key)
    ctlen=len(ciphertext)
    plaintext =''
    i =0
    while i < ctlen:
        j = i % keylen
        k = ascii.index(key[j])
        m = ascii.index(ciphertext[i])
        if m < k:
            m +=len(ascii)
        plaintext += ascii[m-k]
        i +=1
    return plaintext

def base64_jiemi(miwen):
    yuanwen=base64.b64decode(miwen)
    return str(yuanwen, encoding = "utf-8")
#揭秘算法
def decrypt(cipherText,key):
    decipher=weijiniyajiemi(cipherText,key)
    decipher2=bytes(decipher,encoding="utf-8")
    decipher1=base64_jiemi(decipher2)
    return decipher1

key="qwerdfasdfasdf"
x=encrypt("{'type':'broadcast','name':'张三','ip_addr',127.0.0.1}",key)
print('x',x)
y=decrypt(x,key)
print('y',y)
#对汉字的编码
key1= 0xff
key2=0xaa
def encrypt_hanzi(src):
    return ''.join([''.join(chr((ord(x))^key1&key2)) for x in src])

def decrypt_hanzi(src):
    return ''.join([''.join(chr((ord(x))^key1&key2)) for x in src])

#对数字的的加密
def encryption(num):
    """对数字进行加密解密处理每个数位上的数字变为与7乘积的个位数字，再把每个数位上的数字a变为10-a．"""
    newNum = []

    for i in str(num):
        if int(i):
            newNum.append(str(10 - int(i) * 7 % 10))
        else:
            newNum.append(str(0))
    return int(''.join(newNum))


def decryption(num):
    """对数字进行解密处理，把每个数位上的数字乘以7再进行与10求余即可"""
    oldNum = []
    [oldNum.append(str(int(i) * 7 % 10)) for i in str(num)]
    return int(''.join(oldNum))
def encrypt_ip(ip_address):
    ip_list=ip_address.split(".")
    if len(ip_list) == 4:
        ip_list[0]=~(int(ip_list[0])^0x2f)
        ip_list[1] = ~(int(ip_list[1]) ^ 0x3f)
        ip_list[2] = ~(int(ip_list[2]) ^ 0x4f)
        ip_list[3] = ~(int(ip_list[3]) ^ 0x5f)
        return str(ip_list[3])+"."+str(ip_list[1])+"."+str(ip_list[2])+"."+str(ip_list[0])
    else:
        return

def dencrypt_ip(ip_address):
    ip_list = ip_address.split(".")
    if len(ip_list) == 4:
        ip_list[0] = (~int(ip_list[0]))^(0x5f)
        ip_list[1] = (~int(ip_list[1]))^(0x3f)
        ip_list[2] = (~int(ip_list[2]))^(0x4f)
        ip_list[3] = (~int(ip_list[3]))^(0x2f)
        return str(ip_list[3]) + "." + str(ip_list[1]) + "." + str(ip_list[2]) + "." + str(ip_list[0])
    else:
        return
def encrypt_tuple(x):
    if x!=None:
        lis=list(x)
        a=lis[0]
        b=lis[1]
        c=encrypt_ip(a)
        d=encryption(b)
        return (d,c)
def dencrypt_tuple(x):
    if x!=None:
        lis=list(x)
        a=lis[1]
        b=lis[0]
        c=dencrypt_ip(a)
        d=decryption(b)
        return (c,d)
