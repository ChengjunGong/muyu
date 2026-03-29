# 电子木鱼 - Android APK 构建说明

## 快速开始（3分钟完成）

### 1. 创建 GitHub 仓库
- 访问 https://github.com/new
- 仓库名称填写：`muyu`（或任意名称）
- 勾选 **Public**（公开仓库，免费）
- 点击 **Create repository**

### 2. 上传文件
在仓库页面，点击 **Add file → Upload files**，把以下 6 个文件全部拖进去：

| 文件 | 说明 |
|------|------|
| `main.py` | 入口文件 |
| `muyu_kivy.py` | 主程序 |
| `muyu.kv` | 界面布局 |
| `buildozer.spec` | 构建配置 |
| `icon.png` | 应用图标 |
| `.github/workflows/build.yml` | 自动构建脚本（需要先创建文件夹） |

**注意：** `.github/workflows/build.yml` 需要这样创建：
1. 点击 **Add file → Create new file**
2. 文件名填写：`.github/workflows/build.yml`
3. 把 `build.yml` 的内容粘贴进去
4. 点击 **Commit new file**

### 3. 等待构建（约 10-15 分钟）
- 切换到 **Actions** 标签页
- 可以看到构建进度
- 绿色 ✓ 表示成功，红色 ✗ 表示失败

### 4. 下载 APK
- 构建成功后，点击 **Artifacts** 或直接下载
- 文件名：`org.muyu-1.0-arm64-v8a_armeabi-v7a-debug.apk`
- 传到手机安装即可

---

## 构建产物

- **Debug APK**：`bin/*.apk`（约 30-50MB）
- 支持架构：arm64-v8a + armeabi-v7a

## 故障排除

**Q: Actions 显示红色失败？**
- 点击失败的 workflow 查看日志
- 常见问题：网络超时（重试即可）

**Q: 安装到手机后闪退？**
- 可能是 Android 版本问题，检查手机系统 Android 5.0+

**Q: 想更新代码？**
- 直接在 GitHub 网页编辑文件，或重新上传
- 更新后会自动重新构建
