import time,sys
indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('**************')
        time.sleep(0.02)

        if indentIncreasing:
            indent = indent + 2
            if indent == 100:
                indentIncreasing = False
        else:
            indent = indent - 2
            if indent == 0: 
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
