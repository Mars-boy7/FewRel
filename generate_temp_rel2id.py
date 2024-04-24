import json

def generate_files(train_wiki_txt_path, template_output_path, rel2id_output_path, rel2temp_path):
    # 加载 rel2temp 映射
    with open(rel2temp_path, 'r', encoding='utf-8') as file:
        rel2temp = json.load(file)

    unique_relations = set()
    templates = []

    # 读取 train_wiki.txt 文件并处理每一行
    with open(train_wiki_txt_path, 'r', encoding='utf-8') as file:

        for line in file:
            record = json.loads(line)
            relation = record["relation"]
            subject = record["h"]["name"]
            object_ = record["t"]["name"]

            # 从 rel2temp 获取映射值，确保它是字符串
            template_mapping = rel2temp.get(relation, "is associated with")
            if not isinstance(template_mapping, str):
                template_mapping = "is associated with"
            template_phrase = template_mapping.split()

            # 确保短语由三个单词组成
            if len(template_phrase) != 3:
                template_phrase = ["is", "associated", "with"]

            template_str = f"0\t{relation}\t{subject}\t{template_phrase[0]}\t{template_phrase[1]}\t{template_phrase[2]}\t{object_}"
            templates.append(template_str)

            unique_relations.add(relation)

    # 将模板写入 temp.txt 文件
    with open(template_output_path, 'w', encoding='utf-8') as out_file:
        for template in set(templates):  # 使用集合来去除重复项
            out_file.write(template + '\n')

    # 为每个关系分配一个唯一标识符
    rel2id = {rel: idx for idx, rel in enumerate(sorted(unique_relations))}

    # 将 rel2id 映射写入 rel2id.json 文件
    with open(rel2id_output_path, 'w', encoding='utf-8') as out_file:
        json.dump(rel2id, out_file, indent=4)

# 文件路径（请根据实际情况替换）
train_wiki_txt_path = './fewrel/train.txt'  # train_wiki.txt 文件的路径
template_output_path = './fewrel/temp.txt'  # temp.txt 文件的输出路径
rel2id_output_path = './fewrel/rel2id.json'  # rel2id.json 文件的输出路径
rel2temp_path = './fewrel/rel2temp.json'  # rel2temp.json 文件的路径

# 运行函数
generate_files(train_wiki_txt_path, template_output_path, rel2id_output_path, rel2temp_path)
