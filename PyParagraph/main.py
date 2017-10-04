import os
import re

#run this for files ending in _1 and _2 and _3

for suffix in range(1,4):
    file_name = "paragraph_" + str(suffix) + ".txt"
    #print(file_name)

    filename = os.path.join('../Resources',file_name)

    # open the file and read it
    with open(filename, 'r') as text:

        paragraph = text.read()

        print("Paragraph Analysis of " + filename)
        print("----------------------------------------------------")

        #words are separated by spaces; count the spaces and add 1 for the first word
        word_count = paragraph.count(" ") + 1
        print("Approximate Word Count: " + str(word_count))

        #sentences end with . or ? or !
        sentence_count = paragraph.count('.') + paragraph.count('?') + paragraph.count('!')
        print("Approximate Sentence Count: " + str(sentence_count))

        #divide into sentences so can count words in each sentence
        avg_sentence_length = 0

        #split the paragraph into a list of words
        new_para = paragraph.split()

        #loop through new_para and count number of letters for each word
        num_words = 0
        word_len = 0
        for word in new_para:
            num_words = num_words + 1
            word_len = word_len + len(word)
        #compute average word length
        avg_word_length = round(word_len / num_words,2)
        print("Average Word Length (aka Letter Count): "+ str(avg_word_length))


        avg_sentence_length = round(num_words / sentence_count,2)
        print ("Average Sentence Length: "+ str(avg_sentence_length)+ "\n")

    #write to output file
    output_file = os.path.join('../Resources', 'Paragraph_Analysis_' + str(suffix) + ".txt")
    with open(output_file, 'w') as textfile:

        textfile.write("Paragraph Analysis\n")
        textfile.write("---------------------------------------------\n")
        textfile.write("Approximate Word Count: " + str(word_count)+"\n")
        textfile.write("Approximate Sentence Count: " + str(sentence_count)+"\n")
        textfile.write("Average Word Length (aka Letter Count): " + str(avg_word_length)+"\n")
        textfile.write("Average Sentence Length: " + str(avg_sentence_length) + "\n")


