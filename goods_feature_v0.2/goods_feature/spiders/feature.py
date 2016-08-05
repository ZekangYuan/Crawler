import scrapy 
import json
import codecs
from scrapy import optional_features
from goods_feature.items import GoodsFeatureItem
optional_features.remove('boto')

class feature(scrapy.Spider):
	name="feature"
	
	allowed_domains=["jd.com","3.cn"]
	
	start_urls=["http://www.jd.com"]
	

	#get goods no from demo.json
	def parse(self,response):
		f=open("phone_id.txt")

	#fetch number tag of each goods
		i = 0
		for line in f.readlines():
			#print type(line)
			line_1 = list(line)
			line_1.pop()
			#print  line_1[3:-2]
			get_id =  "".join(line_1[3:-2])
			#print type(get_id)
			#if line != '\n':##################zhu yi cun chu de ge shi you huan hang 
			url = "http://item.jd.com/"+get_id+".html"
			print get_id
			#with open("checked_copy.txt",'a') as file:
			#	for l in range(0,len(li)):
			#		file.write(line)
			#		file.write('\n')
			yield scrapy.Request(url,meta={'no':get_id},callback=self.parse_info)
			print  "i---------------------------------->"
			print i
			i = i + 1

	def parse_info(self,response):
		#print "dalei"
		sg = response.xpath('//div[@class="w"]/div[@class="breadcrumb"]/strong/a/text()').extract()
		


		#print "zilei"
		span = response.xpath('//div[@class="breadcrumb"]/span/a/text()').extract()
		
		
		#price
		#pri = response.xpath('//strong[@class="p-price"]')
		#print pri
		#print "xinag xi  xinx xi"
		info = response.xpath('//ul[@class="p-parameter-list"]/li/text()').extract()
			
		
		no = response.meta['no']
		u = "http://p.3.cn/prices/get?type=1&pdtk=&pdbp=0&skuid=J_"+str(no)
		yield scrapy.Request(u,meta={'sg':sg,'span':span,'info':info},callback=self.pri)


	def pri(self,response):
		item = GoodsFeatureItem()
		jsonobj = response.body_as_unicode()
		ss = json.loads(jsonobj)[0]
			
		#print "da lei-------------------------"
		sg = response.meta['sg']
		item['dalei'] = sg
		span = response.meta['span']
		#print "xiao lei-----------------------"
#		for s in range(0,len(span)):
#			sub = span[s]
			#print sub.encode('utf-8')
		item['zilei'] = span
		info = response.meta['info']
		#print "xinag xi xin xi-----------------"
		item['xiangxi'] = info
		#for i in range(1,len(info)):
		#	print info[i].encode('utf-8')
		
		#print "price-------------------------"
		item['yuanjia'] = ss["m"]
		item['xianjia'] = ss["p"]
		yield item
		#print ss
		

				

