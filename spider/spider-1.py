import json
import pandas as pd
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import re
import string
import os
import json
from PIL import Image

import matplotlib.pyplot as plt
def get_text(): ## 用于获取标注文件
    url='http://soleil.i4ds.ch/solarradio/data/BurstLists/2010-yyyy_Monstein/'
    response = requests.get(url)
    if response.status_code == 200:
        # 解析网页内容
        soup = BeautifulSoup(response.text, 'html.parser')
    links=soup.find_all('a')
    for link in links[9:14]:
        href = link.get('href')
        url_gettext=url+href
        response_text=requests.get(url_gettext)
        soup_text=BeautifulSoup(response_text.text,'html.parser')
        links_text=soup_text.find_all('a')
        for link_text in links_text:
            href_text=link_text.get('href')
            if 'e-CALLISTO' in href_text:
                url_text=url_gettext+'/'+href_text
                re=requests.get(url_text)
                so=BeautifulSoup(re.text,'html.parser')
                text=so.get_text()
                file_path='./text_save'+'/'+href_text
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text)
    print('完成')

def are_time_intervals_intersecting(start1, end1, start2, end2):
    if end1 < start2 or start1 > end2:
        return False
    return True
def get_fits(path): # 用于获取某一个标注文件中的爆发fits path 为标志文件的位置
    path_img='http://soleil.i4ds.ch/solarradio/callistoQuicklooks/?date='
    path_img_1='http://soleil.i4ds.ch/solarradio'
    save_path=path.split('/')[2]
    save_path='./fits_save/'+save_path.split(('.'))[0]

    if os.path.exists(save_path) and os.path.isdir(save_path):
        print("文件夹存在")
    else:
        print("文件夹不存在")
        os.makedirs(save_path)
    time_format = "%Y%m%d%H%M"
    with open(path , 'r') as f:
        f=f.readlines()
        for line in f:
            if '20' in line and '#' not in line and ':' in line:
                fields = line.split('\t')
                fild = fields[3]
                fild = fild.split(',')
                fild_tmp = []
                for index in fild:
                    fild_tmp.append(index.replace(' ', ''))

                path_img_temp = path_img + str(fields[0])
                response_temp = requests.get(path_img_temp)
                soup_temp = BeautifulSoup(response_temp.text, 'html.parser')
                img_tags = soup_temp.find_all('a')
                for index,numb in zip(img_tags, range(0,len(img_tags))):
                    str1 = fields[0] + fields[1]
                    cleaned_string_str1 = re.sub(r'[' + re.escape(string.whitespace + string.punctuation) + ']', '',
                                                 str1)
                    str1_0 = cleaned_string_str1[0:8]
                    str1_1 = datetime.strptime(str1_0 + cleaned_string_str1[8:12], time_format)
                    str1_2 = datetime.strptime(str1_0 + cleaned_string_str1[12:], time_format)
                    href_index = index.get('href')

                    if '../q' in href_index:
                        str0 = href_index
                        str0_0 = str0.split('_')
                        str0_0 = [index.split('/') for index in str0_0]
                        if 'Banting' in str0_0[1] or 'NM' in str0_0[1]:
                            str2 = str0_0[2][0] + str0_0[3][0]
                        else:
                            str2 = str0_0[1][0] + str0_0[2][0]

                        cleaned_string_str2 = re.sub(r'[' + re.escape(string.whitespace + string.punctuation) + ']',
                                                     '',
                                                     str2)[:-2]
                        time_interval = timedelta(minutes=15)
                        str2_1 = datetime.strptime(cleaned_string_str2, time_format)
                        str2_2 = datetime.strptime(cleaned_string_str2, time_format) + time_interval
                        a = are_time_intervals_intersecting(str1_1, str1_2, str2_1, str2_2)

                        if a and (str0_0[0][5] in fild_tmp or '*' in fild_tmp):
                            # img_url = path_img_1 + href_index[2:]
                            # 这里是获取quick——look 这里就不拿了
                            fits_url = path_img_1 + img_tags[numb - 1].get('href')[2:]
                            # img_response = requests.get(img_url)
                            fits_response = requests.get(fits_url)
                            if fits_response.status_code == 200:
                                # img_filename = os.path.join(save_path, os.path.basename(img_url))
                                fits_filename = os.path.join(save_path, os.path.basename(fits_url))
                                # with open(img_filename, 'wb') as img_file:
                                #     img_file.write(img_response.content)
                                with open(fits_filename, 'wb') as fit_file:
                                    fit_file.write(fits_response.content)
                                    print('Download completed with fits '+fits_filename)

def fits2imge(path): # 用于将获取的fits 文件转化为img path为fits文件夹的位置
    import sys
    sys.path.append('./pyCallisto/src/')
    import pycallisto as pyc
    import pycallisto_utils as utils
    # 这里并没有报错 不用理会
    # import pyfits
    import astropy.io.fits as pyfits
    import matplotlib.pyplot as plt
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            name=root+'/'+file
            fits = pyc.PyCallisto.from_file(name)
            background_subtracted = fits.subtract_background()
            plt = background_subtracted.spectrogram()
            save_path=root+'_img'
            if os.path.exists(save_path) and os.path.isdir(save_path):
                print("文件夹存在")
            else:
                print("文件夹不存在")
                os.makedirs(save_path)
            plt.savefig(save_path+'/'+file+'.png')

if __name__ == '__main__':
    # get_text()
    # path = './text_save/e-CALLISTO_2020_05.txt'
    # get_fits(path)
    path='./fits_save/e-CALLISTO_2020_05'
    fits2imge(path)