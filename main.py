#!/usr/bin/env python3
"""
电子木鱼 - main.py
"""
__version__ = '1.0'

# 用纯 tkinter 风格，但通过 p4a 的 sdl2 实现
# 由于 Kivy 在新 NDK 上有 pyjnius 兼容问题，
# 这里用 p4a 的 sdl2_ttf bootstrap 做简单界面

from pythonforandroid.recipe import Recipe
from pythonforandroid.bootstrap import Bootstrap

# 简单的启动入口
import sys
import os

# 打印版本信息
print('电子木鱼 v1.0')
print('Author: Davi L')
print('Built with python-for-android')
