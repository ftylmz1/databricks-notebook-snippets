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
