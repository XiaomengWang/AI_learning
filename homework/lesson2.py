#1.实现一周的记账功能
l_income = []
l_cost = []
d_balance = dict()
end_balance = 0
for i in range(7):
    income = float(input("请输入第%d天的收入：" %(i+1)))
    l_income.append(income)
    cost = float(input("请输入第%d天的支出：" %(i+1)))
    l_cost.append(cost)
    d_balance[i+1] = l_income[i] - l_cost[i]
    end_balance +=  d_balance[i+1]
print("7天的收入分别是：")
for i in l_income:
    print(i)
print("7天的支出分别是：")
for i in l_cost:
      print(i)
for i in range(1,8):
      print("第%d天的结余为：%.2f" %(i,d_balance[i]))
print("最终的结余为：%.2f" %end_balance) #最终的结余

# 2.实现ATM机器
choice_info = """
===========
请选择操作
1. 查询余额
2. 存款
3. 取款
4. 退出
===========
"""
balance = 0
choice = input(choice_info)
while (1):
    if choice == '1':
        print("当前余额为：%d" %balance)
        choice = input(choice_info)
        
    elif choice == '2':
        add = int(input("请输入要存款的金额："))
        balance += add
        print("存款成功，存款金额为：%d，当前余额为：%d" %(add,balance))
        choice = input(choice_info)

    elif choice == '3':
        out = int(input("请输入要取款的金额："))
        if out > balance:
            print("余额不足，取款失败！当前余额为：%d" %balance)
            choice = input(choice_info)
        else :
            balance -= out
            print("取款成功，取款金额为：%d，当前余额为：%d" %(out,balance))
            choice = input(choice_info)

    elif choice =='4':
        print("退出成功")
        break
    else:
        print("选择错误，请重新选择")
        choice = input(choice_info)
        
#3. 词汇表生成及统计
text = """2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个 阅兵 方阵 ， 580 台受 阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 的 检阅 。 阅兵 装备 方队 展示 的 武器装备 皆 为 国产 现役 主战 装备 ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲 际 弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 17 高超音速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的 形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度 公开 亮相 的 武器装备 ， 这 三款 武 器 多年 来 传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予 特殊 的 期待 ， 这 三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 特约 相关 领域 军事 专 家 ， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。"""
vocab = []
word2id = dict()
id2word = dict()
index = 0
for i in range(len(text)):
    if text[i] == " ":
        if text[i-1] != "。" and text[i-1] != "，" and text[i-1] != "\"":
            vocab.append(text[index:i])
            index = i+1
        else:
            index = i + 1
    else:
        pass
vocab = list(set(vocab))
print(vocab)
for i in range(len(vocab)):
    word2id[vocab[i]] = i
    id2word[i]=vocab[i]
print(aa)
print(word2id)
print(id2word)
