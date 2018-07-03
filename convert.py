import os

path_to_ddsm = "/home/pc1/data/DDSM/figment.csee.usf.edu/pub/DDSM/"

for root, subFolders, file_names in os.walk(path_to_ddsm):
    for file_name in file_names:
        if file_name.endswith(".LJPEG"):
            ljpeg_path = os.path.join(root, file_name)
            old_path = os.path.join(root, file_name)
            new_path = old_path.split('.LJPEG')[0] + ".jpg"
            
            cmd = './ljpeg.py "{0}" "{1}" --visual --scale 1.0'.format(ljpeg_path, new_path)
            os.system(cmd)
            os.system('mv %s %s' % (old_path, old_path+'.processed'))

print('done')