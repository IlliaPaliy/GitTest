import zipfile

<<<<<<< HEAD
jungle_zip = zipfile.ZipFile('gittest.zip','w')
jungle_zip.write('D:\\Codes\\git\\run.py', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
=======
jungle_zip = zipfile.ZipFile('D:\\Codes\\git\\gittest.zip','w')
jungle_zip.write('GitTest/run.py', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
>>>>>>> 813616378c6ba0f209dbf3404094885df35b084d
