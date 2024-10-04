import tkinter as tk
from tkinter import messagebox

class VocabularyApp:
    def __init__(self, master, vocab_list):
        self.master = master
        self.master.title("背單詞")
        # 設置窗口總是在最前
        self.master.attributes('-topmost', True)
        # 設置窗口大小
        self.master.geometry('350x250')
        # 禁止調整窗口大小
        self.master.resizable(False, False)
        
        self.vocab_list = vocab_list
        self.index = 0

        # 單詞標籤
        self.word_label = tk.Label(master, text='', font=('Arial', 16, 'bold'))
        self.word_label.pack(pady=5)

        # 音標標籤
        self.phonetic_label = tk.Label(master, text='', font=('Arial', 12))
        self.phonetic_label.pack(pady=5)

        # 詞性標籤
        self.pos_label = tk.Label(master, text='', font=('Arial', 12))
        self.pos_label.pack(pady=5)
        
        # 詞義標籤
        self.meaning_label = tk.Label(master, text='', font=('Arial', 12))
        self.meaning_label.pack(pady=5)
        
        # 例句標籤
        self.example_label = tk.Label(master, text='', font=('Arial', 10), wraplength=330, justify='left')
        self.example_label.pack(pady=5)
        
        # 按鈕框架
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)
        
        # 上一個按鈕
        self.prev_button = tk.Button(button_frame, text='<< 上一個', command=self.show_prev)
        self.prev_button.pack(side='left', padx=10)

        # 下一個按鈕
        self.next_button = tk.Button(button_frame, text='下一個 >>', command=self.show_next)
        self.next_button.pack(side='right', padx=10)
        
        # 顯示第一個單詞
        self.show_word()
        
    def show_word(self):
        word_data = self.vocab_list[self.index]
        self.word_label.config(text=word_data['word'])
        self.phonetic_label.config(text='音標：' + word_data['phonetic'])
        self.pos_label.config(text='詞性：' + word_data['pos'])
        self.meaning_label.config(text='詞義：' + word_data['meaning'])
        self.example_label.config(text='例句：' + word_data['example'])
        
    def show_next(self):
        if self.index < len(self.vocab_list) - 1:
            self.index += 1
            self.show_word()
        else:
            messagebox.showinfo("提示", "已經是最後一個單詞")
        
    def show_prev(self):
        if self.index > 0:
            self.index -= 1
            self.show_word()
        else:
            messagebox.showinfo("提示", "已經是第一個單詞")
        
def parse_vocab_file(filename):
    vocab_list = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                # 按最多分割4次，確保例句中有空格也不會影響
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
        root = tk.Tk()
        app = VocabularyApp(root, vocab_list)
        root.mainloop()
    else:
        print("未能加載單詞列表，請檢查文件是否存在或格式是否正確。")
