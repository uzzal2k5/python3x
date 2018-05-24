import requests

status_id_list = ['135237519825044_1338020409546743', '135237519825044_2161777397171036',
                  '135237519825044_2162786230403486', '135237519825044_2164069750275134',
                  '135237519825044_2165185956830180', '135237519825044_2165344623480980',
                  '250144108362888_1795674990476451', '250144108362888_1796766303700653',
                  '250144108362888_1796825967028020']

count = (len(status_id_list))
print(count)


def url_redirect(url):
    for i in range(count):
        req = requests.head(url='https://www.facebook.com/' + status_id_list[i], allow_redirects=True)
        # print(r.status_code)
        print(req.url)



url_redirect(status_id_list)
