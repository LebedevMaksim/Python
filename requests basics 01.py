""" The script creates a download list of all images found on the web page

"""
import requests


URL = 'http://seasonvar.ru/'


def print_response_headers(response_):
    for key, value in response_.headers.items():
        print(key, ': ', value, sep='')


def file_download(path_download, path_to_save):
    file = requests.get(path_download, stream=True)

    file.raise_for_status()

    # The path and file name in 'path_to_save'
    with open(path_to_save, 'wb') as fd:
        for chunk in file.iter_content(chunk_size=50000):

            fd.write(chunk)


def get_html_tag_list(tag, text):
    tag_list = []
    for i in range(len(text)):
        if text[i] == '<' and text[i + 1: i + 4] == tag:
            j = i + 1
            while text[j] != '>':
                j += 1
            tag_list.append(text[i: j + 1])

    return tag_list


def get_attribute_value(attr, string):
    for i in range(len(string)):
        if string[i] == attr[0]:
            if string[i: i + len(attr)] == attr:
                j = i + len(attr) + 2
                while string[j] != string[i + len(attr) + 1]:
                    j += 1

                return string[i + len(attr) + 2: j]


def check_http_header(text):
    return True if text[0:8] == 'https://' or text[0:7] == 'http://' else False


def main():
    try:
        response = requests.get(URL)
    except ConnectionError:
        print('<ConnectionError>')
    else:
        # print_response_headers(response)
        print(response, response.elapsed, response.url, sep='\n')

        images = get_html_tag_list('img', response.text)
        images_url = []
        for image in images:
            src = get_attribute_value('src', image)
            if check_http_header(src):
                images_url.append(src)

        for url in images_url:
            print(url)

    # file_download('https://www.1zoom.ru/big2/564/312369-Lastochka.jpg', 'Lastochka.jpg')


if __name__ == "__main__":
    main()
