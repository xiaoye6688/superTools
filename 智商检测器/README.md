# 🧠 智商检测器

这是一个有趣的智商检测桌面应用程序，使用PySide6构建，具有现代化的界面设计。

## 特性

- 🧠 **智商检测**: 输入智商值进行"专业"检测
- 🎯 **现代化界面**: 深色主题，美观的UI设计
- 📊 **动态进度条**: 检测过程中的实时进度显示
- ✨ **动画效果**: 流畅的检测动画
- 🎉 **结果展示**: 弹窗显示检测结果

## 项目结构

```
智商检测器/
├── main.py              # 智商检测器主程序
├── requirements.txt     # 依赖列表
└── README.md           # 项目说明
```

## 安装和运行

### 方法一：直接安装依赖并运行

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 运行应用
python main.py
```

### 方法二：使用虚拟环境（推荐）

```bash
# 1. 创建虚拟环境
python -m venv venv

# 2. 激活虚拟环境
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 运行应用
python main.py
```

### 快速开始

如果您只想快速体验，可以直接运行：

```bash
pip install PySide6
python main.py
```

## 功能说明

### 智商检测器界面
- **标题区域**: 显示应用名称和版本信息
- **输入区域**: 用户输入智商值的文本框
- **检测按钮**: 点击开始智商检测过程
- **进度条**: 显示检测进度和状态信息
- **结果弹窗**: 显示最终的检测结果

### 检测流程
1. 用户在输入框中输入智商值
2. 点击"开始检测"按钮
3. 显示进度条和检测状态
4. 检测完成后弹出结果窗口
5. 显示"您的智商为250，超越了100%的用户"

## 自定义和扩展

### 修改界面样式
在 `main.py` 中的 `setStyleSheet` 方法中修改样式：

```python
# 修改主题颜色
self.setStyleSheet("""
    QMainWindow {
        background-color: #your_background_color;
    }
    QPushButton {
        background-color: #your_button_color;
    }
""")
```

### 修改检测结果
在 `show_result` 方法中自定义检测结果：

```python
def show_result(self):
    result_text = """您的自定义检测结果"""
    QMessageBox.information(self, "结果", result_text)
```

## 技术栈

- **PySide6**: Qt6的Python绑定
- **Python 3.9+**: 编程语言

## 使用说明

### 启动应用
运行以下命令启动智商检测器：
```bash
python main.py
```

### 操作步骤
1. **输入智商值**: 在输入框中输入任意数字（例如：120）
2. **开始检测**: 点击"🚀 开始检测"按钮
3. **观察进度**: 查看进度条和检测状态提示：
   - 🧮 正在计算智商指数...
   - 📊 正在分析认知能力...
   - 🎯 正在评估智力水平...
   - ✨ 即将完成检测...
4. **查看结果**: 检测完成后会弹出结果窗口
5. **重新检测**: 可以点击"🚀 重新检测"按钮进行多次测试

### 界面说明
- **输入区域**: 支持输入0-300范围内的数值
- **检测按钮**: 点击后开始模拟检测过程
- **进度条**: 显示检测进度（0-100%）
- **状态提示**: 显示当前检测阶段
- **结果弹窗**: 显示最终的"检测结果"

## 故障排除

### 常见问题

**问题1**: 运行时提示 `ModuleNotFoundError: No module named 'PySide6'`
```bash
# 解决方案：安装PySide6
pip install PySide6
```

**问题2**: 程序启动后没有界面显示
- 检查是否在图形界面环境中运行
- 确保Python版本支持（推荐Python 3.8+）

**问题3**: 虚拟环境相关问题
```bash
# 重新创建虚拟环境
python -m venv venv
# 激活并重新安装依赖
pip install -r requirements.txt
```

### 系统要求
- **Python**: 3.8 或更高版本
- **操作系统**: Windows 10+, macOS 10.14+, Linux
- **内存**: 至少 100MB 可用内存
- **显示**: 支持图形界面的环境

## 注意事项

⚠️ **这是一个娱乐性质的应用程序**
- 检测结果仅供娱乐，不具有任何科学依据
- 无论输入什么数值，结果都是固定的（智商250）
- 请勿将此应用用于任何正式的智商评估
- 本程序纯属娱乐，请理性对待结果

## 许可证

MIT License
