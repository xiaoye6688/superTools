#!/usr/bin/env python3
"""
智商检测器 - 简化版本
"""

import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QLabel, QLineEdit, QProgressBar, 
                               QMessageBox, QFrame, QHBoxLayout)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QFont


class IQDetectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧠 智商检测器")
        self.setGeometry(300, 300, 500, 400)
        
        # 设置基础样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #2d2d2d;
                color: white;
                font-family: 'Microsoft YaHei', Arial, sans-serif;
            }
            QWidget {
                background-color: #2d2d2d;
                color: white;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #3d3d3d;
                border: 2px solid #555;
                border-radius: 8px;
                padding: 10px;
                font-size: 14px;
                color: white;
            }
            QLineEdit:focus {
                border-color: #2196F3;
            }
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #555;
                color: #999;
            }
            QProgressBar {
                border: none;
                border-radius: 8px;
                background-color: #555;
                text-align: center;
                color: white;
                font-weight: bold;
                height: 20px;
            }
            QProgressBar::chunk {
                border-radius: 8px;
                background-color: #4CAF50;
            }
            QFrame {
                background-color: #3d3d3d;
                border-radius: 10px;
                border: 1px solid #555;
                padding: 15px;
                margin: 5px;
            }
        """)
        
        # 检测状态
        self.is_detecting = False
        self.progress_value = 0
        
        self.setup_ui()
        self.setup_timer()
        
    def setup_ui(self):
        """设置用户界面"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(30, 30, 30, 30)
        main_layout.setSpacing(20)
        
        # 标题
        title = QLabel("🧠 智商检测器")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #2196F3; margin: 20px;")
        main_layout.addWidget(title)
        
        # 输入区域框架
        input_frame = QFrame()
        input_layout = QVBoxLayout(input_frame)
        
        # 输入说明
        input_label = QLabel("请输入您的智商：")
        input_label.setStyleSheet("font-size: 16px; margin-bottom: 10px;")
        input_layout.addWidget(input_label)
        
        # 输入框
        self.iq_input = QLineEdit()
        self.iq_input.setPlaceholderText("例如：120")
        self.iq_input.setMinimumHeight(40)
        input_layout.addWidget(self.iq_input)
        
        # 提示
        hint_label = QLabel("💡 提示：正常人智商范围为 85-115")
        hint_label.setStyleSheet("font-size: 12px; color: #999; margin-top: 5px;")
        input_layout.addWidget(hint_label)
        
        main_layout.addWidget(input_frame)
        
        # 检测按钮
        self.detect_button = QPushButton("🚀 开始检测")
        self.detect_button.setMinimumHeight(50)
        self.detect_button.clicked.connect(self.start_detection)
        main_layout.addWidget(self.detect_button)
        
        # 进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMinimumHeight(30)
        main_layout.addWidget(self.progress_bar)
        
        # 状态标签
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setVisible(False)
        self.status_label.setStyleSheet("font-size: 14px; color: #2196F3; margin: 10px;")
        main_layout.addWidget(self.status_label)
        
        # 添加弹性空间
        main_layout.addStretch()
        
    def setup_timer(self):
        """设置定时器"""
        self.detection_timer = QTimer()
        self.detection_timer.timeout.connect(self.update_progress)
        
    def start_detection(self):
        """开始检测"""
        input_text = self.iq_input.text().strip()
        
        # 验证输入
        if not input_text:
            QMessageBox.warning(self, "输入错误", "请先输入您的智商值！")
            return
            
        try:
            iq_value = float(input_text)
            if iq_value < 0 or iq_value > 300:
                QMessageBox.warning(self, "输入错误", "请输入合理的智商值（0-300）！")
                return
        except ValueError:
            QMessageBox.warning(self, "输入错误", "请输入有效的数字！")
            return
        
        # 开始检测动画
        self.is_detecting = True
        self.progress_value = 0
        
        # 更新UI状态
        self.detect_button.setEnabled(False)
        self.detect_button.setText("🔄 检测中...")
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_label.setVisible(True)
        self.status_label.setText("🔍 正在检测中...")
        
        # 启动进度条动画
        self.detection_timer.start(100)  # 每100ms更新一次
        
    def update_progress(self):
        """更新进度条"""
        if not self.is_detecting:
            return
            
        self.progress_value += random.randint(2, 5)
        
        # 更新进度条
        self.progress_bar.setValue(min(self.progress_value, 100))
        
        # 更新状态文字
        if self.progress_value < 30:
            self.status_label.setText("🧮 正在计算智商指数...")
        elif self.progress_value < 60:
            self.status_label.setText("📊 正在分析认知能力...")
        elif self.progress_value < 90:
            self.status_label.setText("🎯 正在评估智力水平...")
        else:
            self.status_label.setText("✨ 即将完成检测...")
        
        # 检测完成
        if self.progress_value >= 100:
            self.detection_timer.stop()
            self.complete_detection()
            
    def complete_detection(self):
        """完成检测"""
        self.is_detecting = False
        
        # 恢复按钮状态
        self.detect_button.setEnabled(True)
        self.detect_button.setText("🚀 重新检测")
        
        # 隐藏进度相关UI
        self.progress_bar.setVisible(False)
        self.status_label.setVisible(False)
        
        # 显示结果
        self.show_result()
        
    def show_result(self):
        """显示检测结果"""
        result_text = """🎉 检测完成！

🧠 您的智商为：250

📊 分析结果：
• 超越了 99.99% 的用户
• 智力等级：天才级别
• 认知能力：超凡脱俗

🏆 恭喜您！您拥有极其罕见的超高智商！"""
        
        QMessageBox.information(self, "🎉 智商检测结果", result_text)


def main():
    app = QApplication(sys.argv)
    
    # 设置应用程序属性
    app.setApplicationName("智商检测器")
    app.setApplicationVersion("1.0")
    
    # 创建主窗口
    window = IQDetectorWindow()
    window.show()
    
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
