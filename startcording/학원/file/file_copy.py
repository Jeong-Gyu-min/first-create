buffer_size = 1024
with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/code.mp4", "rb") as source:
    with open("C:/Users/wjdrb/OneDrive/바탕 화면/PythonWorkspace/학원/section13/input/code2.mp4", "wb") as copy:
        while True:
            buffer = source.read(buffer_size)
            if not buffer:
                break
            copy.write(buffer)
            
print("code2.mp4 파일이 복사되었습니다.")
