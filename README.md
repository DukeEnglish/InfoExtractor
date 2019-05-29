
知识图谱自动问答
信息抽取：
1. 文本切分，分词
2. 词性标注，标注词性
3. 命名实体识别，找出实体
4. 关系识别，生成多个形如(entity1,relation,entity2)的tuple。最后两步骤可以一起做


依赖安装：
1、pyltp
2、hanziconv
3、python-goose


https://blog.csdn.net/u013709270/article/details/78944538
NLTK
https://blog.csdn.net/cangqiong112758/article/details/50791468
https://github.com/tim5go/zhopenie
https://github.com/crownpku/Information-Extraction-Chinese

任务流程：
1. 对query进行解析，获取实体以及关系【分词、tagging、ner。主要是利用知识库中的数据进行后处理】- 技术：信息抽取
2. 将解析获取到的实体和关系对应到知识库中的对应的SPO实体上 【利用开源近义词、同义词等建立字典，或者利用词向量进行判断】
3. 利用解析获取到的实体进行soarkql语句构建，利用gStore进行查询
4. 评估解析出来的结果的效果【precision、recall、f1】
5. 根据评估结果improve

pipeline: query - analysis - > SPO - construct - > sparkql - search gStore- > res - eval - > query 

代码运行方法：
1. 将数据放在data里面
2. 运行main.py 
3. 挑选模块进行优化，一个人优化一个模块吧。如果整个框架有问题，也可以进行修改，使用github进行协作。

任务：
1. 梳理一个任务pipeline。写成一个readme，并完成一个bash/main file
2. 梳理出各个任务节点，即可能存在的bottleneck
3. 列出各个节点中需要用到的技术
4. 使用几个例子来详细的解释SPO的抽取以及利用SPO来进行SPARKQL语句的构建，并利用gStore进行查询。


reference
https://github.com/pkumod/gStore/blob/master/docs/API.md
