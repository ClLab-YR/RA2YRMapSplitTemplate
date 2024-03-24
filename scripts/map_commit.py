# -*- encoding: utf-8 -*-
# @File   : map_commit.py
# @Time   : 2024/01/12 18:42:22
# @Author : Chloride

from _common import ini, readConfig, splitMap

if __name__ == '__main__':
    yrpycfg = readConfig()
    _map = ini.INIClass()
    _map.read(str.replace(
        yrpycfg.get('gitutil.mappath', default='./target.map'), '"', ''))
    splitMap(_map, './src')
