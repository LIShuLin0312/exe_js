import execjs


def get_encrypt_psswd(data, key=None, Js_path="./now.js"):
    JS_Str = get_js(Js_path)
    ctx = execjs.compile(JS_Str)  # 加载JS文件
    return ctx.call('Getpass', data)  # 调用js方法  第一个参数是JS的方法名，后面的data和key是js方法的参数


def get_js(Js_path):
    f = open(r"{}".format(Js_path), 'r', encoding='utf-8')  # 打开JS文件
    line = f.readline()
    htmlstr = ''
    while line:
        htmlstr = htmlstr + line
        line = f.readline()
    return htmlstr


if __name__ == '__main__':
    print(get_encrypt_psswd('888888'))
