from urls import is_http_url


# 1 open file in read mode
# 2 read data line by line
# 3 extract url data
File_path = './urls.txt'

file = open(File_path, "r")
lines = file.readlines()



def get_url(line):
    result = []
    for string in line:
        if is_http_url(string):
            result.append(string)
    
    return result



def find_urls(text):
    urls = []
    for line in text:
        splited_line = line.split(" ")
        line_urls = get_url(splited_line)

        urls.extend(line_urls)
    return urls





def main():
    result = find_urls(lines)
    for url in result:
        print(url)


main()