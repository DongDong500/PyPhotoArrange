import tkinter as tk
from tkinter import filedialog

from utils import photoarrange as pa


def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_entry.delete(0, tk.END)  # 기존의 내용 지우기
        directory_entry.insert(0, directory_path)

def process_directory():
    selected_directory = directory_entry.get()
    if selected_directory:
        print(f"Selected Directory: {selected_directory}")
        # 이 곳에서 선택된 디렉토리를 처리하는 추가적인 로직을 작성할 수 있습니다.
        pa.photoarrange(selected_directory)

    else:
        print("No directory selected.")

def center_window(window, width, height):
    # 창의 크기 설정
    window.geometry(f"{width}x{height}")



if __name__ == "__main__":
    # tkinter 창 생성
    root = tk.Tk()
    root.title("나의 사진 정리")

    # 창의 가로 및 세로 크기 설정
    window_width = 400
    window_height = 150
    center_window(root, window_width, window_height)

    # 디렉토리 입력을 위한 Entry 위젯 생성
    directory_entry = tk.Entry(root, width=50)
    directory_entry.pack(pady=10)

    # 디렉토리 선택 버튼 생성
    select_button = tk.Button(root, text="찾아보기", command=browse_directory)
    select_button.pack(pady=5)

    # 디렉토리 처리 버튼 생성
    process_button = tk.Button(root, text="사진 정리하기", command=process_directory)
    process_button.pack(pady=10)

    # GUI 창 실행
    root.mainloop()