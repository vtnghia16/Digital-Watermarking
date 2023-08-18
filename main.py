import subprocess


def run_script(value):
    if value == '1':
        subprocess.run(["python", "pic.py"])
    elif value == '2':
        subprocess.run(["python", "vid.py"])
    elif value == '3':
        subprocess.run(["python", "dwt.py"])
    else:
        print("Giá trị không hợp lệ")


if __name__ == '__main__':
    print("----Vui lòng lựa chọn----")
    value = input("Chọn Hình(Nhập 1)/n/Chọn Video(Nhập 2)/Chọn DWT(Nhập 3): ")
    run_script(value)
