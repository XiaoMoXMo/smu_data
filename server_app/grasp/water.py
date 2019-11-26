from server_app.extensions import requests, re

url = 'http://hqzx.shmtu.edu.cn/cellphone/getHotWater'


def get_water():
    try:
        r = requests.get(url)
        waters = re.findall('<div>(.*?)℃</div>', r.text)
        num = re.findall('<span class="green_col">(.*?)号', r.text)
        volumes = re.findall('<div class="stage">水位(\d+)', r.text)
        water_list = []
        for i in range(len(waters)):
            volume = volumes[i]
            dic = {'num': num[i], 'hot': waters[i], 'volume': volume}
            water_list.append(dic)
        return water_list
    except Exception as e:
        return []
