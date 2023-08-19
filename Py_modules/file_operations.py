try:
    f = open("my_file.txt", "r")
    #print(f.read())  # read all file
    #print(f.readlines()) #read as list
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

finally:
    f.close()
