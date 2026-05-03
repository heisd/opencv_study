# OpenCV 学习笔记

基于 Python + OpenCV 的图像处理与视频处理入门示例合集。

## 环境要求

- Python 3.7+
- OpenCV：`pip install opencv-python`
- NumPy：`pip install numpy`
- Matplotlib（可选）：`pip install matplotlib`

## 项目结构

```
opencv_study/
├── image/
│   └── img.png                    # 示例图片
├── video/
│   └── video.mp4                  # 示例视频
├── src/
│   ├── opencv_image_imread.py     # 图片读取与显示
│   ├── opencv_draw.py             # 基本图形绘制
│   ├── opencv_video.py            # 视频播放（彩色 + 灰度）
│   ├── opencv_video_camera.py     # 调用本机摄像头
│   ├── opencv_video_save.py       # 视频读取并保存
│   └── easy_using_matplotlib.py   # 使用 Matplotlib 展示图片
└── README.md
```

## 示例说明

### 1. 图片读取与显示 (`opencv_image_imread.py`)

演示 `cv2.imread` 的三种读取模式：

| 参数值 | 说明 |
|--------|------|
| `1`    | 彩色图片（默认） |
| `0`    | 灰度图片 |
| `-1`   | 保留透明通道（BGRA） |

运行后会分别展示彩色、灰度、带透明度三个窗口，按 `q` 退出。

```bash
python src/opencv_image_imread.py
```

---

### 2. 基本图形绘制 (`opencv_draw.py`)

在空白画布上演示常用绘图 API：

- `cv2.line` — 画直线
- `cv2.rectangle` — 画矩形
- `cv2.circle` — 画圆形

```bash
python src/opencv_draw.py
```

---

### 3. 视频播放 (`opencv_video.py`)

读取本地视频文件，同时展示**彩色**和**灰度**两个播放窗口，按 `q` 退出。

```bash
python src/opencv_video.py
```

---

### 4. 摄像头实时预览 (`opencv_video_camera.py`)

调用设备默认摄像头（索引 `0`），实时展示画面，按 `q` 退出。

```bash
python src/opencv_video_camera.py
```

---

### 5. 视频保存 (`opencv_video_save.py`)

读取本地视频并以 **XVID** 编码格式保存到 `video/saved_video.avi`，按 `q` 提前停止。

```bash
python src/opencv_video_save.py
```

---

### 6. Matplotlib 展示图片 (`easy_using_matplotlib.py`)

使用 Matplotlib 代替 `cv2.imshow` 展示图片，适合在 Jupyter Notebook 等环境中使用。
注意：OpenCV 使用 BGR 通道顺序，Matplotlib 使用 RGB，脚本中已做转换。

```bash
python src/easy_using_matplotlib.py
```

## 常见问题

**Q: 运行后窗口一闪而过？**
确保脚本末尾调用了 `cv2.waitKey(0)` 或 `cv2.waitKey(1)`（视频场景）。

**Q: 视频/图片无法读取（返回 None）？**
检查 `image/` 和 `video/` 目录下的文件是否存在，路径区分大小写。

**Q: 摄像头无法打开？**
确认摄像头已连接，或尝试将 `VideoCapture(0)` 改为 `VideoCapture(1)`。
