from doc import Document

def clean_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') s infile, open(optput_file, 'w', encoding='utf-8')a output_file
    unique_words = set()

    for line in infile:
       removing_eng = line.strip()

        if not removing_eng:
            continue

        removing_eng = re.subr'[A-Za-z]+', '',removing_eng

        if removing_eng not in unique_words:
            unique_words.add(removing_eng)
            outputfile.write(removing_eng + '/n')

if name == "_only dzongkha_":
    input_file = 'dictionary.txt.txt'
    output_file = 'dzongkha_dic.txt'

    removing_eng(input_file, output_file)
    print(f"only dzongkha txt. {output_file}")
