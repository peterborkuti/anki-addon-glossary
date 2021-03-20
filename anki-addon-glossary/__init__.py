from anki.lang import _
from anki.hooks import addHook
from anki.exporting import TextCardExporter
from aqt.utils import getText
from aqt.utils import showInfo
from anki.cards import Card
from anki.utils import  ids2str, splitFields
import re
import sys
import os
import time
import random
import string
import json
import subprocess

# only_kanji = "我 没 有 问 题 们 现 在 钱 他 工 作 吗 爸 妈 北 京 房 子 你 手 机 上 海 朋 友 的 老 师 男 都 电 脑 这 个 周 末 时 间 不 车 板 公 也 认 识 明 天 可 以 去 用 要 冰 水 两 爱 和 是 美 国 人 太 吃 肉 喜 欢 中 菜 她 学 生 一 儿 法 想 文 会 饺 孩 喝 酒 来 家 觉 得 好 知 道 很 高 胖 帅 湖 南 辣 种 地 方 漂 亮 昨 冷 今 气 了 ！ 麻 烦 餐 厅 看 书 咖 啡 茶 爷 奶 岁 女 贵 德 语 难 还 热 英 年 半 四 三 苹 果 五 星 期 六 月 婆 十 七 傻 八 坏 外 包 号 日 新 平 安 夜 出 结 婚 兴 二 早 忙 做 什 么 跟 见 面 晚 空 下 吧 班 九 点 午 大 哥 校 司 名 说 东 西 那 呢 怎 弟 雨 走 快 给 香 港 休 息 便 宜 办 室 谁 楼 多 小 狗 本 牛 里 杯 码 百 块 课 叫 李 龙 马 滩 字 洗 超 市 园 哪 旅 行 饭 买 姓 王 张 林 毛 赵 陈 您 打 话 后 回 写 汉 唱 歌 开 游 泳 能 帮 找 到 网 宝 声 告 诉 千 坐 候 玩 进 停 抽 烟 脏 睡 累 铁 芒 啤 哭 为 饿 但 听 米 厕 所 猫 聪 远 非 常 鱼 过 飞 、 少 路 店 住 区 静 因 苦 些 习 火 票 对 影 样 妹 巧 克 力 第 次 线 死 几 件 衣 服 丑 吵 急 哇 蛋 糕 差 词 意 思 纽 约 台 湾 旧 门 口 始 完 父 母 前 轻 城 应 该 忘 每 迟 淘 川 直 业 教 起 已 经 感 冒 需 总 记 干 净 心 特 别 努 淇 淋 堡 请 同 事 送 礼 物 带 护 照 碗 澡 银 更 近 变 比 春 节 秋 闹 调 刚 只 员 句 跑 阿 姨 正 扫 离 等 戏 笑 动 边 音 乐 聊 读 黄 河 长 待 久 重 冬 性 格 化 头 发 舒 葡 萄 味 又 黑 姐 湿 矮 瘦 懂 白 真 讨 厌 站 场 啊 错 资 牌 鲜 汁 甜 画 客 户 穿 最 情 山 风 景 怕 解 颜 色 或 者 披 萨 寿 算 杭 州 苏 视 就 像 笼 衬 衫 接 球 先 分 毕 当 统 务 才 自 己 瓶 胡 萝 卜 花 万 亿 零 刻 桌 从 演 部 套 卖 参 加 篇 章 双 鞋 遍 怀 孕 再 定 谢 纸 夏 姑 娘 红 慢 伤 牙 刷 合 巴 交 云 拼 伞 拿 图 馆 脸 首 闻 奇 怪 关 产 品 理 笨 床 派 议 试 尝 考 虑 论 商 量 旁 放 草 共 担 希 望 然 治 笔 亲 介 绍 叔 消 借 骗 邮 报 糖 内 跳 舞 份 炒 斤 条 盒 叶 支 玫 瑰 短 信 颗 赛 宾 懒 收 病 凉 臭 醉 圣 诞 历 史 运 付 主 极 棒 无 害 紧 让 尴 尬 社 科 技 达 专 全 身 汗 假 熟 相 民 把 邀 眼 睛 圆 清 楚 躺 沙 辛 按 摩 松 健 康 聚 滑 祝 顺 利 通 ： 拥 抱 激 着 垃 圾 扔 实 单 敲 温 医 释 层 低 顾 许 搬 煮 硬 软 盐 咸 淡 输 嫉 妒 优 势 故 钟 复 压 原 型 价 浦 摔 倒 决 拍 受 迎 提 示 邻 居 片 撞 掉 糊 队 丢 疯 惯 私 棋 赢 成 功 靠 鱿 赌 药 鸡 互 助 尊 持 鼓 励 响 流 肯 够 换 恐 终 于 咱 愿 庆 怨 幸 查 度 挺 活 式 隐 蔬 体 如 折 俗 貌 陪 越 检 犯 误 疼 适 爬 刮 亏 保 存 浪 费 被 醒 堵 准 备 求 质 龄 入 胞 胎 兄 器 严 肃 凶 恋 态 版 钥 匙 捐 顿 减 肥 瑜 伽 趣 它 页 较 容 易 虽 满 篮 厉 韩 整 术 姚 皮 猜 简 政 府 注 农 村 展 敏 悔 骑 反 众 策 程 欧 洲 数 级 处 豆 腐 养 喂 表 般 野 食 步 宫 修 之 类 呆 谈 怡 柏 芝 《 》 瓜 菠 夫 广 津 剑 桥 印 组 织 际 附 战 吸 血 鬼 负 责 管 推 艺 架 羽 设 计 联 言 济 环 租 押 金 宠 排 订 胃 另 建 航 幼 供 项 目 遇 省 未 险 投 案 改 树 束 确 任 标 赚 奖 微 引 培 训 判 钢 琴 潜 世 立 革 巨 涨 增 惊 讶 逃 院 驾 退 厨 兼 职 辞 桶 占 销 率 志 裙 灯 戴 镜 嘛 谦 虚 塑 料 袋 ； 熊 搞 歉 奢 侈 饮 纪 录 评 独 俩 筷 导 油 庭 源 贡 献 祈 祷 往 左 拐 偷 货 盛 必 须 境 留 享 界 喊 脾 杂 向 转 招 汇 雷 锋 陌 验 异 况 困 坚 枪 警 察 取 封 讲 撒 谎 观 失 粉 丝 寄 团 锅 使 弄 位 妆 废 闲 系 悉 练 羞 虎 润 降 肚 括 福 育 背 税 扰 创 土 薯 侣 幽 默 酪 脉 危 闭 罪 祸 座 申 泰 （ ） 宽 肩 膀 抠 剪 深 圳 秘 密 狠 签 证 选 递 传 授 赏 熬 段 箱 乞 丐 币 巾 饱 袜 散 随 卧 傅 举 捡 抬 鸟 摸 迷 络 昆 粗 暗 破 腿 仔 裤 华 裔 具 善 义 暴 恶 固 执 骄 傲 命 挤 痛 厚 脱 踩 脚 墙 智 迪 斯 尼 扶 污 染 残 忍 嫁 偏 载 抄 绩 恭 财 纱 追 堆 辆 择 值 拉 刺 暖 灵 精 神 尽 预 乱 赋 继 续 弃 连 股 怜 穷 麦 劳 饼 针 典 编 辑 免 除 其 兔 杰 升 充 而 且 营 倍 规 模 速 损 阳 醋 某 研 究 汤 癌 症 效 寓 缺 潮 薪 控 制 古 卦 莓 灰 給 罚 啦 扮 抓 骂 删 碎 赶 律 泡 泉 将 购 乎 晴 江 浙 账 妞 剩 右 槽 嗨 霉 峰 郁 闷 呀 蓝 绿 田 秀 盘 扩 谊 致 并 糟 脊 竟 谓 避 甚 至 裁 掌 桂 承 酬 限 断 底 脆 既 蕉 碰 强 涉 犹 豫 足 拾 敢 仿 普 弊 吉 祥 季 突 魔 却 融 顶 趟 椅 漠 装 杀 毒 根 划 汽 孤 临 枯 燥 屁 猕 猴 桃 缅 甸 逛 街 吓 耶 素 枝 摇 呼 石 粮 爆 凭 扣 迈 尔 逊 忠 诚 疑 富 慧 胜 辩 官 各 灾 族 切 促 趁 彼 此 妻 配 谅 忽 挑 析 梦 丈 弹 啰 嗦 著 与 代 邓 防 初 积 佳 角 颁 赃 款 归 企 批 丰 材 象 维 由 悲 剧 挫 键 奋 倡 叠 携 惩 莫 布 抗 列 涂 领 仍 勇 冲 败 赞 慈 誉 博 即 尚 光 违 戒 炫 耀 赔 偿 遵 守 估 聘 略 厂 寒 腊 稳 基 础 债 陷 衰 贿 伦 敦 罢 瘫 痪 状 挡 卡 嘴 睁 翻 旦 振 塌 沫 崩 溃 答 允 否 则 迹 据 频 元 译 藏 及 吞 吐 何 乘 逼 宁 屑 揉 膨 胀 旗 仅 构 良 矛 盾 哈 欠 喉 咙 鼻 烧 唠 叨 扬 朝 沈 轿 驶 补 形 念 距 童 符 玻 璃 钻 玉 腻 显 苗 余 称 踢 围 洁 娱 郊 凡 竞 争 剂 佛 漫 慰 透 露"


