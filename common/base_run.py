import configparser
import sys
from multiprocessing import Process

import pytest


def choice_env():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    if len(sys.argv) == 1 or sys.argv[1] == 'qa':
        config.set('all_config', 'url', 'https://mcs-qa.mampod.cn/en/admin/login/?next=/en/admin/')
        config.set('all_config', 'api_url', 'https://acc-api-qa-hula.mampod.cn/v2/')
        config.set('all_config', 'username', 'tester')
        config.set('all_config', 'password', '123456Zz.')
        config.set('all_config', 'host', '8.129.97.36')
        print('environment：qa')
    elif sys.argv[1] == 'test':
        config.set('all_config', 'url', 'https://mcs-test.mampod.cn/en/admin/login/?next=/en/admin/')
        config.set('all_config', 'api_url', 'https://acc-api-test-hula.mampod.cn/v2/')
        config.set('all_config', 'username', 'linxin')
        config.set('all_config', 'password', '123456Zz.')
        config.set('all_config', 'host', '47.115.159.83')
        print('environment：test')
    elif sys.argv[1] == 'staging':
        config.set('all_config', 'url', 'https://mcs-staging.mampod.cn/en/admin/login/?next=/en/admin/')
        config.set('all_config', 'api_url', 'https://acc-api-staging-hula.mampod.cn/v2/')
        config.set('all_config', 'username', 'linxin')
        config.set('all_config', 'password', 'DmdY44Mc7PC4fobU')
        config.set('all_config', 'host', '1.1.1.1')
        print('environment：staging')
    else:
        print('Please specify the environment: test or qa or staging')
    config.write(open('./config.ini', "r+"))


def run_test(file):
    allure_path = 'result/allure'
    pytest.main(
        ['-s', '--alluredir', allure_path, 'test/{}'.format(file)])


def run():
    p1 = Process(target=run_test, name='test_content', args=('test_content.py',))
    p2 = Process(target=run_test, name='test_home', args=('test_home.py',))
    p3 = Process(target=run_test, name='test_label_navigation', args=('test_label_navigation.py',))
    p4 = Process(target=run_test, name='test_topic', args=('test_topic.py',))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p1.join()
    p2.join()
    p3.join()
    p4.join()