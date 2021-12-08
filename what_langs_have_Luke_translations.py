#how to make list_of_all_files_in_the_corpus.txt:
# cd /Users/apanova/Downloads/corpus
# ls > /Users/apanova/OneDrive/Documents/Continuative/Continuative_Bibles/list_of_all_files_in_the_corpus.txt

import re

def get_full_list ():
    path = '/Users/apanova/OneDrive/Documents/Continuative/Continuative_Bibles/list_of_all_files_in_the_corpus.txt'
    f = open (path, 'r', encoding = 'utf-8')
    full_list = f.read()
    f.close ()
    return (full_list)


def get_sample_list ():
    path = 'iso_codes_from_my_database.txt'
    f = open (path, 'r', encoding = 'utf-8')
    iso_codes = f.readlines()
    iso_codes = [x.strip() for x in iso_codes] 
    f.close ()
    return (iso_codes)


def searching (full_list, iso_codes):
    bibles = []
    for x in iso_codes:
        regexp = '('+x+'-x-bible.*?\.txt)'
        res = re.findall (regexp, full_list)
        if res:
            for file in res:
                bibles.append (file)

    return bibles

def search_for_concrete_lines (bibles):
    bibles_ok = {}
    for bible in bibles:
        path = '/Users/apanova/Downloads/corpus/%s' % bible
        f = open (path, 'r', encoding = 'utf-8')
        bible_file = f.read()
        f.close ()
        regexp = '(42001001\t.*?)\n' # first line of the Gospel of Luke
        res = re.search (regexp, bible_file)
        if res:
            first_line = res.group(1)
            bibles_ok[bible] = first_line

    return bibles_ok

def main ():
    full_list = get_full_list ()
    iso_codes = get_sample_list ()
    bibles = searching (full_list, iso_codes)
    bibles_ok = search_for_concrete_lines (bibles)
    for key, value in bibles_ok.items() :
        print (key)


if __name__ == '__main__':
    main ()
