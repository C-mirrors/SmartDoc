import sys
import webbrowser

def fileToHtml(filename):
    #通过输入文件生成html
    fold = open(filename, encoding='utf8')
    text = fold.read()
    fold.close()
    text = escape(text)
    if filename[filename.find('.'):] == '.txt':  # 若是srs文件，则添加到code的链接
        text = txtTohtml(text)
    if filename[filename.find('.'):] == '.py':  # 若是code文件，则添加到srs的链接
        text = pyTohtml(text)
    filename = filename[:filename.find('.')]
    fhtml = open(filename + '.html', 'wt', encoding='utf8')
    fhtml.write("""
            <!doctype html>
            <html>
            <head>
            <meta charset="utf-8">
            <title>%s</title>
            <style type="text/css">
                div{border-bottom:1px solid #4b4b4b;padding:30px;}
                h2{font-family:Arial;font-size:25px;color:#333;font-weight:normal;text-transform:uppercase;}    
                h3{font-family:Arial;font-size:18px;color:#333;font-weight:normal;text-transform:uppercase;}
                h4{font-family:Arial;font-size:16px;color:#4b4b4b;font-weight:normal;text-transform:uppercase;}
                li{font-family:Arial;font-size:16px;color:#333;font-weight:normal;}
                p{font-family:Arial;font-size:14px;color:#4b4b4b;font-weight:normal;}
                a{text-decoration:none;font-family:Arial;font-size:16px;color:#4b4b4b;font-weight:bold;text-transform:uppercase;}
            </style>
            </head>

            <body>
                %s
            </body>
            </html>"""%(filename,text))
    fhtml.close()
    webbrowser.open(filename + '.html', new=1)


def escape(text):
    # 将text文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示
    text = text.replace('&', '&#38;')
    text = text.replace(' ', '&#160;')
    text = text.replace('<', '&#60;')
    text = text.replace('>', '&#62;')
    text = text.replace('"', '&#34;')
    text = text.replace('\'', '&#39;')
    return text

def txtTohtml(text):
    #将srs文件转换成html文件
    lines = text.split('\n')
    i = 0
    for line in lines:
        if line.find('Requirement') > -1:
            lines[i] = '<div> <h2>Requirement</h2> <a href="code.html#RQ' + line[line.find('rq')+2] + '" id="RQ' + line[line.find('rq')+2] + \
                    '">ID: RQ' + line[line.find('rq')+2] + '</a> <h3>description</h3> <p>' + line[line.find('description=')+12:-1] + '</p>'
        if line.find('Rationale') > -1:
            lines[i] = '<h2>Rationale</h2> <h4>ID: RA</h4> <h3>description</h3>' + '<p>' + line[line.find('description=')+12:-1] + '</p>'
        if line.find('TestCase') > -1:
            lines[i] = '<h2>TestCase</h2> <h4>ID: TC</h4>' + '<h3>description</h3>' + '<p>' + line[line.find('description=')+12:-1] + '</p>'
        if line.find('Priority') > -1:
            lines[i] = '<h2>Priority</h2>' + '<p>' + line[line.find('[')+1:-1] + '</p> </div>'
        i += 1
    text = ''.join(lines)
    return text

def pyTohtml(text):
    #将code文件转换成html文件
    lines = text.split('#{see')
    i = 0
    for line in lines:
        if len(lines[i]) > 3:
            if line[8].isdigit():
                lines[i] = '<a style="font-size:20px;margin:30px;font-weight:bold" href="srs.html#RQ' + line[8] + '" id="RQ' + line[8] + \
                           '">#{see RQ' + line[8] + '}' + '</a>\n' + line[line.find('\n')+1:]
            else:
                lines[i] = '<a style="font-size:20px;margin:30px;font-weight:bold" href="code.html#RQ" id="RQ">#{see RQ}' \
                           + ' # No link to srs</a>\n' + line[line.find('\n')+1:]
        i += 1
    text = ''.join(lines)
     #将text以行为单位加上<li></li>标签
    lines = text.split('\n')
    i = 0
    for line in lines:
        lines[i] = '<li>' + line + '</li>'
        i += 1
    text = ''.join(lines)
    return text

try:
    s = input('Please enter the file name(e.g.: srs.txt code.py):')
    filename1, filename2 = s.split()
    fileToHtml(filename1)
    fileToHtml(filename2)

except:
    print("Unexpected error:", sys.exc_info()[0], sys.exc_info()[1])
