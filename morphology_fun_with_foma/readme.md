I tried using a couple of morphological engines, but was only successful with Foma. I installed it on my Windows machine as well as my Linux VM. It took me a while to understand how to work with the Foma stack (for example, you can only work with the FSM that is on top of the stack), but after that I thought it was pretty easy to use.

Following the example at [fomafst.github.io/morphtut.html](fomafst.github.io/morphtut.html), I made a `.lexc` file to define a lexicon of ~30 Japanese verbs and adjectives. Then in a `.foma` file, I defined some rules that can change these verbs/adjectives into their respective -Te and -Ta forms (-Te form is used when combining verbs; -Ta form is generally used for the past tense). The `.foma` file reads from the `.lexc` file to define the Lexicon, then joins this FSM with the transformation rules. 

One rule was defined as such:

	def TaMu む "^" T A -> んだ || _ .#. ;

If a verb like よむ was inputed with the "Multichar_Symbols" for verb and past-tense (よむ+V+TA), the result would be よむ^TA. After which, the rule shown above would be applied, so that む^TA is subsituted with the correct past-tense ending, んだ. I attached both the `.foma` and `.lexc` file that contain all the rules I developed, as well as the FSM produced by Foma with the "view" command.

I tested my FSM for quite some time, mainly because I found it really interesting. For the most part it works pretty well. Obviously, this tool doesn't cover every Japanese verb and adjective, which is quite limiting if it were to be used in a real scenario. Also, my FSM doesn't correctly handle irregular verbs (for example, はしる+V+TE would incorrectly be transformed to はして instead of はしって). Aside from that I think it works pretty well. See [example.png](example.png) for the Foma rules in action, and [fsm.png](fsm.png) for the final FSM.