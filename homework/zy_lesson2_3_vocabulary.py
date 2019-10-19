### 作业3：词汇表生成及统计

text = '''2019 年 十月 一日 上午 ， 庆祝 中华人民共和国 成立 70 周年 阅兵式 在 首都北京 盛大举行 ， 59 个
阅兵 方阵 ， 580 台受 阅 装备 ， 1.5 万人 的 参阅 队伍 接受 了 全国 人民 的 检阅 。 阅兵 装备 方队 展示
的 武器装备 皆 为 国产 现役 主战 装备 ， 40% 为 首次 展示 。 其中 近些年来 广受 全球 关注 的 东风 41 洲际
弹道导弹 ， 巨浪 二潜射 弹道导弹 ， 东风 17 高超音速 武器 系统 终于 揭幕 亮剑 ， 以 " 不怒 自威 " 的
形象 向 世界 展示 中国 捍卫 和平 的 意志 与 力量 。 相较 于 其他 首度 公开 亮相 的 武器装备 ， 这 三款
武器 多年 来 传闻 不断 ， 备受 关注 ， 并 因 其 " 大国 基石 " 的 地位 而 被 公众 赋予 特殊 的 期待 ， 这
三款 武器装备 实力 究竟 如何 ， 又 各自 承担 着 怎样 的 历史 " 使命 " 呢 ？ 本报 特约 相关 领域 军事 专家
， 为 大家 详细 解读 这 三款 彰显 国威 ， 震撼 世界 的 国 之 重器 。'''

# 切片及去重
vocab_text = text.split()
vocab_text_overkill = {}
vocab_text_overkill = vocab_text_overkill.fromkeys(vocab_text)

# 词汇列表
vocab = []
wordid = {}
idword = {}

vocab = list(vocab_text_overkill.keys())
    
# 统计
value = 0
for i in vocab:
    wordid[i] = value
    idword[value] = i
    value += 1

print("-"*50)    
print("词汇表", vocab)
print("-"*50) 
print("wordid", wordid)
print("-"*50) 
print("idword", idword)

