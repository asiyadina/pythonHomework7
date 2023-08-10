import os


def rename_files(dir_path: str,
                 new_name: str = '',
                 count: int = 3,
                 in_extension: str = 'txt',
                 out_extension: str = 'txt',
                 slice_name: tuple = (0, 0)):
    if not os.path.isdir(dir_path):
        return False
    file_list = os.listdir(dir_path)
    files_count = 1
    for cur_file in file_list:
        cur_name, cur_ext = cur_file.split('.')
        if cur_ext == in_extension:
            new_file = ''
            if slice_name:
                new_file += f'{cur_name[slice_name[0]:slice_name[1]]}'
            if new_name:
                new_file += f'{new_name}'
            new_file += f'_{files_count:0>{count}}.{out_extension}'
            os.rename(os.path.join(dir_path, cur_file),
                      os.path.join(dir_path, new_file))
            files_count += 1
    return f'{files_count} файл(а/ов) переименован(ы) по шаблону ' \
           f'"old_name[{slice_name[0]}:{slice_name[1]}]{new_name}_{"X" * int(f"{count}")}.{out_extension}"'


print(rename_files('Example_files', new_name='NewSuper', count=5, in_extension='txt',
                   out_extension='doc', slice_name=(5, 30)))