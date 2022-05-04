import requests


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(url, headers=headers, params=params)
        upload_link = response.json().get('href')
        work = requests.put(upload_link, data=open('test.txt', 'r'), params=params, headers=headers)
        return work


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/test.txt'
    my_token = 'AQAAAAAJ2bXkAADLW5INLqBOyUuEuFH8gSu4M3k'
    uploader = YaUploader(my_token)
    result = uploader.upload(path_to_file)
