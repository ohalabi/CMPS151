
def get_word_dict (line_list):
    word_dict = {}
    count = 0
    for e in line_list:
        words = e.split(' ')
        for w in words:
            if w in word_dict:
                word_dict[w].add(count + 1)
            else:
                word_dict[w] = set([count + 1])
        count += 1 #

def main():
    with open ('Kennedy.txt', 'r') as inputfile:
        line_list = inputfile.readlines()
        
    for i in range(len(line_list)):
        line_list[i] =line_list[i].rstrip('\n')
    
    word_dict = get_word_dict (line_list)
    write_index_file (word_dict)
    
main()
        
    
    