For this assignment, I decided to use PyTorch. 

On the PyTorch documentation, there is an unfinished neural network, in which readers can use what they've learned in previous PyTorch examples to finish the network and get it running. I used this as my "boilerplate", and I was able to gain a much clearer understanding of PyTorch and neural networks. I made a Continuous Bag of Words (CBOW) model in which a word is predicted from four surrounding words (2 before and 2 after). I think this model could have practical applications in handwriting resolution, in which a certain word is illegible or missing, and needs to be infered by its surrounding words.

I used the first 100 lines from the Reuters corpus that comes with NLTK. The model structure, which is defined in the `__init__()` method, is characterized by its embeddings and two layers. The first of which has "n" nodes, which is defined during instantiation (I used 40). This layer then translates its outputs to the 2nd layer, which has 300 nodes. The 2nd layer transforms the output from the 300 nodes into "vs" nodes, where "vs" is the vocab size. The "forward" function is how outputs are actually generated. It calculates the embeddings, runs it through the nodes, then returns the output. 

After an hour of re-reading documentation and debugging, I finally got my network to work. But...it took me another hour to find out how to make predictions. The examples online would only calculate loss, and the outputs didn't make sense to me at first. I finally figured out that the resulting vector wasn't an embedding for the predicted word, but was a representation of which words were most likely. For example, the vector `[12.123, 0, 0]` would correspond to a word list `['tree','dog','bird']`. Because the `vector[0]` had the highest number, the model was predicting the word "tree". Knowing this, I wrote a function that made this easier, and played around with some different predictions (see [prediction_1.png](prediction_1.png) and [prediction_2.png](prediction_2.png)).

At this point, I tried playing around with the neural network structure. I tried the following configurations:
1. "n" -> linear -> vocab_size
2. "n" -> linear -> 100 -> linear -> vocab_size
3. "n" -> linear -> 300 -> linear -> vocab_size
4. "n" -> linear -> 200 -> linear -> 100 -> vocab_size

For each network, I record the total loss score and plotted it with Excel (see [loss_comparison.png](loss_comparison.png)). Config #3 appeared to be best. These loss numbers don't give a good way to evaluate the model in general, but is only good for comparing it to itself. That said, I think the model prefomed very well given that it was only trained on a ~100 sentences. 

I also gained an appreciation for the "tensor" data type in which many of these frameworks are based on. I tried to replicate my PyTorch neural net using the Sci-Kit Learn module, but I spent too much time fighting with native Python lists, so I decided to stick with PyTorch.