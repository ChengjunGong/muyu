[app]

title = 电子木鱼
package.name = muyu
package.domain = org.muyu

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ttf,json,ttc

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.permissions = VIBRATE

android.minapi = 21
android.api = 33

p4a.bootstrap = sdl2

android.icon.filename = icon.png

[buildozer]
log_level = 2
