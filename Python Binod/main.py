import os

def isBinod(filename):
    with open(filename, 'r') as f:
        fileContent=f.read()

    if "binod" in fileContent.lower():
        return True
    else:
        return False




if __name__ == '__main__':
    dir_contents=os.listdir()
    print(dir_contents)
    nBinod=0
    for item in dir_contents:
        if item.endswith('txt'):
            print(f"Detecting Binod in {item}")
            flag=isBinod(item)
            if (flag):
                print(f"Binod fond in {item}")
                nBinod+=1
            else:
                print(f"Binod not found in {item}")


    print("Binod detect summary")
    print(f"{nBinod} files found into the file which is hidden into them")