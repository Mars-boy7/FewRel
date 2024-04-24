def sum_data2sample(train_paths, val_paths, test_paths, sample_path):
    # Open the sample_path file once for writing to clear any existing data
    with open(sample_path, 'w') as file:
        pass

    for path in [train_paths, val_paths, test_paths]:
        with open(path, 'r') as file:
            data = file.readlines()
            # Open the sample_path file in append mode to add new data
            with open(sample_path, 'a') as file:
                for line in data:
                    file.write(line)

train_paths = './fewrel/train_wiki.txt'
val_paths = './fewrel/val_wiki.txt'
test_paths = './fewrel/test_nyt.txt'
sample_path = './fewrel/sum_alldata.txt'
sum_data2sample(train_paths, val_paths, test_paths, sample_path)