ext = ".htm"

hideTags = True

def getRandomId(group):
    # https://pythontips.com/2013/07/28/generating-a-random-string/
    return ' id="' + ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])+'"'

def escapeText(text):
    "Escape newlines, tabs and CSS and change id to class"
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("<hr id=answer>", '<hr class="answer">')

    return text

def myEscapeText(s):
    s = re.sub('(?si)^.*<hr id=answer>\n*', "", s)
    s = re.sub("(?si)<style.*?>.*?</style>", "", s)
    s = re.sub(r'\[sound:(.*)]', r'<audio controls src="\1"></audio>', s, 0, re.IGNORECASE)

    return escapeText(s)

class MyTextCardExporter(TextCardExporter):
    key = _("Export deck as My Html Glossary")

    def __init__(self, col):
        TextCardExporter.__init__(self, col)

    def doExport(self, file):
        collection_media = '/home/srghma/.local/share/Anki2/User 1/collection.media'
        child_dir        = 'anki-addon-glossary' # None

        cardIds = self.cardIds()

        cache = list()

        print("exporting")

        for cardId in cardIds:
            card = self.col.getCard(cardId)

            template = card.template()
            template_name = template["name"]

            # if template_name != 'from ierogliph to transl':
            #     # print(f"skipping template {template_name}")
            #     continue

            kanji = card.note()["kanji"]

            # if kanji not in only_kanji:
            #     continue

            dir_full             = "/".join(filter(None, [collection_media, child_dir]))
            file_from_collection = "/".join(filter(None, [child_dir, kanji + '.js']))
            file_full            = "/".join(filter(None, [collection_media, file_from_collection]))

            print(file_full)

            if not os.path.exists(dir_full):
                os.makedirs(dir_full)

            # cache.append(file_from_collection)

            data = { 'kanji': kanji, 'value': myEscapeText(card.answer()) }
            data = '(window.kanjicache=window.kanjicache||[]).push(' + json.dumps(data, sort_keys=True, indent=2 * ' ', ensure_ascii=False) + ')'

            if os.path.exists(file_full):
                old_content = None

                with open(file_full, 'r') as myfile:
                    old_content = myfile.read()

                if old_content == data:
                    print("skipping because not changed")
                    continue

            with open(file_full, 'w') as myfile:
                print(f"writing {kanji}")
                myfile.write(data)

            # file.write("dummy".encode("utf-8"))

        # cache = map(lambda x: "<img src=\"" + x + "\">", cache)
        # cache = "".join(cache)
        # print(cache)

        # zip_path = '/home/srghma/Dropbox/anki-files/anki-addon-glossary.zip'
        # if os.path.exists(zip_path):
        #     os.remove(zip_path)

        # stdout=subprocess.PIPE, stderr=subprocess.PIPE
        # subprocess.run(["env"], cwd=collection_media, check=True)
        # subprocess.run(["/nix/store/nn4mvpxbf6lcynqbji15d6nmkb7p8qg8-zip-3.0/bin/zip", "-r", "--temp-path", "/tmp/", zip_path, "anki-addon-glossary/"], cwd=collection_media, check=True)

def addMyExporter(exps):
    def theid(obj):
        return ("%s (*%s)" % (obj.key, obj.ext), obj)
    exps.append(theid(MyTextCardExporter))

addHook("exportersList", addMyExporter)
