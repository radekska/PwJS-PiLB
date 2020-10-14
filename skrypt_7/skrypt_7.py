import os

def words_removal(words_to_remove, original_path, new_path):
    
    original_abs_path = os.path.abspath(original_path)
    new_abs_path = os.path.abspath(new_path)

    file_names = os.listdir(original_abs_path)
    if '.DS_Store' in file_names:
        file_names.remove('.DS_Store')

    abs_file_path_list = [os.path.join(original_abs_path,file_path) for file_path in file_names]

    for file_path, file_name in zip(abs_file_path_list, file_names):
        new_read_lines = list()
        save_path = os.path.join(new_abs_path, 'new_{file_name}.txt'.format(file_name=file_name))
        
        with open(file_path, 'r', encoding='utf-8', errors='ignore' ) as file_stream:    
            read_lines = file_stream.read()
            read_lines = read_lines.split(' ')

            for word in read_lines:
                word = word.lstrip().rstrip()
                if word not in words_to_remove:
                    new_read_lines.append(word)

            new_read_lines = ' '.join(new_read_lines)


        with open(save_path, 'x') as output_stream:
            output_stream.write(new_read_lines)




if __name__ == '__main__':
    words_to_remove = ['itself', 'and', 'also', 'never', 'why']

    original_path = 'skrypt_7/pliki_tekstowe/oryginalne'
    new_path = 'skrypt_7/pliki_tekstowe/nowe'

    words_removal(words_to_remove, original_path, new_path)

