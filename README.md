# 图像处理程序
[![TensorFlow](https://badgen.net/github/release/KingJerrick/NJUST_image-processing/stable)](https://objects.githubusercontent.com/github-production-release-asset-2e65be/959605317/88f827e1-9e64-4a7e-bf9b-58d1c2918297?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=releaseassetproduction%2F20250403%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250403T083404Z&X-Amz-Expires=300&X-Amz-Signature=9f576ea392e4966bd6f04fea2f18eb2a70f6e6c81724e756cf248dcf42abab10&X-Amz-SignedHeaders=host&response-content-disposition=attachment%3B%20filename%3DProcess_v4.0.0_realse.rar&response-content-type=application%2Foctet-stream)
![Python](https://img.shields.io/badge/Python-14354C.svg?logo=python&logoColor=white)
![](https://img.shields.io/badge/Qt-%23217346.svg?style=flat&logo=Qt&logoColor=white)

该程序重构离散余弦变换、离散傅氏变换、直方图均衡三个图像处理程序，使用qt进行可视化界面设计。

## 环境配置
### 1、anaconda安装
下载anaconda，请从[官网](https://www.anaconda.com/download)下载。
### 2、其余库安装
由于使用base环境进行设计，故无法导出环境yml，自行查看运行问题使用pip安装对应库（安装最新版本即可）

## 封装程序下载
本项目提供封装程序下载，点击上方release按钮进行下载

下载安装包后解压，从位./main/*.exe运行

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