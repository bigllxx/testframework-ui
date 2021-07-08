from common.action import *
from common.base_run import choice_env, run

if __name__ == '__main__':
    choice_env()  # 选择环境
    clear_file('/result/all.log')  # 清空日志文件
    del_file('result/allure')  # 配置allure目录
    run()  # 运行用例
    try:
        os.system('allure serve result/allure')  # 运行allure服务
    except Exception:
        pass
