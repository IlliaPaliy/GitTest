import zipfile

jungle_zip = zipfile.ZipFile('gittest.zip','w')
jungle_zip.write('run.py', compress_type=zipfile.ZIP_DEFLATED)
jungle_zip.close()
