# 图像处理程序
[<img src="https://github.com/KingJerrick/icon/blob/main/njust.png" height="100"/>](https://www.njust.edu.cn/)[<img src="https://github.com/KingJerrick/icon/blob/main/physic.webp" height="100"/>](https://physics.njust.edu.cn/main.htm)

[![Author](https://img.shields.io/badge/Author-Jerrick-blue)](mailto:zhechen0224@outlook.com)
[![TensorFlow](https://badgen.net/github/release/KingJerrick/NJUST_image-processing/stable)](https://github.com/KingJerrick/NJUST_image-processing/releases/tag/v4.0.0)
[![Python](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white)](https://www.python.org/)
[![](https://img.shields.io/badge/Qt-%23217346.svg?style=flat&logo=Qt&logoColor=white)](https://www.qt.io/download-dev)

该程序重构离散余弦变换、离散傅氏变换、直方图均衡三个图像处理程序，使用qt进行可视化界面设计。

## 环境配置
### 1、anaconda安装
下载anaconda，请从[官网](https://www.anaconda.com/download)下载。

## 封装程序下载
本项目提供封装程序下载，包含免安装版本和安装版本

免安装版本下载后解压，从位./main/*.exe运行

## 项目结构
```
📂 Project Root                     # 项目根目录
├── 📜 README.md                     # 说明文档
├── 📂 res                           # 资源文件夹
│   └── 📜 img.py                    # 图标脚本
├── 📂 slot                          # 槽函数
│   ├── 📜 DCT.py                    # 离散余弦变换槽函数
│   ├── 📜 DFT.py                    # 离散傅里叶变换槽函数
│   ├── 📜 equhist.py                # 直方图均衡槽函数
│   └── 📜 mainwindow.py             # 主窗口逻辑
├── 📂 ui                            # 界面文件
│   ├── 📜 ui_DCT.py                 # DCT 界面逻辑
│   ├── 📜 ui_DCT.ui                 # DCT 界面布局
│   ├── 📜 ui_DFT.py                 # DFT 界面逻辑
│   ├── 📜 ui_DFT.ui                 # DFT 界面布局
│   ├── 📜 ui_equhist.py             # 直方图均衡化界面逻辑
│   ├── 📜 ui_equhist.ui             # 直方图均衡化界面布局
│   ├── 📜 ui_mainwindow.py          # 主窗口界面逻辑
│   └── 📜 ui_mainwindow.ui          # 主窗口界面布局
└── 📜 main.py                       # 主程序入口
```
## 联系作者
通过上方标签可直接向作者发送邮件
