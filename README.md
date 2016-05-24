#Lz4压缩工具实现的过程和设计思路

使用linux（Ubuntu15.04系统）+ Python完成lz4压缩工具
在官方文档中查看lz4的使用方式
> import lz4

> compressed_data = lz4.dumps(data)

> data == lz4.loads(compressed_data)

> True
#下面开始设计程序
##设计思路
    ####第一要考虑到的是命令行参数传递：
       1.程序设计要符合提供的参数的要求：
       2.解压和压缩分别使用的参数格式
       3.处理参数的顺序
    ####命令行参数搞定了后，就是开始压缩与解压缩的功能设计了：
       1.分别定义两个函数去实现压缩与解压
       2.压缩函数功能是将数据读取，使用lz4.dumps()进行压缩数据
       3.解压函数功能是将压缩包内数据读出，使用lz4.loads()写入原来的文件中

##编写过程
    按照思路中提供的条例：
        1.处理命令行参数：
            这里使用的是sys.argv[]这个属性。
            它可以直接把命令行中的所有参数读入到一个列表中，
            这其中包括脚本名称；
            所以会其中会有叫本用不到的参数。
            那就再传参之前做一次过滤，我要的是选项及其后面的参数
            当输入的参数小于四个的时候，不在继续进行程序运行。退出程序，并给出相应的帮助信息。
            满足要求后，取参数。
            第一个参数很重要，表名是解压还是压缩，
            这一步在程序入口时执行：
                > if __name__ == '__main__':

                > import sys

                > if len(sys.argv) < 4:

                >    print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")

                > else:

                >    main(sys.argv[2:])

        2.满足要求后，开始取参数：
            第一个参数很重要，表明是解压还是压缩，
            所以在取参数的时候从第三个参数开始向后取（sys.argv[2:]）
            得到参数需要进一步判断，再次进行判断
            如果参数给的不符合要求，直接抛出帮助信息，不在继续执行
            >def main(argv):

            >    if argv[0] == '-c' and len(argv) == 3:

            >        Compress(argv[2], argv[1])

            >    elif argv[0] == '-x':
            
            >        sou = argv[1]

            >        des = argv[2] if len(argv) == 3 else sou[:sou.rindex('.')]
            
            >        Decompresstion(sou, des)
            
            >    else:
            
            >        print("Usage：lz4 -c dir_name.lz4r dir_name | lz4 -x dir_name.lz4r")

            对应的能够判断出是进行解压，还是压缩。
            再调用不同的函数进行后续操作
        3.压缩：
            先前导入的有lz4模块，所以可以直接使用lz4.dumps()进行数据压缩
            在压缩之前我们还要判断文件时候存在，如果不存在，抛出异常，并给出显示信息，文件不存在
            读取文件中的数据，使用with语句 。
            它可以打开文件读取文件，并将温江保存回源文件，
            使用了两次，是为了读写方便操作，打开要写入的不存在的压缩后的文件，
            再打开读取的被压缩的文件，使用写操作的子句同时用压缩工具，把读操作子句读到的内容
            放置压缩文件，完成压缩。
        4.解压：
            同于压缩，这完全是一个逆向。
            读写完全反过来，对于解压的数据使用lz4.loads()这个内置的函数，完成效果

        5.测试：
            写几个文件，使用：
            > Python hello.py lz4 -c hello.lz4r hello.txt
            
            查看大小82k的文件被压缩至3.7k
            接着删除原始文件：
            > rm -rf hello.txt
            释放压缩包：
            > python hello.py lz4 -x hello.lz4r 
            查看数据是否和原始一样
            cat hello.txt
            完全一致
