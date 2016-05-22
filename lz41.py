#!/usr/bin/python
import lz4


# 压缩文件
def Compress(sou, des):
    try:
        with open(des, 'wb') as out:
            with open(sou, 'rb') as inFile:
                out.write(lz4.dumps(inFile.read()))
            out.flush()
            out.close()
    except IOError:
        print('文件找不到')


# 解压文件
def Decompresstion(sou, des):
    try:
        with open(des, 'wb') as out:
            with open(sou, 'rb') as inFile:
                out.write(lz4.loads(inFile.read()))
            out.flush()
            out.close()
    except IOError:
        print('文件找不到')


# 命令行参数处理
#def main(argv):
#    if argv[1] == '-c':
#        Compress(argv[3], argv[2])
#    elif argv[0] == '-x':
#        Decompresstion(argv[1], argv[2])
#    else:
#        print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")
def main(argv):
    if argv[0] == '-c':
        if len(argv) < 3:
            print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")
        else:
            Compress(argv[2], argv[1])
    elif argv[0] == '-x':
        sou = argv[1]
        des = sou[:sou.rindex('.')]
        Decompresstion(sou, des)
    else:
        print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 4:
        print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")
    else:
        main(sys.argv[2:])

'''
Python hello.py lz4 -c hello.lz4r hello.txt
python hello.py lz4 -x hello.lz4r 
'''