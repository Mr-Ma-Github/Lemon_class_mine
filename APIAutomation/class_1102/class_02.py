#-*-coding:utf-8-*-
# 绝对路径：绝对路径又分为本地绝对路径和网络绝对路径。
# 本地路径是指文件在硬盘上真正存在的路径。网络路径就是带有网址的路径，
# 相对路径：相对路径相对路径就是相对于当前文件的路径
# 疑问：如果我们要操作一个文件 是用绝对路径好  还是相对路径好？  都可以

import os
# mkdir  新建一个目录/新建一个文件夹
# os.mkdir("Alisa")

# 跨级新建目录  用/符号来代表目录的不同层级
# 必须确保上级目录是存在的
# os.mkdir("Alisa/vict")#相对路径
# os.mkdir("D:\\tlisa")#绝对路径
# 此处要添加双斜杠，因为\t是转义字符
# 转义字符 \r   \n   \t 通过加\  还有r  R   让转义字符失效(R"D:\tlisa")

# rmdir 删除目录  删除文件也是一级一级的删除     不推荐一次性删除
# os.rmdir(r"D:\tlisa")
# OSError: [WinError 145] 目录不是空的。: 'D:\\tlisa'
#
# import shutil
# # os.remove(path)   #删除文件
# # os.removedirs(path)   #删除空文件夹
# shutil.rmtree(r"D:\tlisa")    #递归删除文件夹

# 拓展:怎么去创建文件    open   删除文件
# 文件操作：
# os.mknod("test.txt")        创建空文件
# fp = open("test.txt",w)     直接打开一个文件，如果文件不存在则创建文件
# os.remove()                 函数用来删除一个文件

# # 路径的获取1   获取当前工作目录  具体到最后一级目录
# path= os.getcwd()
# print("1获取到当前的路径是:{0}".format(path))
# # print(os.getcwd())
# # 路径的获取2   获取当前文件所在的绝对路径   具体到模块（文件）名
# path_2= os.path.realpath(__file__)#__file__表示的是当前文件本身
# print("2获取到当前的路径是:{0}".format(path_2))

# 如何拼接路径
# new_path=os.getcwd()+"\python1"
# print(new_path)
# os.mkdir(new_path)

# join
# new_path_2=os.path.join(os.getcwd(),"python2")
# print(new_path_2)
# os.mkdir(new_path_2)

# 判断是文件还是目录
# print(os.path.isfile(os.getcwd()))#返回值  布尔值
# print(os.path.isdir(os.getcwd()))#返回值  布尔值  dir  directory

# 怎么判断文件是否存在?      返回布尔值
# print(os.path.exists("class_02.py"))
# print(os.path.exists("C:\\Users\haiyu.ma\PycharmProjects\lemon_class\class_1102\class_02.py"))

# 罗列出当前路径的所有文件和目录
# print(os.listdir(os.getcwd()))

# 拓展题：
# 给定一个路径，请打印出所有的路径（直至这个路径下没有目录为止）
# 思路：递归函数   写成一个函数
# for path in print(os.listdir(os.getcwd())):