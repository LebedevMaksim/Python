import requests


URL = 'http://wttr.in/'


def print_response_headers(response_):
    for key, value in response_.headers.items():
        print(key, ': ', value, sep='')


def file_download(path_download, path_to_save):
    file = requests.get(path_download, stream=True)

    file.raise_for_status()

    # The path and file name in 'path_to_save'
    with open(path_to_save, 'wb') as fd:
        for chunk in file.iter_content(chunk_size=50000):
            print('Received a Chunk')

            fd.write(chunk)


def main():
    try:
        response = requests.get(URL)
    except ConnectionError:
        print('<ConnectionError>')
    else:
        # print_response_headers(response)
        print(response, response.elapsed, response.url, sep='\n')

    # file_download('https://www.1zoom.ru/big2/564/312369-Lastochka.jpg', 'Lastochka.jpg')


if __name__ == "__main__":
    main()
