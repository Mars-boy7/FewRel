import json
import random
from collections import defaultdict

def read_and_merge_files(file_paths):
    merged_data = []
    for path in file_paths:
        with open(path, 'r') as file:
            for line in file:
                record = json.loads(line.strip())
                record_text = record['relation'].split(' ')
                if len(record_text) <4:
                    merged_data.append(record)
    return merged_data

def sample_data(data, ratios):
    # Ensure each relation is represented at least once
    relation_dict = defaultdict(list)
    for record in data:
        relation_dict[record['relation']].append(record)

    sampled_data = [[], [], []]  # Data for each of the three files

    # Add at least one of each relation to the samples
    for relation, records in relation_dict.items():
        if len(records) < 4:
            for i in range(3):
                sampled_data[i].append(records.pop(0))

    # Shuffle the remaining data
    remaining_data = [record for records in relation_dict.values() for record in records]
    random.shuffle(remaining_data)

    # Assign remaining data according to the ratios
    total_length = len(remaining_data)
    lengths = [int(ratio * total_length) for ratio in ratios]

    current_index = 0
    for i in range(3):
        end_index = current_index + lengths[i]
        sampled_data[i].extend(remaining_data[current_index:end_index])
        current_index = end_index

    return sampled_data

def save_samples(samples, output_file_paths):
    for sample, path in zip(samples, output_file_paths):
        with open(path, 'w') as file:
            for record in sample:
                file.write(json.dumps(record) + '\n')

# File paths of the original .txt files
file_paths = ['./train_wiki.txt', './val_wiki.txt', './test_nyt.txt']

# File paths for the sampled output files
output_paths = ['./train5%.json', './val5%.json', './test5%.json']

# Read and merge files
merged_data = read_and_merge_files(file_paths)

# Sample the data
sampled_data = sample_data(merged_data, [0.7*0.05, 0.2*0.05, 0.1*0.05])

# Save the samples
save_samples(sampled_data, output_paths)