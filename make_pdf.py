import os
from PIL import Image


def extract_last_number(filename):
    name = os.path.splitext(filename)[0]
    try:
        return int(name.split('_')[-1])
    except ValueError:
        return -1


def images_to_pdf(folder_path, base_name):

    valid_exts = ('.png', '.jpg', '.jpeg')

    image_files = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(valid_exts)],
        key=extract_last_number
    )

    if not image_files:
        print(f"{base_name} : 해당 폴더에 이미지가 없습니다.")
        return

    image_list = []
    for filename in image_files:
        path = os.path.join(folder_path, filename)
        img = Image.open(path).convert('RGB')
        image_list.append(img)

    first_image = image_list.pop(0)
    output_path = os.path.join(save_path, base_name + ".pdf")
    first_image.save(output_path, save_all=True, append_images=image_list)
    print(f"{base_name}.pdf")


def get_subfolder_names(parent_folder):
    subfolders = [
        name for name in os.listdir(parent_folder)
        if os.path.isdir(os.path.join(parent_folder, name))
    ]

    for i, subfolder in enumerate(subfolders):
        subfolder_path = os.path.join(parent_folder, subfolder)
        images_to_pdf(subfolder_path, subfolder)


root_path = "/Users/yoma/Downloads/screenshots"
save_path = "/Users/yoma/Downloads/ebooks"
get_subfolder_names(root_path)
