import numpy as np
from hmmlearn import hmm
from util import load_data,load_test

sequences = load_data()
test_seqs,labels = load_test()
print(sequences)
print(test_seqs)
Mtran = np.array([[0.5, 0.5]
                  [0.5, 0.5]])