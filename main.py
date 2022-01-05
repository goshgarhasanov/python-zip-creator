import zipfile
import zipfile as zf
import os
from termcolor import colored

def addFile(zipFileName,fileName):
    with open(fileName,'w') as f:
        f.write('Hello Python')
    filelist=os.listdir()
    if not zipFileName in filelist:
        yazi='w'
    else:
        yazi='a'
    zip = zf.ZipFile(zipFileName, yazi)

    zip.write(fileName)
    print(colored(f'{zipFileName} Fayli yaradildi','green'))
    print(colored(f'{fileName} Fayli Sıxıştırıldı','green'))
    zip.close()

def extractFile(zipFileName):
    filelist = os.listdir()
    if zipFileName in filelist:
        with zf.ZipFile(zipFileName,'r')as zip:
            zip.extractall()
            print(colored('Bütün fayllar arxivdən çıxarıldı', 'green'))

    else:
        print(colored(f'{zipFileName} adli fayl tapilmadi', 'red'))



def isZipFile(zipFileName):
    if not zipFileName.endswith('.zip'):
        return zipFileName + '.zip'
    else:
        return zipFileName



while True:
    process = input(""" 
    Yeni Zip Fayl ve Yeni Fayl Yaratmaq üçün 1
    Varolan Zip Faylı Extract Etmək     üçün 2
    
     daxil edin  : """)
    inputFileName = input(
        """
        Zip Fayl Adini Daxil Edin
        Nümunə: example.zip
        """
    )
    if(process=='1'):
        fileName=input(
            """
            Zip Fayla Sıxışdıralacaq 
            Fayl Adını Daxil Edin
            Nümunə: example.txt
            """
        )
        zipFilename=isZipFile(inputFileName)
        addFile(zipFilename,fileName)

    elif(process=='2'):
        extractFile(inputFileName)
    else:
        print("Yalnish sechim")




