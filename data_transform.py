import json

def transform_json_with_relation(json_file_path, output_file_path, relation_file_path):
    # Read the relation file to get the relation values
    with open(relation_file_path, 'r') as file:
        pid2name = json.load(file)

    # Read the input JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Function to transform the record and lookup relation values
    def transform_record(record, pid):
        # Get the first and last position if they are different, otherwise just one position
        h_pos = [record['h'][2][0][0], record['h'][2][-1][-1]] if record['h'][2][0][0] != record['h'][2][-1][-1] else [record['h'][2][0][0]]
        t_pos = [record['t'][2][0][0], record['t'][2][-1][-1]] if record['t'][2][0][0] != record['t'][2][-1][-1] else [record['t'][2][0][0]]

        # Ensure that h and t names are only one word by splitting and taking the first word
        h_name = record['h'][0].split()[0] if record['h'][0] else 'unknown'
        t_name = record['t'][0].split()[0] if record['t'][0] else 'unknown'

        # Get the relation value using the PID
        relation_value = pid2name.get(pid, ["no_relation"])[0]

       # Construct the transformed record
        return {
            'token': record['tokens'],
            'h': {'name': h_name, 'pos': h_pos},
            't': {'name': t_name, 'pos': t_pos},
            'relation': relation_value
        }

    # Open the output file
    with open(output_file_path, 'w') as out_file:
        # Write each transformed record to the file
        for pid, records in data.items():
            for record in records:
                transformed_record = transform_record(record, pid)
                out_file.write(json.dumps(transformed_record) + '\n')

    return output_file_path

# Paths to the input JSON file, the output TXT file, and the relation JSON file
# Make sure to replace these placeholders with the actual file paths when using the script
input_json_path = './val_nyt.json'
output_txt_path = './fewrel/test_nyt.txt'
relation_file_path = './pid2name.json'

# Uncomment the line below and replace the placeholders with your file paths
# transform_json_with_relation(input_json_path, output_txt_path, relation_file_path)
transform_json_with_relation(input_json_path, output_txt_path, relation_file_path)