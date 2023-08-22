# base64隐写
import base64
def get_diff(s1, s2):
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    res = 0
    for i in range(len(s2)):
        if s1[i] != s2[i]:
            return abs(base64chars.index(s1[i]) - base64chars.index(s2[i]))
    return res


def b64_stego_decode():
    file = open("base.txt","rb")
    x = ''                                      # x即bin_str
    lines =  file.readlines()
    for line in lines:
        l = str(line, encoding = "utf-8")
        stego = l.replace('\n','')
        #print(stego)
        realtext = base64.b64decode(l)
        #print(realtext)
        realtext = str(base64.b64encode(realtext),encoding = "utf-8")
        #print(realtext)
        diff = get_diff(stego, realtext)        # diff为隐写字串与实际字串的二进制差值
        n = stego.count('=')
        if diff:
            x += bin(diff)[2:].zfill(n*2)
        else:
            x += '0' * n*2
            
    i = 0
    flag = ''
    while i < len(x):
        if int(x[i:i+8],2):
            flag += chr(int(x[i:i+8],2))
        i += 8
    print(flag)

if __name__ == '__main__':
    b64_stego_decode()
