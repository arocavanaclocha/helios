import os

def search_files(folder, endswith=".json"):
  # r=root, d=directories, f = files
  files = []
  print(f'Searching at {folder}.')
  for r, d, f in os.walk(folder):
      for file in f:
          if file.endswith(endswith):
              print("             " + os.path.join(r, file))
              files.append( os.path.join(r, file))
  return files
