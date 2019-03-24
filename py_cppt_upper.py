# クリップボード内をすべて大文字にする
import pyperclip

#クリップボードからテキストを
txt = pyperclip.paste()

# 行をそのまま、大文字に変換する
txt = txt.upper()

pyperclip.copy(txt)