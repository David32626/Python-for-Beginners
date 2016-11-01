import os

def rename_files():
    # get file names from a folder
    file_list = os.listdir()
    saved_path = os.getcwd()
    print ("current working directory is " + saved_path)
    os.chdir()
    for file_name in file_list:
        os.rename(file_name, xxx)
    os.chdir(saved_path)

def main():
    rename_files()

if __name__ == '__main__':
    main()