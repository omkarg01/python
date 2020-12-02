from requests_html import HTML, HTMLSession
import csv

with open('simple1.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)
print(match.html)

# print(html.html)
# print(html.text)

# match = html.find('title', first=True)
# print(match.text)

# match = html.find('#footer', first=True)
# print(match.text)

# articles = html.find('div.article')
# print(articles)
# for article in articles:
#     headline = html.find('h2', first=True)
# #     summary = html.find('p', first=True).text
#     print(headline.text)
# #     print(summary)
# #     print()

# session = HTMLSession()
# r = session.get('https://coreyms.com/')
#
# articles = r.html.find('article')
# # print(article.html)
#
# csv_file = open('cms_scrape1.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline', 'summary', 'video'])
#
# for article in articles:
#     headline = article.find('.entry-title-link', first=True).text
#     print(headline)
#
#     summary = article.find('.entry-content', first=True).text
#     print(summary)
#
#     try:
#         vid_src = article.find('iframe', first=True).attrs['src']
#         vid_id = vid_src.split('/')[4].split('?')[0]
#
#         yt_link = f'https://youtube.com//watch?v={vid_id}'
#
#
#     except:
#         yt_link=None
#
#
#     print(yt_link)
#     print()
#
#     csv_writer.writerow([headline, summary, yt_link])
#
# csv_file.close()
