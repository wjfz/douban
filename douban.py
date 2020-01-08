class DouBan:
    soup = ''

    def __init__(self, soup):
        self.soup = soup

    def Title(self):
        print('-----书名-----:')
        h1 = self.soup.find('h1')
        if h1:
            return h1('span')[0].find(text=True)
        return ''

    def Image(self):
        print('------图片--------:')
        tag = self.soup.find('a', class_='nbg')
        if tag:
            return tag.img['src']
        return ''

    def Score(self):
        print('-----豆瓣评分------:')
        strong = self.soup.find('strong')
        if strong:
            score = strong.find_all(text=True)[0].strip()
            if score != '':
                return score
        return '0'

    def Info(self):
        print('-----基本信息-----:')
        info = {}

        info['title'] = self.Title()
        info['image'] = self.Image()
        info['score'] = self.Score()

        div = self.soup.find(id='info')
        arr = []
        for text in div.find_all(text=True):
            if len(text.strip().strip(':')) != 0:
                arr.append(text.strip().strip(':'))
        mapArr = {}
        for index, item in enumerate(arr):
            mapArr[item] = index

        if '副标题' in mapArr:
            info["sub_title"] = arr[mapArr['副标题'] + 1]
        if 'ISBN' in mapArr:
            info["isbn"] = arr[mapArr['ISBN'] + 1]
        if '译者' in mapArr:
            info["translator"] = arr[mapArr['译者'] + 1]
        if '作者' in mapArr:
            info["author"] = arr[mapArr['作者'] + 1]
        if '原作名' in mapArr:
            info["origin_author"] = arr[mapArr['原作名'] + 1]
        if '出版社' in mapArr:
            info["publisher"] = arr[mapArr['出版社'] + 1]
        if '出版年' in mapArr:
            info["publish_at"] = arr[mapArr['出版年'] + 1]
        if '页数' in mapArr:
            info["page_num"] = arr[mapArr['页数'] + 1]
        if '定价' in mapArr:
            info["price"] = arr[mapArr['定价'] + 1]
        if '装帧' in mapArr:
            info["binding"] = arr[mapArr['装帧'] + 1]
        if '出品方' in mapArr:
            info["producer"] = arr[mapArr['出品方'] + 1]
        if '丛书' in mapArr:
            info["series"] = arr[mapArr['丛书'] + 1]

        return info

    def Content(self):
        print('-----类容简介-----:')
        div = self.soup.find(id='link-report', class_='indent')
        if div:
            return "</br>".join([text.get_text().strip() for text in div('p')])
        return ""

    def Author(self):
        print('-----作者简介-----:')

        span = self.soup.find('span', string='作者简介')
        if span:
            h2 = span.find_parent('h2')

            div = h2.find_next_sibling('div')

            return "</br>".join([text.get_text().strip() for text in div.find_all('p')])
        return ""

    def CataLog(self):
        print('-----目录-----:')

        span = self.soup.find('span', string='目录')
        if span:
            h2 = span.find_parent('h2')
        else:
            return ''
        div = h2.find_next_sibling('div')
        div2 = div.find_next_sibling('div')

        return div2.get_text().strip().replace('\n', '</br>')

    def Tags(self):
        print('------标签----:')
        div = self.soup.find(id='db-tags-section')
        if div:
            span = div.find_all('div', class_='indent')
            a = div.find_all("a", attrs={"class": "tag"}, text=True)

            return [text.get_text().strip() for text in a]
        return []

    def Like(self):
        print('------喜欢读的人也喜欢----:')
        div = self.soup.find(id='db-rec-section')
        if div:
            return [text.get_text().strip() for text in div.select('dd > a')]
        return []

    def Read(self):
        print('------想读----:')

        read = {'reading': 0, 'readed': 0, 'want_read': 0}

        div = self.soup.find(id='collector')
        if div:
            for p in div.find_all('p'):
                if '人在读' in p.a.get_text():
                    read['reading'] = int(p.a.get_text().replace('人在读', ''))
                if '人读过' in p.a.get_text():
                    read['readed'] = int(p.a.get_text().replace('人读过', ''))
                if '人想读' in p.a.get_text():
                    read['want_read'] = int(p.a.get_text().replace('人想读', ''))
        return read

    def WhereToBuy(self):
        print('------在哪儿买这本书----:')

        div = self.soup.find(id='buyinfo-printed')
        if div:
            div2 = div.find_all('a', class_='buylink-price')
            if div2 and div:
                return [link.get('href') for link in div.find_all('a', class_='buylink-price')]
        return []
