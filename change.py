with open(‘trans.txt’) as open_file:
    all_data = open_file.read()

# 各行のリストを作る
line_list = all_data.splitlines()

#読み込んだデータを辞書に追加
bot_dict = {}

For line in line_list:
    orig,trans = line.split(‘:’)
    bot_dict[orig] = trans

print(bot_dict)