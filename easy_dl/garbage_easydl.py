# -*- coding: utf-8 -*-
# @Time    : 2020/02
# @Author  : Sunyu
# @PROJECT : Easy_DL_CAMP
import base64
import json
from pprint import pprint

import requests


class Easy_Dl:
    # 【物体检测】垃圾分类 模型ID：50648
    od_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/detection/garbage_od?access_token="
    # 【图像分类】垃圾分类-图像分类 模型ID：50931
    pt_url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/classification/garbage_pt?access_token="

    def getByte(self, path):
        '''
        Base64转换
        '''
        with open(path, 'rb') as f:
            img_byte = base64.b64encode(f.read())
        img_str = img_byte.decode('ascii')
        return img_str

    def get_token(self):
        '''
        获取Token
        '''
        # 为官网获取的AK
        client_id = 'esdIR17bZ7KCd06yc9kpmf4E'
        # 为官网获取的SK
        client_secret = 'OPyMtywQ7qh6gDizfHySOoWKfpSNGLo1'
        # URL地址
        host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'
        response = requests.get(host)
        if response:
            return response.json()['access_token']
        else:
            print("Token获取失败")

    def get_easydlapi(self, request_url, image):
        '''
        调用官方API
        '''
        # URL地址
        request_url += self.get_token()
        headers = {'Content-Type': 'application/json'}
        # 图像编码
        data = self.getByte(image)
        # BODY参数
        params = {
            'image': data,
            'threshold': '0.7'
        }

        response = requests.request(
            "POST",
            url=request_url,
            headers=headers,
            data=json.dumps(params)).text

        if response:
            return json.loads(response)['results']


if __name__ == '__main__':
    dl = Easy_Dl()
    image1 = '00070.jpg'
    image2 = 'R_10815.jpg'
    # 调用物体检测模型
    pprint(f'物体检测接口调用返回结果：{dl.get_easydlapi(dl.od_url, image1)}')
    # 调用图像分类模型
    pprint(f'图像分类接口调用返回结果：{dl.get_easydlapi(dl.pt_url, image1)}')
