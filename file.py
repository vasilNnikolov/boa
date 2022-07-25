import os
import shutil
from random import randint


base_dir = os.getcwd()
forbidden_dirs = [os.path.join(base_dir, "Games"), os.path.join(base_dir, "bad_images")]
def copy_random_image(directory):
    image_names = [
        os.path.join(base_dir, "bad_images", name) for name in os.listdir(os.path.join(base_dir, "bad_images"))
    ]

    rnd_image = image_names[randint(0, len(image_names) - 1)]
    extension = rnd_image.split(".")[-1]
    new_name = f"{randint(0, 1000)}_amogus_burger_king_{randint(0, 69)}.{extension}"

    shutil.copyfile(rnd_image, os.path.join(directory, new_name))

def count_dirs(directory, max_depth):
    if max_depth == 0: 
        return 1
    normal_subdirs = []
    for sd in os.listdir(directory): 
        full_sd_name = os.path.join(directory, sd)
        if not sd.startswith(".") and os.path.isdir(full_sd_name) and not (full_sd_name in forbidden_dirs):
            normal_subdirs.append(full_sd_name)

    if len(normal_subdirs) == 0: 
        return 1
    return sum([count_dirs(sd, max_depth - 1) for sd in normal_subdirs]) 


def recurse_through_filetree(directory, n_dirs, n_replications, max_depth):
    if max_depth == 0: 
        return
    normal_subdirs = []
    for sd in os.listdir(directory): 
        full_sd_name = os.path.join(directory, sd)
        if not sd.startswith(".") and os.path.isdir(full_sd_name) and not (full_sd_name in forbidden_dirs):
            normal_subdirs.append(full_sd_name)

    for sd in normal_subdirs: 
        if randint(0, int(n_dirs/n_replications) - 1) == 0:
            copy_random_image(sd)
        recurse_through_filetree(sd, n_dirs, n_replications, max_depth - 1)

max_depth = 7
n_dirs = count_dirs(base_dir, max_depth)
n_replications = min(300, n_dirs) 
print(f"n_dirs: {n_dirs}")

recurse_through_filetree(base_dir, n_dirs, n_replications, max_depth)
