import numpy as np

def entropy(attribute_data):
    _, val_freqs = np.unique(attribute_data, return_counts=True)
    val_probs = val_freqs / len(attribute_data)
    return -val_probs.dot(np.log(val_probs))

def get_count_dict(data):
    data_values, data_freqs = np.unique(data, return_counts=True)
    return dict(zip(data_values, data_freqs))

def info_gain(attribute_data, labels):

    attr_val_counts = get_count_dict(attribute_data)
    total_count = len(labels)
    EA = 0.0
    for attr_val, attr_val_count in attr_val_counts.items():
        EA += attr_val_count * entropy(labels[attribute_data == attr_val])
    return entropy(labels) - EA / total_count