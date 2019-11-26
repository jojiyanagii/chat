with open('trans.txt') as open_file:
    all_data = open_file.read()

line_list = all_data.splitlines()

bot_dict = {}

for line in line_list:
    orig,trans = line.split(':')
    bot_dict[orig] = trans

print(bot_dict)

while True:
    command = input('bot&gt; ')
    
    responce = ""
    
    for key in bot_dict:
        if key in command:
            responce = bot_dict[key]
            break
    
    if not responce:
        responce = 'ナニヲイッテイルノデスカ...'
    
    print(responce)
    
    if 'ばいばい' in command:
        break
