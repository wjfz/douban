from concurrent import futures
import time
import grpc
from pb import request_pb2, request_pb2_grpc
import douban
import requests
from bs4 import BeautifulSoup


class Greeter(request_pb2_grpc.GreeterServicer):

    req = requests.Session()

    def GetBookInfo(self, request, context):
        headers = {
            'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }

        response = self.req.get(
            url='http://douban.com/isbn/%s' % request.isbn, headers=headers, timeout=2, allow_redirects=True)

        soup = BeautifulSoup(response.text.replace('--!>', '-->'), 'lxml')

        db = douban.DouBan(soup)

        return request_pb2.GetBookInfoResp(
            info=db.Info(),
            brief_introduction=db.Content(),
            about_author=db.Author(),
            directory=db.CataLog(),
            tags=db.Tags(),
            where_to_buy=db.WhereToBuy(),
            recommend=db.Like(),
            read=db.Read(),
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    request_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:10086')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
