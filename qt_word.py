import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class VocabularyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("背單詞應用")
        self.setFixedSize(350,350)
        
        # 單詞數據
        self.words = [
            {
                'word': 'aberration',
                'part_of_speech': 'n.',
                'meaning': '偏差；異常',
                'example': 'The outbreak in the city was an aberration.'
            },
            {
                'word': 'benevolent',
                'part_of_speech': 'adj.',
                'meaning': '仁慈的；善意的',
                'example': 'She was a benevolent woman, volunteering all of her free time.'
            },
            {
                'word': 'candid',
                'part_of_speech': 'adj.',
                'meaning': '坦率的；公正的',
                'example': 'He was candid about the difficulties the company was facing.'
            },
            # 可以添加更多單詞
        ]
        
        self.current_word = None
        
        # 設置界面元素
        self.setup_ui()
        self.next_word()
    
    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 單詞標籤
        self.word_label = QLabel()
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setFont(QFont("Helvetica", 24, QFont.Weight.Bold))
        self.word_label.setStyleSheet("color: #2E86C1;")
        main_layout.addWidget(self.word_label)
        
        # 詞性和意思
        self.pos_meaning_label = QLabel()
        self.pos_meaning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pos_meaning_label.setFont(QFont("Helvetica", 16, QFont.Weight.Normal, italic=True))
        self.pos_meaning_label.setStyleSheet("color: #28B463;")
        main_layout.addWidget(self.pos_meaning_label)
        
        # 例句框架
        example_frame = QFrame()
        example_frame.setFrameStyle(QFrame.Shape.StyledPanel | QFrame.Shadow.Raised)
        example_layout = QVBoxLayout(example_frame)
        
        example_title = QLabel("例句")
        example_title.setFont(QFont("Helvetica", 14))
        example_layout.addWidget(example_title)
        
        self.example_label = QLabel()
        self.example_label.setWordWrap(True)
        self.example_label.setFont(QFont("Helvetica", 12))
        example_layout.addWidget(self.example_label)
        
        main_layout.addWidget(example_frame)
        
        # 按鈕框架
        button_layout = QHBoxLayout()
        
        self.btn_not_know = QPushButton("不認識")
        self.btn_some_memory = QPushButton("有印象")
        self.btn_know = QPushButton("認識")
        
        for btn in [self.btn_not_know, self.btn_some_memory, self.btn_know]:
            btn.setFont(QFont("Helvetica", 12))
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498DB;
                    color: white;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #2980B9;
                }
            """)
            button_layout.addWidget(btn)
        
        main_layout.addLayout(button_layout)
        
        # 連接按鈕信號
        self.btn_not_know.clicked.connect(self.not_know)
        self.btn_some_memory.clicked.connect(self.some_memory)
        self.btn_know.clicked.connect(self.know)
    
    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.setText(self.current_word['word'])
        pos_meaning = f"{self.current_word['part_of_speech']} {self.current_word['meaning']}"
        self.pos_meaning_label.setText(pos_meaning)
        self.example_label.setText(self.current_word['example'])
    
    def not_know(self):
        print(f"不認識: {self.current_word['word']}")
        self.next_word()
    
    def some_memory(self):
        print(f"有印象: {self.current_word['word']}")
        self.next_word()
    
    def know(self):
        print(f"認識: {self.current_word['word']}")
        self.next_word()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VocabularyApp()
    window.show()
    sys.exit(app.exec())
