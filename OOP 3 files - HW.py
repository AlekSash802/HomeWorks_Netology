
def text(list_names_files):
  text_files = []
  for file_name in list_names_files:
    with open(file_name) as file:
      lines = file.readlines()
      text_files.append({'name_file': file_name, 'len_file': len(lines), 
                         'lines_file': [line.strip() for line in lines]})
      text_files = sorted(text_files, key=lambda nx: nx.get('len_file'), reverse=True)
  for ix in text_files:
    na_f = ix.get('name_file')
    le_f = ix.get('len_file')
    li_f = ix.get('lines_file')
    # print(na_f, le_f, *li_f, sep='\n')
    with open('text_files.txt', 'a+') as file:
      # print(file.readlines())
      print(na_f, le_f, *li_f, sep='\n', file=file)
      file.flush()
  with open('text_files.txt', encoding='utf-8') as f:
    print(f.read())
  return text_files  # print(*text_files, sep='\n')
  
text(['1.txt', '2.txt', '3.txt'])
