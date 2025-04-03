# 图像处理程序
该程序重构离散余弦变换、离散傅氏变换、直方图均衡三个图像处理程序，使用qt进行可视化界面设计。

## 环境配置
### 1、anaconda安装
下载anaconda，请从[官网](https://www.anaconda.com/download)下载。
### 2、其余库安装
由于使用base环境进行设计，故无法导出环境yml，自行查看运行问题使用pip安装对应库（安装最新版本即可）

## 封装程序下载
本项目提供封装程序下载，点击按钮进行下载

下载安装包后解压，从位./dist/main/*.exe运行

## 项目结构
```
📂 Project Root                     # 项目根目录
├── 📜 README.md                     # 说明文档
├── 📂 res                           # 资源文件夹
│   └── 📜 img.py                    # 图像处理脚本
├── 📂 slot                          # 插槽函数
│   ├── 📜 DCT.py                    # 离散余弦变换
│   ├── 📜 DFT.py                    # 离散傅里叶变换
│   ├── 📜 equhist.py                 # 直方图均衡化
│   └── 📜 mainwindow.py              # 主窗口逻辑
├── 📂 ui                            # 界面文件
│   ├── 📜 ui_DCT.py                 # DCT 界面逻辑
│   ├── 📜 ui_DCT.ui                 # DCT 界面布局
│   ├── 📜 ui_DFT.py                 # DFT 界面逻辑
│   ├── 📜 ui_DFT.ui                 # DFT 界面布局
│   ├── 📜 ui_equhist.py             # 直方图均衡化界面逻辑
│   ├── 📜 ui_equhist.ui             # 直方图均衡化界面布局
│   ├── 📜 ui_mainwindow.py          # 主窗口界面逻辑
│   └── 📜 ui_mainwindow.ui          # 主窗口界面布局
└── 📜 main.py                        # 主程序入口

```