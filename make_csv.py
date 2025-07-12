import os
import csv

root_path = "/Users/yoma/Downloads/resolved_ebooks"
start_id = 1500


def export_filenames_to_csv(folder_path, output_csv_path):
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # writer.writerow(['id', 'raw_name'])
        writer.writerow(['raw_name', 'is_done', 'is_korean', 'first_check'])

        for i, f in enumerate(files):
            name_without_ext = os.path.splitext(f)[0]
            # writer.writerow([start_id + i, name_without_ext])
            writer.writerow([name_without_ext, False, False, False])

    print(f"CSV 저장 완료: {output_csv_path}")


export_filenames_to_csv(root_path, './new_ebooks.csv')
