#!/usr/bin/env python3
"""
电子木鱼 - Kivy 跨平台版本
支持：Windows EXE + Android APP
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse
from kivy.properties import NumericProperty
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.animation import Animation
import os
import sys

# 注册中文字体
FONT_PATH = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
if os.path.exists(FONT_PATH):
    resource_add_path(os.path.dirname(FONT_PATH))
    LabelBase.register(name='NotoSansCJK',
                      fn_regular=FONT_PATH)
    DEFAULT_FONT = 'NotoSansCJK'
else:
    DEFAULT_FONT = 'Roboto'

SOUND_FILE = os.path.join(os.path.dirname(__file__), 'muyu.wav')


class FishButton(Widget):
    count = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(on_touch_down=self.on_tap)

    def on_tap(self, instance, touch):
        if self.collide_point(*touch.pos):
            self.count += 1
            # 动画：缩放反馈
            anim = Animation(scale=0.85, duration=0.05) + \
                   Animation(scale=1.0, duration=0.12,
                             t='out_back')
            anim.start(self)

    def on_count(self, instance, value):
        app = App.get_running_app()
        app.root.ids.gongde_label.text = f'功德: {value}  次'


class WoodenFishLayout(BoxLayout):
    pass


class WoodenFishApp(App):
    def build(self):
        Window.clearcolor = (0.96, 0.96, 0.97, 1)  # Apple 浅灰背景
        return WoodenFishLayout()

    def reset(self):
        self.root.ids.fish_widget.count = 0


if __name__ == '__main__':
    WoodenFishApp().run()
