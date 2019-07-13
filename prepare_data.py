import os, shutil


def make_dir(base_dir : str, sub_dir : str ) -> str:
    ''' Receives a directory and makes it '''

    dir = os.path.join(base_dir, sub_dir)
    os.mkdir(dir)

    for i in range(0, 43):

        aux = os.path.join(base_dir, sub_dir + '/' + format(i, '05d'))
        os.mkdir(aux)
        
    return dir

def extract_from_dir(src_dir : str, dst_dir):
    ''' Extracts part of the train samples to the validation directory '''
    fnames = ['00000_' + format(j, '05d') + '.ppm' for j in range(0, 30)]
        
    for i in range(0, 43):
        for fname in fnames:
            src = os.path.join(src_dir, format(i, '05d') + '/' + fname)
            dst = os.path.join(dst_dir, format(i, '05d') + '/' + fname)
            shutil.copyfile(src, dst) 
            os.remove(src)
            

original_dataset_dir = './GTSRB/Training'
base_dir = './GTSRB'

validation_dir = make_dir(base_dir, 'Validation')

extract_from_dir(original_dataset_dir, validation_dir)
