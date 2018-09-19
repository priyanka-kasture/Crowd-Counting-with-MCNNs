'''
Crowd-Counting using Multi-Column Convolutional Neural Networks.
'''

from network import MCNN
#import sys
                
'''
# For accepting the input from the prompt.
if len(sys.argv) == 2:
    dataset = sys.argv[1]
else:
    print('Usage: python3 test.py A(or B)')
    exit()
'''

dataset='A'    

'''
# For the B dataset.
dataset = 'B'
'''                        
mcnn = MCNN(dataset)

# For predicting the count of people in one Image.
mcnn.predict()

'''
# For predicting the count of people in all Images in the Test Dataset.
mcnn.test()
'''