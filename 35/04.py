# 在上一题的基础上增强功能：当用户点击“OK”按钮的时候，比较当前文件是否修改过，
# 如果修改过，则提示“覆盖保存”、“放弃保存”或“另存为…”并实现相应的功能。

import easygui as g
import sys
import os.path


def mfile_action(m_choice):
    if m_choice == '覆盖保存':
        with open(f_name, 'r') as fo:
            temp_content = fo.readlines()
            with open(f_name, 'w') as fw:
                fw.writelines(temp_content)
    elif m_choice == '放弃保存':
        with open(f_name, 'w') as fw:
            fw.writelines(f_content)
    elif m_choice == '另存为':
        # with open(f_name, 'r') as fo:
        #     temp_content = fo.readlines()
        new_fname = g.filesavebox(msg=None, title=None, default='', filetypes=None)
        if new_fname:
            with open(f_name, 'r') as fo:
                temp_content = fo.readlines()
            with open(new_fname, 'x') as fs:
                fs.writelines(temp_content)
    else:
        sys.exit()


f_name = g.fileopenbox(msg=None, title=None, default='*', filetypes=None, multiple=False)
old_mtime = os.path.getmtime(f_name)
if f_name:
    message = "文件" + f_name + "的内容如下： "
    title = "显示文件内容"

    with open(f_name, 'r') as f:
        f_content = f.readlines()
        print(f_content)
    if g.textbox(msg=message, title=title, text=f_content, codebox=False, callback=None, run=True):
        new_mtime = os.path.getmtime(f_name)
        if new_mtime != old_mtime:
            warn_msg = '检测到文件内容发生改变，请选择以下操作：'
            warn_title = '警告'
            warn_choices = ['覆盖保存', '放弃保存', '另存为']
            choice = g.buttonbox(msg=warn_msg, title=warn_title, choices=warn_choices, image=None, images=None,
                        default_choice=None, cancel_choice=None, callback=None, run=True)
            mfile_action(choice)
else:
    sys.exit()
