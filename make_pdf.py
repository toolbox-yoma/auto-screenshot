import os
import img2pdf


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

    images = [os.path.join(folder_path, f) for f in image_files]
    output_path = os.path.join(save_path, base_name + ".pdf")

    try:
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(images))
        print(f"{base_name}.pdf 생성 완료")

        # import shutil
        # shutil.rmtree(folder_path)
        # print(f"{folder_path} 폴더 삭제 완료")

    except Exception as e:
        print(f"PDF 생성 실패: {e}")


def get_subfolder_names(parent_folder):
    subfolders = [
        name for name in os.listdir(parent_folder)
        if os.path.isdir(os.path.join(parent_folder, name))
    ]

    for subfolder in subfolders:
        subfolder_path = os.path.join(parent_folder, subfolder)
        images_to_pdf(subfolder_path, subfolder)


root_path = "/Users/yoma/Downloads/ebooks_screenshots"
save_path = "/Users/yoma/Downloads/ebooks_need_to_resolve"
get_subfolder_names(root_path)
