# 提供一个文件浏览框，让用户选择需要打开的文本文件，打开并显示文件内容

import easygui as g
import sys

f_name = g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
if f_name:
    message = "文件" + f_name + "的内容如下： "
    title = "显示文件内容"

    with open(f_name, 'r') as f:
        f_content = f.readlines()
    g.textbox(msg=message, title=title, text=f_content, codebox=False, callback=None, run=True)

else:
    sys.exit()



