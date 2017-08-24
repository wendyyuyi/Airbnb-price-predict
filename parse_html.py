from lxml import etree

def find_cities(big_title) :
    # There are 43 cities, 16 cities are in the US
    f = open('US_cities.txt','w')
    for city in big_title :
        full_name = city.text.split(',')
        if full_name[-1] == ' United States' :
            f.write(city.text + '\n')
            print full_name[0].lower()


f = open('insidebnb.html','r')

html = etree.HTML(f.read())

f.close()
city_list = ['asheville','austin','boston','chicago','denver','los-angeles','nashville','new-orleans','new-york-city','oakland','portland','san-diego','san-francisco','santa-cruz-county','seattle','washington-dc']

#big_title = html.xpath("//div[@class='contentContainer']/h2")

file_count = 0
f = open('urls.txt','w')
f_dir = open('dir.txt','w')
f_date = open('date.txt','w')
f_name = open('name.txt','w')

for city_name in city_list :
    content_table = html.xpath("//div[@class='contentContainer']/table[@class='table table-hover table-striped " + city_name + "']/tbody/tr")
    file_count = file_count + len(content_table)
    for tr in content_table :
        f.write(tr.xpath("td")[2].xpath("a")[0].attrib['href'] + '\n')
        f_dir.write(tr.xpath("td")[1].text + '\n')
        f_date.write(tr.xpath("td")[2].xpath("a")[0].attrib['href'].split('/')[-3] + '\n')
        f_name.write(tr.xpath("td")[2].xpath("a")[0].attrib['href'].split('/')[-1] + '\n')
print file_count
