#coding='utf-8'
import scrapy
import string
import random
from scrapy import optional_features
from diverdity.items import DiverdityItem


optional_features.remove('boto')

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["jd.com"]
	start_urls = ["http://www.jd.com/allSort.aspx"]
	#start_urls = ["http://list.jd.com/list.html?cat=1713,3274"]

	def parse(self,response):
		filename = response.url.split("/")[-2]+'.html'
		i = 0
		with open(filename,'wb') as f:
			title = response.xpath('//div[@class="category-items clearfix"]/div[@class="col"]')#/div[@class="mc"]/div[@class="items"]/dl[@class="clearfix"]/dd')
			#print title
			cl = title[0]			#di 0 lie:zuobian de lie
			#print cl
			print "fetch col------------------------------------------"
			name = cl.xpath('div[@class="category-item m"]')
			wi = name[2]			#zhe yi lie de di 2 ge
			##print  "items"


			k =  wi.xpath('div[@class="mt"]/h2/span/text()').extract()
			itemname =  k[0].encode('utf-8')
			#print itemname				
				
			mc = wi.xpath('div[@class="mc"]/div[@class="items"]/dl[@class="clearfix"]/dd/a')
			for mc_c in mc:	
				name = mc_c.xpath('text()').extract()
				#print name[0].encode('utf-8')

				url = mc_c.xpath('@href').extract()
				#print url[0].encode('utf-8')
				sub_url = "http:"+url[0].encode('utf-8')
				if "list.html" in sub_url:
					alert =  itemname+"--------------------------------------------------------------->"+name[0].encode('utf-8')+sub_url
					yield scrapy.Request(sub_url,meta={'sub_url':sub_url,'alert':alert},callback=self.parse_dir_contents)


	def parse_dir_contents(self,response):	
		#tot = 1

		#print response.css('.fp-text > i:nth-child(3)')
		page =	response.xpath('//div[@id="J_topPage"]/span[@class="fp-text"]/i/text()').extract()
		main_url = response.meta['sub_url']      
		alert = response.meta['alert']
		#print   alert
		#print type(int(page[0]))
		#print int(page[0])
		#print file_name
		for sub_goods_pages in range(0,int(page[0])+1):
			#print alert
		 	new_url = main_url+"&page="+str(sub_goods_pages)+"&JL=6_0_0#J_main"
			#print new_url

			#rint '\n'
			#for ran_num in range(1,string.atoi(sub_goods_pages.encode('utf-8'))):
			#print sub_goods.extract()
				#new_url = main_url+"&page="+str(ran_num)+"&JL=6_0_0&ms=2#J_main"
				#print new_url
				#i = i + 1
				#print i
				#print '\n'
				#f.write(new_url)
				#f.write('\n')	
			yield scrapy.Request(new_url,callback=self.parse_goods)

	def parse_goods(self,response):
		#with open("goods_information.txt",'w') as f:
		#items = []
		for div in response.xpath('//li[@class="gl-item"]/div[@class="gl-i-wrap j-sku-item"]'):
			#item = DiverdityItem()
			no = div.xpath('@data-sku').extract()
			#item['no'] = no 

			name = div.xpath('div[@class="p-name"]/a/em/text()').extract()
			#item['name'] = name[0].encode('utf-8')
			#items.append(item)
			with open("houseapplication_id.txt","a") as f:
				f.write(str(no))
				f.write('\n')
			print no
			print name[0].encode('utf-8')
		#return items



		
		
	

				
	
