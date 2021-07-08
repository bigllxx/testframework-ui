import logging
import os


class Logger:

    if os.path.exists(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/result') is False:
        os.mkdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/result')
    filename = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/result/all.log'

    def __init__(self, name='Assert'):
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(logging.INFO)  # 只记录INFO及以上的日志
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 输出格式

        # 控制台输出
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # 只输出INFO及以上的日志
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        # 文件输出
        fh = logging.FileHandler(self.filename)
        fh.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)