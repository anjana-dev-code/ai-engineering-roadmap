import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score


def confusion_matrix_scratch(y_true, y_pred):
    """Returns [[TN, FP], [FN, TP]]."""
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tn = np.sum((y_true == 0) & (y_pred == 0))
    fp = np.sum((y_true == 0) & (y_pred == 1))
    fn = np.sum((y_true == 1) & (y_pred == 0))
    tp = np.sum((y_true == 1) & (y_pred == 1))
    return np.array([[tn, fp], [fn, tp]])


def precision_scratch(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix_scratch(y_true, y_pred).ravel()
    if tp + fp == 0:  # model never predicted 1
        return 0.0
    return tp / (tp + fp)


def recall_scratch(y_true, y_pred):
    tn, fp, fn, tp = confusion_matrix_scratch(y_true, y_pred).ravel()
    if tp + fn == 0:  # no real 1s exist
        return 0.0
    return tp / (tp + fn)


def f1_scratch(y_true, y_pred):
    p = precision_scratch(y_true, y_pred)
    r = recall_scratch(y_true, y_pred)
    if p + r == 0:
        return 0.0
    return 2 * p * r / (p + r)


# Tests: scratch vs sklearn
cases = {
    "normal": ([1,0,1,1,0,0,1,0,1,0,1,1], [1,0,0,1,0,1,1,0,1,0,0,1]),
    "perfect": ([1,0,1,0,1,0], [1,0,1,0,1,0]),
    "never predicts 1": ([1,0,1,0,1,0], [0,0,0,0,0,0]),
}

for name, (yt, yp) in cases.items():
    assert np.array_equal(confusion_matrix_scratch(yt, yp), confusion_matrix(yt, yp))
    assert np.isclose(precision_scratch(yt, yp), precision_score(yt, yp, zero_division=0))
    assert np.isclose(recall_scratch(yt, yp), recall_score(yt, yp, zero_division=0))
    assert np.isclose(f1_scratch(yt, yp), f1_score(yt, yp, zero_division=0))
    print(f"{name}: passed")