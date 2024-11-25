# Programming Exercise 9-3

# Part 2

# Encryption and decryption are inverse of one another
CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
        'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
        'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
        'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
        'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
        'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
        'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
        'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
        'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
        '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
        '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
        '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
        ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
        "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
        '{':'[','[':'{','}':']',']':'}'}

def main():
    # Obtain a string of converted text.
    result = convert()

    # Write converted text to the screen.
    print(result)

# The convert function asks the user for a file name, opens
# the file, and converts its contents using the CODE above.
# It then returns a string of the converted text.
def convert():
    result = ''
    text = ''

    input_name = input('Enter the name of the input file: ')
    with open(input_name, 'r') as input_file:
        text = input_file.read()

    # If character is space, it is not converted;
    # otherwise convert.
    for ch in text:

        if ch.isspace():
            result = result + ch
        else:
            result = result + CODE[ch]

    return result

# Call the main function.
if __name__ == '__main__':
    main()