# 编写一个程序，用户输入开始搜索的路径，查找该路径下（包含子文件夹）所有的视频格式文件（要求查找mp4，rmvb，avi的格式即可），
# 并创建一个文件（vedioList.txt）存放找到的文件的路径，程序实现如图：

import os
import os.path

file_list = []

#
# def create_video_list(file_l):
#


def search_video(path, format_list=['.mp4', '.rmvb', '.avi']):
    os.chdir(path)
    temp_folder = list(filter(lambda x: os.path.isdir(x), os.listdir(path)))
    temp_file = list(filter(lambda x: (os.path.isfile(x) and os.path.splitext(x)[1] in format_list), os.listdir(path)))
    file_list.extend(os.path.join(path, each_file) for each_file in temp_file)
    if temp_folder:
        for sub_folder in temp_folder:
            search_video(os.path.join(path, sub_folder))

    f_video_list = open('/Users/felix/PycharmProjects/learningpython/vedioList.txt', 'w')

    # 如果直接使f_video_list.writelines(file_list) 写入的文件内容没有换行
    # f_video_list.writelines(file_list)
    for each_file_path in file_list:
        f_video_list.write(each_file_path)
        f_video_list.write('\n')
    f_video_list.close()


if __name__ == '__main__':
    search_video(input('请输入待查找的初始目录：'))
    print(file_list)

