from pyunpack import Archive
import os ,zipfile ,shutil

print("""
 ██████╗██████╗ ███████╗                                                     
██╔════╝██╔══██╗╚══███╔╝                                                     
██║     ██████╔╝  ███╔╝                                                      
██║     ██╔══██╗ ███╔╝                                                       
╚██████╗██████╔╝███████╗                                                     
 ╚═════╝╚═════╝ ╚══════╝                                                     
                                                                             
███████╗███████╗    ████████╗ ██████╗     ███████╗██╗██████╗                 
╚════██║╚══███╔╝    ╚══██╔══╝██╔═══██╗    ╚══███╔╝██║██╔══██╗                
    ██╔╝  ███╔╝        ██║   ██║   ██║      ███╔╝ ██║██████╔╝                
   ██╔╝  ███╔╝         ██║   ██║   ██║     ███╔╝  ██║██╔═══╝                 
   ██║  ███████╗       ██║   ╚██████╔╝    ███████╗██║██║                     
   ╚═╝  ╚══════╝       ╚═╝    ╚═════╝     ╚══════╝╚═╝╚═╝                     
                                                                             
 ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                             
Brought to you by ChokunPlayZ

Github: https://github.com/chokunplayz
""")

print('Clearing Temp Folder')

# Define cleardir func with varible "dir" passed
def cleardir(dir):
    # for loop all files in "dir"
    for filename in os.listdir(dir):
        # get path file and set as varible "file_path"
        file_path = os.path.join(dir, filename)
        # "try" to do somthing
        try:
            # check if file exist
            if os.path.isfile(file_path) or os.path.islink(file_path):
                # delete file
                os.unlink(file_path)
            # if above statement is incorrect do below
            elif os.path.isdir(file_path):
                # delete directory
                shutil.rmtree(file_path)
        # If there is an error while trying to do somthing
        except Exception as e:
            print('[ERROR] Failed to delete %s. Reason: %s' % (file_path, e))

# call "cleardir" func above to clear folder "temp"
cleardir('./temp')

# get all files in "input" dir and set as varible "inputdir"
inputdir = os.listdir('./input')
# display all files in "input" dir
print(f'[info] Listing Input Folder Contents \n > {inputdir}')

# loop all files in "input" dir
for i in inputdir :
    # check if the filename extenstion is not ".cbz"
    if os.path.splitext(i)[1] != ".cbz" :
        # Skip file
        pass
    # if the above statement is incorrect
    else :
        print(f'[info] Extracting > {i}')
        # Extract input file to "temp" directory
        Archive(f'./input/{i}').extractall("./temp")
        
        # accounce temp directory as "directoy" varible
        directory = f'./temp/'
        # announce files inside "directory" as varible files
        files = os.listdir(directory)

        print(f'[info] Repacking > {i}')

        # Open a new zipfile handler
        zipfilehandler = zipfile.ZipFile(f'./output/{i}', 'w', zipfile.ZIP_DEFLATED)
        # get length of temp
        length = len('temp')
    
        # go through every file in temp
        for root, dirs, files in os.walk('temp'):
            # get folder inside temp
            folder = root[length:]
            # loop through files in folder
            for file in files:
                # write the file inside the new zip archive
                zipfilehandler.write(os.path.join(root, file), os.path.join(folder, file))

        # Close the zipfile handler
        zipfilehandler.close()
        
        print(f'[info] Cleaning up temp files for > {i}')

        # call "cleardir" func above to clear folder "temp"
        cleardir('./temp')

        # do everything again for all files in "input"

print("""
 █████╗ ██╗     ██╗         ██████╗  ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██║         ██╔══██╗██╔═══██╗████╗  ██║██╔════╝
███████║██║     ██║         ██║  ██║██║   ██║██╔██╗ ██║█████╗  
██╔══██║██║     ██║         ██║  ██║██║   ██║██║╚██╗██║██╔══╝  
██║  ██║███████╗███████╗    ██████╔╝╚██████╔╝██║ ╚████║███████╗
╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                               
███████╗███╗   ██╗     ██╗ ██████╗ ██╗   ██╗██╗                
██╔════╝████╗  ██║     ██║██╔═══██╗╚██╗ ██╔╝██║                
█████╗  ██╔██╗ ██║     ██║██║   ██║ ╚████╔╝ ██║                
██╔══╝  ██║╚██╗██║██   ██║██║   ██║  ╚██╔╝  ╚═╝                
███████╗██║ ╚████║╚█████╔╝╚██████╔╝   ██║   ██╗                
╚══════╝╚═╝  ╚═══╝ ╚════╝  ╚═════╝    ╚═╝   ╚═╝                
                                                               
""")