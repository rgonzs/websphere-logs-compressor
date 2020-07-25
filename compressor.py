import os
import zipfile
from os import getcwd, walk
from os.path import basename
from datetime import date, timedelta
from zipfile import ZipFile

def logFiles():

    filesToCompress = []
    protectedFiles = ['SystemOut.log', 'SystemErr.log', 'native_stdout.log', 'native_stderr.log','pdfgen.log']

    for file in os.listdir('./'):
        if (file.endswith(".log")) and (getToday() not in file) and (file not in protectedFiles):
            file_name = file
            getToday()
            filesToCompress.append(file_name)
    return filesToCompress

def getDate():
    yesterday = date.today() - timedelta(days=1)
    return str(yesterday.strftime('%Y-%m-%d'))

def getToday():
    return str(date.today())

def main():
    
    currentDirectory = basename(getcwd())
    nameZip = getDate() + "-" + currentDirectory
    filesPath = logFiles()
    print('Los siguientes archivos van a ser comprimidos: ')
    for i in filesPath:
        print("- ", i)    
    with ZipFile(nameZip + '.zip', 'w', zipfile.ZIP_DEFLATED) as zip:
        try: 
            for i in filesPath:
                print("Comprimiendo el archivo " + i)
                zip.write(i)
                os.remove(i)
        except PermissionError:
            print("El archivo " + i +" esta siendo utilizado.")
if __name__ == "__main__":
    main()