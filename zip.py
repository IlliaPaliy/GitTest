import zipfile

jungle_zip = zipfile.ZipFile('D:\\Codes\\git\\gittest.zip','w')
jungle_zip.write('D:\\Codes\\git\\run.py', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()