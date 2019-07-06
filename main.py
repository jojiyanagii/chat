with open('trans.txt') as open_file:
    all_data = open_file.read()

# 各行のリストを作る
line_list = all_data.splitlines()

#読み込んだデータを辞書に追加する
bot_dict = {}

for line in line_list:
    orig,trans = line.split(':')
    bot_dict[orig] = trans

print(bot_dict)

while True:
    command = input('bot&gt; ')
    
    responce = ""
    
    #辞書のキーが含まれているかチェック
    for key in bot_dict:
        if key in command:
            responce = bot_dict[key]
            break
    
    # 空文字の判定
    if not responce:
        responce = 'ナニヲイッテイルノデスカ...'
    
    print(responce)
    
    if 'ばいばい' in command:
        break