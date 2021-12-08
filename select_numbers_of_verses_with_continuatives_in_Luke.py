import os


def choose_lines (bible_list):
    result = ""
    for bible in bible_list:
        bible = bible.strip("\n")
        result = result + bible.split(".")[0] + "\t"
        #print(bible)
        path = 'results/%s' % bible
        f = open (path, 'r', encoding = 'utf-8')
        lines = f.readlines()
        f.close ()
        for line in lines:
            line = line.strip ("\n")
            line_parts = line.split(":")
            if int(line_parts[0]) >= 42001001 and int(line_parts[0]) <= 42024053:
                if line_parts[1] == "1":
                    result = result + line_parts[0] + ", "
        result = result + "\n"
    return result



def main():
    f = open ("/Users/apanova/OneDrive/Documents/Continuative/Continuative_Bibles/list_of_files.txt", 'r', encoding = 'utf-8')
    bible_list = f.readlines()
    f.close ()
    result = choose_lines(bible_list)
    path = '/Users/apanova/OneDrive/Documents/Continuative/Continuative_Bibles/contexts_with_continuatives.csv'
    f = open (path, 'w', encoding = 'utf-8')
    f.write (result)
    f.close
    
if __name__ == '__main__':
    main()
