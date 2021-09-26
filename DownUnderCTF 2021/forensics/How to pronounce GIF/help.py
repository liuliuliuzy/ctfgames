from PIL import Image
import os
import random


class GIFTest:

    def __init__(self, file_name):
        self.file_name = file_name      # 传入的文件名
        self.dir_name = self.file_name[:-4]     # 根据文件名创建存放分帧图片的文件夹
        self.gif_path = os.path.join(os.path.dirname(__file__), file_name)  # 拼接图片文件的完整路径（仅限同一文件夹内）
        self.make_dir()

    def make_dir(self):
        """用于创建存放分帧图片的文件夹"""
        try:
            os.mkdir(self.dir_name)
        except FileExistsError:
            print('<%s>文件夹已存在' % self.dir_name)
            self.dir_name += str(random.randint(0, 10))
            os.mkdir(self.dir_name)

    def framing_test(self):
        """GIF图片分帧"""
        img = Image.open(self.gif_path)
        try:
            while True:
                curr = img.tell()
                name = os.path.join(self.dir_name, '第%s帧.png' % str(curr + 1))
                img.save(name)
                img.seek(curr+1)
        except Exception as e:
            pass


if __name__ == '__main__':
    GIFTest('challenge.gif').framing_test()