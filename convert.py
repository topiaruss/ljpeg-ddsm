import os
from multiprocessing import Pool

path_to_ddsm = "/home/pc1/data/DDSM/figment.csee.usf.edu/pub/DDSM/"


def process(dir_node):
    root, sub_folders, file_names = dir_node
    for file_name in file_names:
        if file_name.endswith(".LJPEG"):
            old_path = os.path.join(root, file_name)
            new_path = old_path.split('.LJPEG')[0] + ".jpg"
            cmd = './ljpeg.py "{0}" "{1}" --visual --scale 1.0'.format(old_path, new_path)
            os.system(cmd)
            os.system('mv %s %s' % (old_path, old_path + '.processed'))
    return root


with Pool(processes=8) as pool:
    for node in pool.imap_unordered(process, os.walk(path_to_ddsm)):
        print(node)

print('done')
