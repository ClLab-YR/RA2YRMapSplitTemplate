# 红红单张地图仓库模板
受[岛风](https://github.com/frg2089)的提案启发，结合古早打理“脑死”的经验诞生的模板仓库。当然很大程度上应该是我自用。

> [!important]
> 已经使用此模板的仓库请自行考虑是否**手动**适配更新。  
> `pyalert2yr`包说实话并不是很完善，本仓库模板的每一次更新都伴随着 py 包的重要修复。  
> 但强行跟进往往会对你的仓库里已经写好的脚本（可能包括你自己后加的）造成重大的兼容性问题。

## 入门和配置
[Github 模板仓库说明书](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)  
建议使用 Visual Studio Code 打开项目目录。

脚本需要安装 Python（≥v3.8）才能食用，包依赖参考`pyalert2yr`项目的`requirements.txt`即可。

子库依赖需要单独克隆：`git submodule update --init`。  
我是 SSH 优先，不好使的话不妨打开`.gitmodules`将 url 改为`https://github.com/ClLab-YR/pyalert2yr.git`再重试。

## 脚本食用
直接运行`scripts`目录底下的脚本即可。
- `csf_compile.py`把`.json`编译成`.csf`；
- `map_commit.py`把`.map`拆分为`src`目录下的`.ini`和`.mappkg`分块；
- `map_packup.py`把`src`目录下的分块重组为`.map`文件。

项目（不是脚本）的根目录中可新建`config.ini`用于配置上述脚本操作的文件：
```ini
[Settings]
csf.jsonfile = ./lang.json
csf.csffile = ./stringtable99.csf
gitutil.mappath = ./target.map
```
其中，`\`还是`/`无所谓；两端是否有引号无所谓；等号两边有无空格也无所谓。

当然，也可以考虑自写脚本。只要你管理起来没什么压力就行（。  
希望你作图愉快（笑）
