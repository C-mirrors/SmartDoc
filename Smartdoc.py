import webbrowser
import sys

#输入文件
fname = input("Please enter the file you want to generate to the html file:")
if fname == 'srs.txt':
    GEN_HTML = 'srs.html'
    str = 'srs'
elif fname == 'code.py':
    GEN_HTML = 'code.html'
    str = 'code'
else:
    print('To enter the true file name.')

#打开文件，将文件初步转化成html
ffile = open(fname, 'r')
file_content = ffile.read()

fhtml = open(GEN_HTML, 'w')
html_content = """
<html>
<head>The %s htmlpage</head>
""" % (str)


#将文件分段后转化成html段落
"""function need be added"""
html_content += """
<body>
<p>%s</p>""" % (file_content)



#补全html文件
html_content += """
</body>
</html>
"""

# 写入文件
fhtml.write(html_content)
# 关闭文件
fhtml.close()

# 运行完自动在网页中显示
webbrowser.open(GEN_HTML, new=1)

