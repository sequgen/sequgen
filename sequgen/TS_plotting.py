import numpy as np
from sklearn import metrics
import matplotlib
from matplotlib import pyplot as plt


def plot_TS(X_ts: np.ndarray, TS_def: dict):
    """ Plot multivariate time series.
    """
    n_ch = X_ts.shape[0]

    cmap = matplotlib.cm.get_cmap('inferno') #'Spectral')
    plt.style.use('ggplot')
    plt.figure(figsize=(10, (1 + 0.7 *n_ch)))
    for i in range(n_ch):
        plt.plot((X_ts[i, :] - i), color=cmap(i / n_ch))

    if 'class_name' in TS_def:
        title = TS_def['class_name']
    else:
        title = 'Generated time series'
    plt.title(title)
    plt.yticks(-np.arange(n_ch), ['channel ' + str(i) for i in range(n_ch)])
    plt.xlabel('time')


def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues,
                          figsize=(8, 8)):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.style.use('ggplot')

    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = metrics.confusion_matrix(y_true, y_pred)
    ## Only use the labels that appear in the data
    #classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.grid(False)

    # Show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()

    return cm
