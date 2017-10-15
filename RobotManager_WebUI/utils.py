import time
import numpy as np
import logging
from ctypes import *
lib = cdll.LoadLibrary('/usr/lib/libbase64.so')

class StopWatch:
    def __init__(self):
        self._timestamp  = 0
    def start(self):
        self._timestamp = time.time() * 1000
    def elapsed(self):
        now = time.time() * 1000
        return now - self._timestamp
    def stop(self):
        pass
    def reset(self):
        self._timestamp = 0

class Converter:
    def base64str(self,byte_array):
        find_padding = lambda str,n : (((len(str) // n) + 1) * n) - len(str)
        buffer = ""
        n=6
        for b in byte_array:
            binary = (bin(b)[2:]).zfill(8)
            buffer+=binary
        if (len(buffer) % 6 != 0):
            padding = find_padding(buffer,6)
            buffer += '0' * padding
        
        chunks = [buffer[i:i+n] for i in range(0, len(buffer), n)]
        retval = ""
        for chunk in chunks:
            retval += self.convertChunk(chunk) 
        if len(retval) % 4 != 0:
            padding = find_padding(retval,4)
            retval += '=' * padding
        return retval

    def convertChunk(self,chunk):
        value = int(chunk,2)
        if value == 62: return chr(43)
        if value == 63: return chr(47)
        if (value >= 0 and value <=51):
            return chr(value + 65)
        if (value >=52 and value <=61):
            return chr(value - 4)
        return "="    
    def tobase64(self,s, padd = False):
        b64s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        b64p = "="
        ret = ""
        left = 0
        for i in range(0, len(s)):
            if left == 0:
                ret += b64s[ord(s[i]) >> 2]
                left = 2
            else:
                if left == 6:
                    ret += b64s[ord(s[i - 1]) & 63]
                    ret += b64s[ord(s[i]) >> 2]
                    left = 2
                else:
                    index1 = ord(s[i - 1]) & (2 ** left - 1)
                    index2 = ord(s[i]) >> (left + 2)
                    index = (index1 << (6 - left)) | index2
                    ret += b64s[index]
                    left += 2
        if left != 0:
            ret += b64s[(ord(s[len(s) - 1]) & (2 ** left - 1)) << (6 - left)]
        if(padd):
            for i in range(0, (4 - len(ret) % 4) % 4):
                ret += b64p
        return ret   

    def row_function(self,n):
       
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
    def toBae64Np(self,png):
        padding = 0
        if (len(png) % 3 != 0):
            padding = 3 - (len(png) % 3)
            for i in range(padding):
                png = np.append(png,'\x00')
        n=3
        sw = StopWatch()
        sw.start()
        list = Parallel(n_jobs=50)(delayed(self.row_function)(png[i:i+n]) for i in range(0, len(png), n))

        #list = [png[i:i+n] for i in range(0, len(png), n)]
        logging.info("Chunked Elapsed %d",sw.elapsed())
        #list = map(self.row_function,chunkedArray)
        #list = [(chunkedArray[i]) for i in range(len(chunkedArray))]
        return str.join('',list)
    

    def encodeBase64(self,str):
        b64 = c_char_p(lib.base64_encode(str,len(str))).value
        l = 4*((len(str)+2)//3)
        b64=b64[:l]
        return b64
        #arr =[]
        #for i in range(len(s)):
        #    arr.append(ord(s[i]))
        #rows = len(png) // 3 
        #arr2 = np.array(arr)
        #result = np.apply_along_axis(self.row_function,1,png.reshape(rows,3))
        #result_str = np.concatenate(result) 
