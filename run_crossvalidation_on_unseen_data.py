from evaluation import *
from util import import_new_data

#move the file with the data you want to run our code on to the same folder as this file
# replace unseendata.txt below with the actual filname
#call python3 run_on_unseen_data.py from teriminal

new_data__file_name = 'unseendata.txt'
new_data = import_new_data(new_data__file_name)



#this call will run the 10-fold crossvalidation without pruning on the data imported
# and print average results at the end
print ('#'*70)
print('10-FOLD CROSSVALIDATION ON THE UNSEEN DATA')
print ('#'*70)
(average_classification_rate,
average_recall,
average_precision,
average_F1,
average_confusion_matrix,
trees) =\
K_fold_evaluation(new_data)
print('Average confusion matrix for unseen data:')
print(np.round(average_confusion_matrix, 0))
print('Average recall per class for unseen data: {}'\
.format(np.round(average_recall, 3)))
print('Average presicion per class for unseen data: {}'\
.format(np.round(average_precision, 3)))
print('Average F1-score per class for unseen data: {}'\
.format(np.round(average_F1, 3)))
print('Average classification rate for unseen data: {}'\
.format(np.round(average_classification_rate, 3)))
