import sys
import os
import subprocess


def createHardLink(original_file_name):
    try:
        output=subprocess.run(['ln',f"/home/nadeemshaik/Sample/{original_file_name}",f"/home/nadeemshaik/Sample/{original_file_name}_hardlink"],stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)

        if output.returncode!=0:
            print(output.stderr)
    except FileNotFoundError as e :
        print("Sorry the command is not valid")


def createSoftLink(original_file_name):
    try :
        output_softlink=subprocess.run(['ln','-s',f"/home/nadeemshaik/Sample/{original_file_name}",f"/home/nadeemshaik/Sample/{original_file_name}_softlink"],stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)

        print(output_softlink.returncode)
    except FileNotFoundError as e :
        print("Sorry the command not found")

def mapHardLinksAndSoftLinks():
    try :
        final_output_hardlinks=subprocess.run(['ls',"/home/nadeemshaik/Sample"],stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)
    except FileNotFoundError as e :
        print("Command not found")

    list_files_and_dirs=final_output_hardlinks.stdout.split("\n")
    finalList=[]

    for file_or_dir in list_files_and_dirs :
        if str(file_or_dir).__contains__('.'):
            finalList.append(str(file_or_dir))
    return finalList



dir_path=sys.argv[1]

# executing the first command
try:
    list_of_files=subprocess.run(['ls',"-l",dir_path],stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)
except FileNotFoundError as e :
    print(f"Sorry , Enter the valid command , for more info read this : {e}")

# executing the second commmand
try:
    list_of_files_ed_1=subprocess.run(['ls',dir_path],stdout=subprocess.PIPE,text=True,stderr=subprocess.PIPE)
except FileNotFoundError as e :
    print(f"Sorry Enter the valid command")





# returns the extra info
list_of_files_and_dirs=list_of_files.stdout.split("\n")

# returns jst the names of the files
list_files_dirs_ed_1=list_of_files_ed_1.stdout.split("\n")

# variable for storing all the files (without extra info)
files=[]

# variables for storing all the files (extra info)
files_extra_info=[]



# ignore all the directories and concentrate on files only since links are added to files
for i in range(1,len(list_of_files_and_dirs)):
    if len(list_of_files_and_dirs[i])>0:
        if (str(list_of_files_and_dirs[i]))[0]=='d':
            pass
        else:
            files.append(list_files_dirs_ed_1[i-1])
            files_extra_info.append(list_of_files_and_dirs[i])



# iterating through the files and creating hard links as well as softlinks

for file in files :
    if str(file).__contains__('_hardlink') or str(file).__contains__('_softlink'):
        pass
    else :
        createHardLink(file)
        createSoftLink(file)


hard_and_soft=mapHardLinksAndSoftLinks()
print(hard_and_soft)
