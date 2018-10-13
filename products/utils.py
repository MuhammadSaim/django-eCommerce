import random,string,os

# get extension of any file
def get_file_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)
    return name, ext

# get image path for upload image
def upload_image_path(instance, filename):
    new_filename = ''.join([random.choice(string.ascii_lowercase) for i in range(16)])
    name, ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{final_filename}'