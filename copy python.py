ile=input("Enter Source File:")
try:
    sf=open(sfile,"rb")

    tfile = input("Enter Target File:")
    tf=open(tfile,"wb")

    tf.write(sf.read())

    sf.close()
    tf.close()
    print("File Copied...")
except FileNotFoundError as e:
    print(e)
