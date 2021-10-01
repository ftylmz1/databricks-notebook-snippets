def delete_subfolder(path):
  file_list = dbutils.fs.ls(path)

  for f in file_list:
    dbutils.fs.rm(f.path, True)


def print_recursive(path):
  file_list = dbutils.fs.ls(path)

  if file_list[0].path == path:
    f = file_list[0]
    print(f'{f.path} - {f.name} - {f.size}')
  else:
    for f in file_list:
      print_recursive(f.path)

      
def get_full_path_recursively(path, list_files: list):
  file_list = dbutils.fs.ls(path)

  if file_list[0].path == path:
    f = file_list[0]
    list_files.insert(0, f.path)
  else:
    for f in file_list:
      get_full_path_recursively(f.path, list_files)
      
