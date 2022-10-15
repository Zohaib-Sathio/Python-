from pydictionary import Dictionary

while(True):
    word = input("Enter word here: ")
    if(word.lower() == 'exit'):
        break
    Dic = Dictionary(word)

    antonym = Dic.antonyms()
    synonym = Dic.synonyms()

    Dic.print_antonyms()
    Dic.print_synonyms()
    # Dic.print_meanings()

    # print(antonym)
    # print(synonym)