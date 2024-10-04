import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class VocabularyApp(QMainWindow):
    def __init__(self, vocab_list):
        super().__init__()
        self.vocab_list = vocab_list
        self.index = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("背單詞")
        self.setFixedSize(350, 250)
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # 單詞標籤
        self.word_label = QLabel('', self)
        self.word_label.setFont(QFont('Arial', 16, QFont.Weight.Bold))
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.word_label)

        # 音標標籤
        self.phonetic_label = QLabel('', self)
        self.phonetic_label.setFont(QFont('Arial', 12))
        self.phonetic_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.phonetic_label)

        # 詞性標籤
        self.pos_label = QLabel('', self)
        self.pos_label.setFont(QFont('Arial', 12))
        self.pos_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.pos_label)

        # 詞義標籤
        self.meaning_label = QLabel('', self)
        self.meaning_label.setFont(QFont('Arial', 12))
        self.meaning_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.meaning_label)

        # 例句標籤
        self.example_label = QLabel('', self)
        self.example_label.setFont(QFont('Arial', 10))
        self.example_label.setWordWrap(True)
        self.example_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.example_label)

        # 按鈕佈局
        button_layout = QHBoxLayout()
        
        self.prev_button = QPushButton('<< 上一個', self)
        self.prev_button.clicked.connect(self.show_prev)
        button_layout.addWidget(self.prev_button)

        self.next_button = QPushButton('下一個 >>', self)
        self.next_button.clicked.connect(self.show_next)
        button_layout.addWidget(self.next_button)

        layout.addLayout(button_layout)

        # 顯示第一個單詞
        self.show_word()

    def show_word(self):
        word_data = self.vocab_list[self.index]
        self.word_label.setText(word_data['word'])
        self.phonetic_label.setText('音標：' + word_data['phonetic'])
        self.pos_label.setText('詞性：' + word_data['pos'])
        self.meaning_label.setText('詞義：' + word_data['meaning'])
        self.example_label.setText('例句：' + word_data['example'])

    def show_next(self):
        if self.index < len(self.vocab_list) - 1:
            self.index += 1
            self.show_word()
        else:
            QMessageBox.information(self, "提示", "已經是最後一個單詞")

    def show_prev(self):
        if self.index > 0:
            self.index -= 1
            self.show_word()
        else:
            QMessageBox.information(self, "提示", "已經是第一個單詞")

def parse_vocab_file(filename):
    vocab_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                parts = line.split(' ', 4)
                if len(parts) == 5:
                    word, phonetic, pos, meaning, example = parts
                    vocab_list.append({
                        'word': word,
                        'phonetic': phonetic,
                        'pos': pos,
                        'meaning': meaning,
                        'example': example
                    })
                else:
                    print(f"第 {line_num} 行格式錯誤，已跳過：{line}")
        return vocab_list
    except FileNotFoundError:
        print(f"未找到文件：{filename}")
        return []

if __name__ == '__main__':
    vocab_list = parse_vocab_file('vocab.txt')
    
    if vocab_list:
        app = QApplication(sys.argv)
        window = VocabularyApp(vocab_list)
        window.show()
        sys.exit(app.exec())
    else:
        print("未能加載單詞列表，請檢查文件是否存在或格式是否正確。")
