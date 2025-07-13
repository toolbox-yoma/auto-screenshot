import os
import unicodedata
import subprocess


# target_path = "/Users/yoma/Library/Mobile Documents/com~apple~CloudDocs/Extended Mind/4. Akashic Records/Study/IT"

target_path = "/Users/yoma/Downloads/ebooks_resolved"
save_path = "/Users/yoma/Downloads/ebooks_cover"
done_file = os.path.join(save_path, "-done.txt")
done_list = []
dup_check_list = []

if os.path.isfile(done_file):
    with open(done_file, 'r', encoding='utf-8') as f:
        for line in f:
            done_list.append(line.strip())


def append_line_to_file(file_path: str, line: str):
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(line + '\n')


def check_file_exist(path):
    if os.path.isfile(path):
        return True
    return False


def list_all_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)
                if not check_file_exist(os.path.join(save_path, file[:-4] + ".png")):
                    generate_pdf_thumbnail(full_path, save_path)
                    # append_line_to_file(done_file, file[:-4])
                if file in dup_check_list:
                    print(f"dup - {file}")

            dup_check_list.append(file)


def generate_pdf_thumbnail(file_path, output_folder):
    file_path = os.path.expanduser(file_path)
    output_folder = os.path.expanduser(output_folder)

    try:
        subprocess.run([
            "qlmanage",
            "-t",
            "-s", "1080",
            "-o", output_folder,
            file_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ 썸네일 생성 실패: {file_path}\n{e}")


list_all_files(target_path)
# niddle = "혼자 공부하는"
# normalized_niddle = unicodedata.normalize('NFC', niddle)
# for f in files:
# if niddle in unicodedata.normalize('NFC', f):
#     print(f)
# print(f)
