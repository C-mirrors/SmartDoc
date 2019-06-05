import sys
import webbrowser

def escape(text):
    # ��text�ı��еĿո�&��<��>����"������'��ת���ɶ�Ӧ�ĵ��ַ�ʵ�壬�Է�����html����ʾ
    text = text.replace('&', '&#38;')
    text = text.replace(' ', '&#160;')
    text = text.replace('<', '&#60;')
    text = text.replace('>', '&#62;')
    text = text.replace('"', '&#34;')
    text = text.replace('\'', '&#39;')
    return text

def changetohtml(text):
    #��text����Ϊ��λ����<li></li>��ǩ
    lines = text.split('\n')
    i = 0
    for line in lines:
        lines[i] = '<li>' + line + '</li>'
        i += 1
    text = ''.join(lines)
    return text


try:
    filename = input('Please enter the file name:')
    filename = filename.replace('\r', '')  # �ڿ���̨������س����ļ������һ��'\r'����Ҫȥ��
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