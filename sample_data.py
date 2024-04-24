import random
from collections import defaultdict

def read_file(filename):
    data = defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            data["relation"].append(line)
    return data

def sample_data(data, num):
    sampled_data = []
    for relation in data:
        if len(data["relation"]) > num:
            sampled_data.extend(random.sample(data["relation"], num))
        else:
            sampled_data.extend(data["relation"])
    return sampled_data

def write_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in data:
            file.write(line)

def main():
    for filename, num in [('train_wiki.txt', 20000), ('val_wiki.txt', 11200), ('test.txt', 2500)]:
        data = read_file(filename)
        sampled_data = sample_data(data, num)
        new_filename = filename.replace('.txt', '_sample.txt')
        write_file(new_filename, sampled_data)
if __name__ == "__main__":
    main()