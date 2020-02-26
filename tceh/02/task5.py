path_str = '/bin:/usr/bin:/usr/local/bin'
path_list = path_str.split(':')

for item in path_list:
    print(item)