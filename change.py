with open(‘trans.txt’) as open_file:
    all_data = open_file.read()
line_list = all_data.splitlines()

bot_dict = {}

For line in line_list:
    orig,trans = line.split(‘:’)
    bot_dict[orig] = trans

print(bot_dict)
