import torch
import torch.nn as nn
import torch.autograd as autograd
import torch.optim as optim
import torch.nn.functional as F
from nltk.corpus import reuters

class CBOW(nn.Module):

    def __init__(self, context_size=2, embedding_size=10, vocab_size=None):
        super(CBOW, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_size)
        self.linear1 = nn.Linear(context_size * embedding_size, 300)
        self.linear2 = nn.Linear(300, vocab_size)

    def forward(self, inputs):
        embeds = self.embeddings(inputs).view((1, -1))
        out = F.relu(self.linear1(embeds))
        out = self.linear2(out)
        return out

def make_context_vector(context, word_to_ix):
    idxs = [word_to_ix[w] for w in context]
    tensor = torch.LongTensor(idxs)
    return autograd.Variable(tensor)

CONTEXT_SIZE = 4
EMBEDDING_SIZE = 10

words = [word.lower() for sent in reuters.sents()[:100] for word in sent if str.isalnum(word)]

vocab = set(words)
vocab_size = len(vocab)

word_to_ix = {word: i for i, word in enumerate(vocab)}
data = []
for i in range(2, len(words) - 2):
    context = [words[i - 2], words[i - 1],
                words[i + 1], words[i + 2]]
    target = words[i]
    data.append((context, target))

losses = []
loss_func = nn.CrossEntropyLoss()
net = CBOW(CONTEXT_SIZE, embedding_size=EMBEDDING_SIZE, vocab_size=vocab_size)
optimizer = optim.SGD(net.parameters(), lr=0.01)

for epoch in range(10):
    total_loss = 0
    for context, target in data:
        
        context_var = make_context_vector(context, word_to_ix)
        
        net.zero_grad()
        
        log_probs = net(context_var)

        loss = loss_func(log_probs, autograd.Variable(
            torch.LongTensor([word_to_ix[target]])
        ))

        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    losses.append(total_loss)

print(losses)

# prediction
ix_to_word = {v:k for k,v in word_to_ix.items()}

def prediction(context):
    n = net(context)

    res = [(i,x) for i,x in enumerate(n[0])]

    for id,_ in sorted(res, key=lambda x: x[1], reverse=True)[:10]:
        print(ix_to_word[id])