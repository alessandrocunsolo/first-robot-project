import numpy as np
import cv2

def row_function(n):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    #print (n)
    if (n[0] == ''):
        n[0] = '0'
    num = int(n[0])<<16
    if (n[1] == ''):
        n[1] = '0'
    num+=int(n[1])<<8
    if (n[2] == ''):
        n[2] = '0'
    num+=int(n[2])

    c1 = symbols[num>>18]
    c2 = symbols[(num>>12) & 63]
    c3 = symbols[(num>>6) & 63]
    c4 = symbols[num & 63]
    return c1 + c2 + c3 + c4
def main():
    camera = cv2.VideoCapture(0)
    im = camera.read(0)[1]
    png = cv2.imencode('.png',im)[1]
    padding = 0
    if (len(png) % 3 != 0):
        padding = 3 - (len(png) % 3)
        for i in range(padding):
            png = np.append(png,'\x00')
    #arr =[]
    #for i in range(len(s)):
    #    arr.append(ord(s[i]))
    rows = len(png) // 3 
    #arr2 = np.array(arr)
    result = np.apply_along_axis(row_function,1,png.reshape(rows,3))
    result_str = np.concatenate(result) 
    #result_str = result.tostring()
    #result_str = result_str[:-padding]
    #result_str += '=' * padding
    print (result_str)

if __name__=='__main__':
    main()




