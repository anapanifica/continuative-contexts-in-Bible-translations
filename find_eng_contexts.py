import re

def get_list_of_contexts ():
    path = 'full_list_of_contexts.txt'
    f = open (path, 'r', encoding = 'utf-8')
    full_list_of_contexts = f.readlines()
    f.close ()
    return (full_list_of_contexts)


def find_lines (full_list_of_contexts):
    result = {}
    path = '/Users/apanova/Downloads/corpus/eng-x-bible-newworld2013.txt'
    f = open (path, 'r', encoding = 'utf-8')
    bible_file = f.read()
    f.close ()
    for context in full_list_of_contexts:
        context = context.strip("\n")
        regexp = '%s\t(.*?)\n' % context
        res = re.search (regexp, bible_file)
        if res:
            line = res.group(1)
            result[context] = line
        else:
            print(context)
    return result


def main():
    full_list_of_contexts = get_list_of_contexts ()
    result = find_lines (full_list_of_contexts)
    result_file = ""
    for x in result:
        result_file = result_file + x + "\t" + result[x] + "\n"
    print(result_file)
    
if __name__ == '__main__':
    main()
