import requests
from common.action import get_config


def send_api(method='get', params=None, verify=False):
    """
    发送请求
    :param method:
    :param params:
    :param verify:
    :return:
    """
    cf = get_config('/config.ini', 'all_config')
    _url = cf['api_url']
    res = requests.request(method=method, url=_url + params, verify=verify)
    # print(res.json())
    return res.json()


def banner_grid_api():
    """
    :return: list, ['瓦片区', '轮播图']
    """
    res = []
    s = send_api(params='homepage')
    res.append(s['data']['gridCells'][1]['title'])
    res.append(s['data']['banners'][1]['title'])
    return res


def hottest_api():
    """
    :return: 当前最热第一条
    """
    s = send_api(params='homepage/weekly_hottest?offset=0&limit=6')
    res = s['data']['list'][1]['title']
    return res


def recommend_grid_api():
    """
    :return: 推荐页瓦片区第一条
    """
    s = send_api(params='recommend/grid_cell')
    res = s['data'][0]['title']
    return res


def recommend_navbar_api():
    """
    :return: 推荐页导航栏最后一条
    """
    s = send_api(params='recommend/nav_bar')
    res = s['data'][-1]['name']
    return res


if __name__ == '__main__':
    print(banner_grid_api())