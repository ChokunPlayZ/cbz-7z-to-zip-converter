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

def cleardir(dir):
    for filename in os.listdir(dir):
        file_path = os.path.join(dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('[ERROR] Failed to delete %s. Reason: %s' % (file_path, e))

cleardir('./temp')

inputdir = os.listdir('./input')
print(f'[info] Listing Input Folder Contents \n > {inputdir}')

for i in inputdir :
    if os.path.splitext('my_file.txt') != "cbz" :
        pass
    else :
        print(f'[info] Extracting > {i}')
        Archive(f'./input/{i}').extractall("./temp")
        
        directory = f'./temp/'
        files = os.listdir(directory)

        print(f'[info] Repacking > {i}')

        zipfilehandler = zipfile.ZipFile(f'./output/{i}', 'w', zipfile.ZIP_DEFLATED)
        length = len('temp')
    
        for root, dirs, files in os.walk('temp'):
            folder = root[length:]
            for file in files:
                zipfilehandler.write(os.path.join(root, file), os.path.join(folder, file))

        zipfilehandler.close()
        
        print(f'[info] Cleaning up temp files for > {i}')

        cleardir('./temp')

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