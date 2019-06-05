import sys
import webbrowser

def escape(text):
    # 将text文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示
    text = text.replace('&', '&#38;')
    text = text.replace(' ', '&#160;')
    text = text.replace('<', '&#60;')
    text = text.replace('>', '&#62;')
    text = text.replace('"', '&#34;')
    text = text.replace('\'', '&#39;')
    return text

def changetohtml(text):
    #将text以行为单位加上<li></li>标签
    lines = text.split('\n')
    i = 0
    for line in lines:
        lines[i] = '<li>' + line + '</li>'
        i += 1
    text = ''.join(lines)
    return text


try:
    filename = input('Please enter the file name:')
    filename = filename.replace('\r', '')  # 在控制台中输入回车后文件名会多一个'\r'，需要去掉
    f = open(filename, encoding='utf8')
    t = f.read()
    f.close()
    t = escape(t)
    t = changetohtml(t)
    f = open(filename + '_htmlpage.html', 'wt', encoding='utf8')
    f.write(t)
    f.close()
    webbrowser.open(filename + '_htmlpage.html', new=1)
except:
    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])