# 红红单张地图仓库模板

咱以后大概都是这么整罢。直接提交整张地图对 Git 而言无疑是种折磨。

Python 版本最低 `3.8.10`，更低版本未经测试。

推荐使用 [Visual Studio Code](https://code.visualstudio.com/) 管理地图仓库。  
脚本文件均置于`scripts`文件夹，以免喧宾夺主，影响正常的地图项目维护。

## 脚本和配置文件
配置文件`config.ini`**位于项目根目录**，而不是`scripts`文件夹。  
其中，路径带不带引号无所谓，用`/`还是`\`分割无所谓，等号两边有无空格也无所谓。

### 地图拆合
`map_commit.py`将指定地图（默认`./target.map`）拆分为`./src`里的分块文件。  
`map_packup.py`则相反，把分块文件重组为指定地图。  
二者作用于同一个地图文件，以保证迭代正常进行。
```ini
[Settings]
gitutil.mappath = ./target.map
```

### CSF 编译
`csf_compile.py`会将`.json`编译成`.csf`。
默认遵循下列设置：
```ini
[Settings]
csf.jsonfile = .\lang.json
csf.csffile = ./stringtable99.csf
```
