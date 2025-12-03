# 在这个文件里编写代码
import random

# 定义选手类（可扩展技术参数，比如进攻胜率、防守胜率）
class Player:
    def __init__(self, name, attack_rate=0.5, defend_rate=0.5):
        self.name = name
        self.attack_rate = attack_rate  # 进攻得分概率
        self.defend_rate = defend_rate  # 防守得分概率

# 模拟单局比赛
def simulate_set(player1, player2):
    score1, score2 = 0, 0
    server = player1  # 初始发球方
    while True:
        # 模拟回合得分（简化版：按进攻胜率随机判定）
        if random.random() < player1.attack_rate:
            score1 += 1
        else:
            score2 += 1
        # 发球轮换规则
        if (score1 + score2) % 2 == 0 and not (score1 >=10 and score2 >=10):
            server = player2 if server == player1 else player1
        elif score1 >=10 and score2 >=10 and (score1 + score2) % 1 == 0:
            server = player2 if server == player1 else player1
        # 单局胜负判定
        if (score1 >=11 or score2 >=11) and abs(score1 - score2) >=2:
            return 1 if score1 > score2 else 0

# 模拟整场比赛（5局3胜为例）
def simulate_match(player1, player2, set_num=5):
    win1, win2 = 0, 0
    for _ in range(set_num):
        set_winner = simulate_set(player1, player2)
        if set_winner == 1:
            win1 += 1
        else:
            win2 += 1
        # 先赢3局则结束比赛
        if win1 == 3 or win2 == 3:
            break
    return 1 if win1 > win2 else 0

# 示例：创建两名选手并模拟100场比赛，统计胜率
if __name__ == "__main__":
    p1 = Player("选手A", attack_rate=0.55)
    p2 = Player("选手B", attack_rate=0.45)
    p1_win = 0
    total_matches = 100
    for _ in range(total_matches):
        if simulate_match(p1, p2) == 1:
            p1_win += 1
    print(f"选手A胜率：{p1_win/total_matches:.2f}")
