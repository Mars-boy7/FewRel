"data_refine.py"
# 用途
    将3个文件汇总在一起，并且进行7：2：1抽样，并最终保存三个抽样后的数据

"sum_data2sample.py"
# 用途
    将三个文件汇总为一个文件，并保存

"data_transform.py"
# 说明
    将fewrel数据集的json文件，根据pid2name.json进行格式变化，最后存为txt

"generate_temp_rel2id.py"
# 说明
    根据"data_transform.py"得到的txt文件，生成temp.txt以及rel2id.json文件，其中rel2temp.json文件用于修改描述的动宾词，详情请看rel2temp.json

"sample_data.py"
# 说明
    用来抽取数据的代码模块，已被"sum_data2sample.py"优化，建议弃用