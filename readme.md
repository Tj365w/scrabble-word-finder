A simple scrabble word finder written in python.
there are 2 modes, default and manual.
in default/auto mode, just enter the letters and it will find all the possible words which can be made using these letters.
in manual mode the regex entry is required according to which all words will be found,
the words will then be sorted in the order of highest probability of occurance.
whilst calculating probability of occurance of word the number of the letter pieces of a letter in scrabble are considered,
also counter intuitively , the most probable word lenth in english is 7-9 letters,
source :  https://www.reddit.com/r/dataisbeautiful/comments/6jbt4d/a_distribution_of_english_words_by_length_using/
hence the seven letter words have been printed first, 

credits:  
I thank @dwyl on git hub for the proccessed list of words document.
https://github.com/dwyl/english-words     this is the original github repo for the dictionary.

Warning: please for gods sake run this script through the terminal and not on IDLE, it takes eternities to get the work done there.

 
After each search each asks the input for all letters used in the roud,
this accounts for the used up letters and change in probability of the letters.

While entering the used up letters , 'aa' acounts for 2 A(s) used up in the round and henceforth.
