from common.action import *
from multiprocessing import Process
from common.base_run import choice_env, run

if __name__ == '__main__':
    # 选择环境
    choice_env()
    # 清空日志文件
    clear_file('/result/all.log')
    # 配置allure目录
    del_file('result/allure')
    # 运行用例you hua
    run()
    # 运行allure服务
    try:
        os.system('allure serve result/allure')
    except Exception:
        pass
