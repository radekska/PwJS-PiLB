import os

def words_replacing(replacers, original_path, new_path):
    
    original_abs_path = os.path.abspath(original_path)
    new_abs_path = os.path.abspath(new_path)

    file_names = os.listdir(original_abs_path)

    if '.DS_Store' in file_names:
        file_names.remove('.DS_Store')

    abs_file_path_list = [os.path.join(original_abs_path,file_path) for file_path in file_names]

    for file_path, file_name in zip(abs_file_path_list, file_names):
        save_path = os.path.join(new_abs_path, 'new_{file_name}.txt'.format(file_name=file_name))
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore' ) as file_stream:    
            new_read_lines = list()
            read_lines = file_stream.read()
            read_lines = read_lines.split(' ')

            for word in read_lines:
                word = word.lstrip().rstrip()
                if word in replacers.keys():
                    word = word.replace(word, replacers.get(word))
                
                new_read_lines.append(word)

            new_read_lines = ' '.join(new_read_lines)


        with open(save_path, 'x') as output_stream:
            output_stream.write(new_read_lines)


if __name__ == '__main__':
    replacers = {
        'and':'also',
        'also':'and',
        'never':'almost never',
        'why':'cause'
    }

    original_path = 'tekst/podmienianie_slow/pliki_tekstowe/oryginalne'
    new_path = 'tekst/podmienianie_slow/pliki_tekstowe/nowe'

    words_replacing(replacers , original_path, new_path)