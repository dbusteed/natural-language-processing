For this assignment, I decided to explore phonology by using Python and NLTK. I read through section 2.4.2 in the NLTK book, and wrote a Python script called [phon_tool.py](phon_tool.py) that applies some of the things I learned about phonology.

My Python script 
    1) uses the CMUDict to phonemicize words and sentences into ARPABET
    2) produces a list of words that rhyme with a given word

As for inputs and outputs, the script has two modes. First, it can act as an interactive CLI, where the user can choose to lookup phonemes or rhymes for a given word, until they decide to quit (see [one.png](one.png)) Second, the user can call the script from the command line, and provide the necessary parameters (see [two.png](two.png)). This option is important because it allows the script to be used with other programs. For example, the script can read an external input file, process it, then write out the results to an output file (see [three.png](three.png)).

I think the script works pretty well. This is my first time using the CMUDict, and it seems to be extremely accurate and comprehensive. As for the rhyming feature of the script, it also seems to work pretty well. In the script, I define a RIME_FACTOR, which is esentially how many of the ending phonemes must match for words to be considered a rhyme. I originally set this at 2, but found that I wouldn't consider most of the results true rhymes. I changed it to 3, and felt that it gave better results. 