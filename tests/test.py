import FS
import time


if __name__ == "__main__":
    
    fil = FS.FileShareClass()
    print(fil.start_fileShare("C:/users/harsh/desktop"))
    time.sleep(20)
    fil.stopFileShare()