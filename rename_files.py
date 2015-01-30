import os
def rename_files():
    #(1) get file names from a folder
    path = '/Users/kseidl/Documents/Udacity/Python/prank/'
    file_list = os.listdir(path)
    os.chdir(path)
    print(file_list)

    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name -" +file_name)
        os.rename(file_name, file_name.translate(None, "0 1 2 3 4 5 6 7 8 9"))
        print("New Name -" + file_name)
 
rename_files()
