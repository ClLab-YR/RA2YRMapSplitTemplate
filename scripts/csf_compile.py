# -*- encoding: utf-8 -*-
# @File   : csf_compile.py
# @Time   : 2024/01/12 18:54:25
# @Author : Chloride

from _common import csf, readConfig

if __name__ == '__main__':
    yrpycfg = readConfig()
    fj = str.replace(
        yrpycfg.get('csf.jsonfile', default='./lang.json'), '"', '')
    fc = str.replace(
        yrpycfg.get('csf.csffile', default='./stringtable99.csf'), '"', '')
    csfdoc = csf.importJSONV2(fj)
    csfdoc.writeCsf(fc)
