import sys
import webbrowser

def fileToHtml(filename):
    #通过输入文件生成html
    file = open(filename, encoding='utf8')
    text = file.read()
    file.close()
    text = escape(text)
    if filename[-1] == 't':  # 若是srs文件，则添加到code的链接
        text = txtTopy(text);
    if filename[-1] == 'y':  # 若是code文件，则添加到srs的链接
        text = pyTotxt(text)
    text = preChange(text)
    file = open(filename + '_htmlpage.html', 'wt', encoding='utf8')
    file.write(text)
    file.close()
    webbrowser.open(filename + '_htmlpage.html', new=1)

def escape(text):
    # 将text文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示
    text = text.replace('&', '&#38;')
    text = text.replace(' ', '&#160;')
    text = text.replace('<', '&#60;')
    text = text.replace('>', '&#62;')
    text = text.replace('"', '&#34;')
    text = text.replace('\'', '&#39;')
    return text

def preChange(text):
    #将text以行为单位加上<li></li>标签
    lines = text.split('\n')
    i = 0
    for line in lines:
        lines[i] = '<li>' + line + '</li>'
        i += 1
    text = ''.join(lines)
    return text

def txtTopy(text):
    #向srs文件中添加到code的链接
    lines = text.split('@')
    i = 0
    for line in lines:
        if line != '':
            lines[i] = '<a href="code.py_htmlpage.html#RQ' + str(i) + '" id="RQ' + str(i) + '">#{see function}' + '</a>\n@' + line
        i += 1
    text = ''.join(lines)
    return text

def pyTotxt(text):
    #向code文件中添加到srs的链接
    lines = text.split('#{see')
    i = 0
    for line in lines:
        if len(lines[i]) > 3:
            if line[8].isdigit():
                lines[i] = '<a href="srs.txt_htmlpage.html#RQ' + line[8] + '" id="RQ' + line[8] + \
                           '">#{see RQ' + line[8] + '}' + '</a>\n' + line[line.find('\n')+1:]
            else:
                lines[i] = '<a href="code.py_htmlpage.html#RQ" id="RQ">#{see RQ}' \
                           + ' # No link to srs</a>\n' + line[line.find('\n')+1:]
        i += 1
    text = ''.join(lines)
    return text

try:
    s = input('Please enter the file name(e.g.: srs.txt code.py):')
    filename1, filename2 = s.split()
    print(filename1, filename2)
    fileToHtml(filename1)
    fileToHtml(filename2)

except:
    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
