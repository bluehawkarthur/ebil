import sys
import stdnum
from stdnum import verhoeff
import base64
import math
import qrcode
from qrcode import *
from qrcode.image.pure import PymagingImage
from ebil.settings import MEDIA_ROOT


def KSA(key):
    key_length = len(key)

    a= range(256)

    j = 0
    for i in range(256):
        j = (j + a[i] + key[i % key_length]) % 256
        a[i], a[j] = a[j], a[i]    #swapping

    return a


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swapping

        K = S[(S[i] + S[j]) % 256]
        yield K


def key_conversion(key):
    key=[ord(c) for c in key]
    
    #KSA Step
    S=KSA(key)

    #PRGA Step
    keystream=PRGA(S)
    return keystream


def encrypt(data,key):
    keystream=key_conversion(key)
    out=[]
    for char in data:
        out.append("%02X" % (ord(char) ^ keystream.next()))
    
    hex_data=''.join(out)
    return hex_data


def verhoeff(lista):
    li2 = []
    for i in lista:
        num1 = stdnum.verhoeff.calc_check_digit(i)
        num1 += stdnum.verhoeff.calc_check_digit(int(str(i)+num1))
        i = int(str(i) + num1)
        li2.append(i)
    return li2 #Datos mas dos digitos de verhoeff


def sumatorias(r):
    v = []
    sumatoria = 0
    for i in r:
        sumatoria = sumatoria + ord(i)
    v.append(sumatoria)
    print v, type(r)

    sp1 = 0
    sp2 = 0
    sp3 = 0
    sp4 = 0
    sp5 = 0

    for j in range(0, len(r), 5):
        sp1 = sp1+ord(r[j])
    v.append(sp1)
    for j in range(1, len(r), 5):
        sp2 = sp2+ord(r[j])
    v.append(sp2)
    for j in range(2, len(r), 5):
        sp3 = sp3+ord(r[j])
    v.append(sp3)
    for j in range(3, len(r), 5):
        sp4 = sp4+ord(r[j])
    v.append(sp4)
    for j in range(4, len(r), 5):
        sp5 = sp5+ord(r[j])
    v.append(sp5)
    return v

def base64(n):
    dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', '+', '/']
    
    cociente = 1
    resto = 0
    palabra = ''
    while n >= 64:
        cociente = n // 64
        resto = n % 64
        palabra = dic[resto] + palabra
        n = cociente
    palabra = dic[n] + palabra
    return palabra


def codigoControl(llave_dosificacion, num_autorizacion, num_de_factura, nit_ci, fecha_transaccion, total):

    llave_dosificacion = 'aILQZTnHUqQ+ZC8wt]cnXaqLFk3JeZ65i6)8DPBa4t]Zv7J=K==dsz8p=Lh%+sK}'
    # print llave_dosificacion
    num_autorizacion = 2904002017340
    num_de_factura = 72138
    nit_ci = 1829881
    fecha_transaccion =  "2007-06-14" #20070702
    fecha_transaccion = fecha_transaccion.replace("-", "")
    monto_transaccion = 13227.51
    monto_transaccion = int(round(monto_transaccion))
    print "dfgdfgdfgdfgdfg", monto_transaccion
    li = [num_de_factura, nit_ci, fecha_transaccion, monto_transaccion]
    li2 = verhoeff(li)
    suma_verhoeff = 0
    for ii in li2:
        suma_verhoeff = suma_verhoeff+ii
    cinco_dig = []
    cinco_dig_str = []

    num1 = suma_verhoeff
    for iii in range(0, 5):
        num = stdnum.verhoeff.calc_check_digit(num1)
        cinco_dig.append(int(num))
        cinco_dig_str.append(num)
        num1 = (int(str(num1)+num))
    x = "".join(cinco_dig_str)


    sumarUno = []
    for i in cinco_dig:
        sumarUno.append(i+1)
    i0 = 0
    i1 = sumarUno[0]
    i2 = i1+sumarUno[1]
    i3 = i2+sumarUno[2]
    i4 = i3+sumarUno[3]
    i5 = i4+sumarUno[4]

    cad0 = llave_dosificacion[i0:i1]
    cad1 = llave_dosificacion[i1:i2]
    cad2 = llave_dosificacion[i2:i3]
    cad3 = llave_dosificacion[i3:i4]
    cad4 = llave_dosificacion[i4:i5]

    #CADENAS PARA ENTRADA DE AllegedRC4
    a1 = str(num_autorizacion)+cad0
    a2 = str(li2[0])+cad1
    a3 = str(li2[1])+cad2
    a4 = str(li2[2])+cad3
    a5 = str(li2[3])+cad4

    param1_a = a1+a2+a3+a4+a5
    param2_a = llave_dosificacion+x

    r = encrypt(param1_a, param2_a)
    v = sumatorias(r) #retorna lista de las sumatorias, el primer es total de todo
    print sumarUno
    st1 = int((v[0]*v[1])/sumarUno[0])
    st2 = int((v[0]*v[2])/sumarUno[1])
    st3 = int((v[0]*v[3])/sumarUno[2])
    st4 = int((v[0]*v[4])/sumarUno[3])
    st5 = int((v[0]*v[5])/sumarUno[4])
    total_st = st1+st2+st3+st4+st5
    print total_st
    y = base64(total_st)
    
    alle = encrypt(y, llave_dosificacion+x)
    i=0
    cod_control1 = ''
    while i < len(alle):
        cod_control1 = cod_control1 + alle[i] + alle[i+1]
        i = i + 2
        if i < len(alle):
            cod_control1 = cod_control1 + '-'

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data('1020703023|545|30010060025|2/12/2015|5000,00|5000.00|5A-79-C9-DA-32|3764863|0|0|0|0')
    qr.make(fit=True)

    img = qr.make_image()
    print '44444444', img
    rute = '%s/%s' % (MEDIA_ROOT, "codigo/QQRR.png")
    img.save(rute)

    return cod_control1
