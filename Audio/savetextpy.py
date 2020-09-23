def save_txt(name,data):
    file_name = name + '.txt'
    with open(file_name, mode = 'w', encoding = 'utf-8') as x_file:
        x_file.write(data)


data = "com mèo"
save_txt("demo",data)