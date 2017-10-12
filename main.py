from scrapy.cmdline import execute

if __name__ == '__main__':
    # 在此添加专辑url列表或在命令行执行scrapy crawl fmfiles -a urls={多个专辑url，以逗号隔开}
    album_urls = ['http://www.ximalaya.com/8889234/album/3703879/']
    urls = ','.join(album_urls)
    execute_str = 'scrapy crawl fmfiles -a urls=' + urls
    execute(execute_str.split())
