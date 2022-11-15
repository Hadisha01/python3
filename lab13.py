f=input("Enter Source File:")

try:
    sf=open(f,"rb")

    c = input("Enter Target File:")
    cf=open(c,"wb")

    cf.write(sf.read())

    sf.close()
    cf.close()
    print("File Copied.")
except FileNotFoundError as e:
    print(e,"!!!")