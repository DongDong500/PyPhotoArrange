import tkinter as tk
from tkinter import filedialog

from utils import photoarrange as pa


def browse_directory(directory_entry):
    directory_path = filedialog.askdirectory()
    if directory_path:
        directory_entry.delete(0, tk.END)  # 기존의 내용 지우기
        directory_entry.insert(0, directory_path)

def process_directory(directory_entry, dst_entry):
    selected_directory = directory_entry.get()
    dst_directory = dst_entry.get()
    if selected_directory and dst_entry:
        print(f"Selected Directory: {selected_directory}")
        print(f"Destination Directory: {dst_directory}")
        # 이 곳에서 선택된 디렉토리를 처리하는 추가적인 로직을 작성할 수 있습니다.
        pa.photoarrange(selected_directory, dst_directory)
    else:
        print("No directory selected.")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')



if __name__ == "__main__":
    # tkinter 창 생성
    root = tk.Tk()
    root.title("나의 사진 정리")

    # 창의 가로 및 세로 크기 설정
    window_width = 500
    window_height = 150
    center_window(root, window_width, window_height)

    # 디렉토리 입력을 위한 Entry 위젯 생성
    directory_entry = tk.Entry(root, width=50)
    directory_entry.grid(row=0, column=1, padx=10, pady=10)
    # 디렉토리 선택 버튼 생성
    select_button = tk.Button(root, text="찾아보기", command=lambda: browse_directory(directory_entry))
    select_button.grid(row=0, column=0, padx=10, pady=10)

    # 디렉토리 입력을 위한 Entry 위젯 생성
    dst_entry = tk.Entry(root, width=50)
    dst_entry.grid(row=1, column=1, padx=10, pady=10)
    # 저장할 데렉토리 선택 버튼 생성
    dst_button = tk.Button(root, text="저장위치", command=lambda: browse_directory(dst_entry))
    dst_button.grid(row=1, column=0, padx=10, pady=10)

    # 디렉토리 처리 버튼 생성
    process_button = tk.Button(root, text="사진 정리하기", command=lambda: process_directory(directory_entry, dst_entry))
    process_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # GUI 창 실행
    root.mainloop()