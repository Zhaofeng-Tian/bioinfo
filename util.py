import numpy as np

def load_test():
    # Define the file path
    file_path = "hw2_test.data"

    # Load the file into a list of strings
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Remove the ">" character and identifier from each line
    lines = [line.strip()[1:] for line in lines if line.startswith(">") == False]
    sequences = np.array([list(line) for line in lines])  
    seq = []
    labels = []
    for i in range(len(sequences)):
        if i%2==0:
            seq.append(sequences[i])
        else:
            labels.append(sequences[i])
    seq = np.array(seq)
    labels = np.array(labels)

    return seq, labels

def load_data():
    # Define the file path
    file_path = "hw2_train_unlabelled.data"

    # Load the file into a list of strings
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Remove the ">" character and identifier from each line
    lines = [line.strip()[1:] for line in lines if line.startswith(">") == False]
    sequences = np.array([list(line) for line in lines])  
    return sequences 
    
test_seq, labels = load_test()
print(test_seq)
print(labels)


# sequences = np.concatenate(sequences)
# print(len(sequences),' ==>', sequences)
# for i in range(len(sequences)):
#     for j in range(len(sequences[i])):
#         if sequences[i][j] == 'A':
#             # print("=A!!")
#             sequences[i][j] = 0
#         elif sequences[i][j] == 'T':
#             sequences[i][j] = 1
#         elif sequences[i][j] == 'C':
#             sequences[i][j] = 2
#         elif sequences[i][j] == 'G':
#             sequences[i][j] = 3
# print(sequences.astype(np.int16))
# states = ['+','-']
# n_states = 2
# obs = ['A','T','C','G']
# n = 4
# model = hmm.CategoricalHMM(n_components=n_states,algorithm='viterbi',n_iter=2000,tol=0.01)
# X = sequences.astype(np.int16)
# # X = np.concatenate(X)

# model.fit(X)
# print (model.startprob_)
# print (model.transmat_)
# print (model.emissionprob_)
# print (model.score(X))