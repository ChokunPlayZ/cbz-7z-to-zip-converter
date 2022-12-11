from pyunpack import Archive
import os
import zipfile
import shutil

def zipdir(path, ziph):
    length = len(path)
    
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        folder = root[length:] # path without "parent"
        for file in files:
            ziph.write(os.path.join(root, file), os.path.join(folder, file))

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
                                                                             
Brought to you by: ChokunPlayZ

Github: https://github.com/chokunplayz
""")

print('Clearing Temp Folder')
for filename in os.listdir('./temp'):
    file_path = os.path.join('./temp', filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('[ERROR] Failed to delete %s. Reason: %s' % (file_path, e))

inputdir = os.listdir('./input')
print(f'[info] Listing Input Folder Contents \n > {inputdir}')

for i in inputdir :
    if i == 'filler.txt' or i == '.DS_Store' :
        pass
    else :
        print(f'[info] Extracting > {i}')
        Archive(f'./input/{i}').extractall("./temp")
        
        directory = f'./temp/'
        files = os.listdir(directory)

        print(f'[info] Repacking > {i}')

        zipf = zipfile.ZipFile(f'./output/{i}', 'w', zipfile.ZIP_DEFLATED)
        zipdir('temp', zipf)
        zipf.close()
        
        print(f'[info] Cleaning up temp files for > {i}')

        for filename in os.listdir('./temp'):
            file_path = os.path.join('./temp', filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('[ERROR] Failed to delete %s. Reason: %s' % (file_path, e))

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