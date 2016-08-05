import scrapy 
import json
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy import optional_features
optional_features.remove('boto')
#from infor.items import InforItem

class infor(scrapy.Spider):
	name="infor"
	allowed_domains=["jd.com"]
	
	start_urls=["http://www.jd.com"]
	

	#get goods no from demo.json
	def parse(self,response):
		li=[]

	#fetch number tag of each goods
	#	for line in f.readlines():
	#		str_list=list(line)
	#		del str_list[-2]
	#		line="".join(str_list)
		
		
	#		if line[0] == '[':
	#			line = line[1:]

	#		if line[-1] == ']':
	#			print "last"
		
	#transfer string type into json
	#		line=json.loads(line)
		
		
	#		print line['name']
	#		no=line['no'][0].encode('utf-8')
	#		print no
		f=open("demo.json")

	#fetch number tag of each goods
		i = 0
		for line in f.readlines():
			#print type(line)
			line_1 = list(line)
			line_1.pop()
			#print  line_1[3:-2]
			get_id =  "".join(line_1[3:-2])
			
				
			no = get_id
			#print no
			if(li.count(no)==0):
				li.append(no)
	#save goods id checked,in case that mutiple checked
				#with open("checked.txt",'a') as file:
					#for l in range(0,len(li)):
					#file.write(no)
					#file.write('\n')
						#print type(str(list[l]))
	
	#only the goods unchecked that put into file
				new_url="http://club.jd.com/productpage/p-"+str(no)+"-s-0-t-0-p-0.html"
				part_url = "http://club.jd.com/productpage/p-"+str(no)+"-s-0-t-0-p-"
				#print new_url
				yield scrapy.Request(new_url,meta={'part_url':part_url},callback=self.parse_my)
		
	

	#to get cpmment page num
	def parse_my(self,response):
		jsonobj = response.body_as_unicode().encode('utf-8')
		s= json.loads(jsonobj)
		#print type(s)
		#lis = s['comments']
		#print lis[0].keys()
		#for no in range(0,len(lis)):
		#	print lis[no]['content']
		#get content in tag comments
		#print s
		comments = s['productCommentSummary']
		#print  comments.keys()
		#print type(comments)

		averageScore = comments['averageScore']
		beginRowNumber = comments['beginRowNumber']
		goodRate =comments['goodRate']
		poorRateShow=comments['poorRateShow']
		generalRateStyle = comments['generalRateStyle']
		poorRate = comments['poorRate']
		goodRateShow = comments['goodRateShow']
		generalRate = comments['generalRate']
		generalRateShow= comments['generalRateShow']
	        goodRateStyle= comments['goodRateStyle']
		skuId= comments['skuId']
		score5Count= comments['score5Count']
		score4Count = comments['score4Count']
		poorRateStyle = comments['poorRateStyle']
		goodCount = comments['goodCount']
		poorCount = comments['poorCount']
		score1Count = comments['score1Count']
		score3Count = comments['score3Count']
		commentCount = comments['commentCount']
		showCount = comments['showCount']
		generalCount = comments['generalCount']
		endRowNumber = comments['endRowNumber']
		productId  = comments['productId']
		score2Count  = comments['score2Count']
		name = s['comments'][0]['referenceName'].encode('utf-8')
		infor = "name "+str(name)+"  productId "+str(productId)+"  averageScore "+str(averageScore)+"  beginRowNumber "+str(beginRowNumber)+"  goodRate "+str(goodRate)+"  poorRateShow "+str(poorRateShow)+"  generalRateStyle "+str(generalRateStyle)+"  poorRate "+str(poorRate)+"  goodRateShow "+str(goodRateShow)+"  generalRate "+str(generalRate)+"  generalRateShow "+str(generalRateShow)+"  goodRateStyle "+str(goodRateStyle)+"  skuId "+str(skuId)+"  score5Count "+str(score5Count)+"  score4Count "+str(score4Count)+"  poorRateStyle "+str(poorRateStyle)+"  goodCount "+str(goodCount)+"  poorCount "+str(poorCount)+"  score1Count "+str(score1Count)+"  score3Count "+str(score3Count)+"  commentCount "+str(commentCount)+"  showCount "+str(showCount)+"  generalCount "+str(generalCount)+"  endRowNumber "+str(endRowNumber)+"  score2Count "+str(score2Count)+'\n'
		with open("demo_static.json",'w') as f:
				f.write(infor)
		#print len(comments)
		#f=codecs.open('demo_comment.json','a',encoding='utf-8')
		#f.write("--------------------------------------------------insert one goods comment----------------------------------------")
		#print "--------------------------------------------------insert one goods comment----------------------------------------"
		#line = json.dumps(comments,ensure_ascii=False)+"\n"
		#f.write(line)
		#f.close()
	
		#print s.keys() #get keys of json
		
		#item = InforItem()

		#item['Id'] = "Id "+str(s['productCommentSummary']['productId'] )
		#item['goodCount'] = "goodCount "+str(s['productCommentSummary']['goodCount'])
		#item['good'] = "goodRate "+str(s['productCommentSummary']['goodRate'])


		#print "generalCount "+str(s['productCommentSummary']['generalCount'])
		#print "generalRate "+str(s['productCommentSummary']['generalRate'])
		

		#print "poorCount "+str(s['productCommentSummary']['poorCount'])
		#print "poorRate "+str(s['productCommentSummary']['poorRate'])

		#for i in s['comments']:
			#print i['content']
			#with open("comment.json",'w') as f:
				#f.write(jsonobj)

		#page_num = s['productCommentSummary']['commentCount']/10
		#print "page_num"
		#print page_num
		#new_url=response.meta['part_url']
		#for p in range(1,page_num):
			#url=new_url+str(p)+".html"
			#print url
			#print '\n'
			#yield scrapy.Request(url,callback=self.parse_comment)

	def parse_comment(self,response):
		#get diffrent tags from the json text
		jsonobj = response.body_as_unicode().encode('utf-8')
		s= json.loads(jsonobj)
		lis = s['comments']
		name = s['comments'][0]['referenceName']		
		id = s['comments'][0]['referenceId']
		for no in range(0,len(lis)):
			with open("phone_comment_content.json","a") as f:
				f.write(id.encode('utf-8')+"  "+name.encode('utf-8')+"  "+lis[no]['content'].encode('utf-8')+'\n')
#			print name.encode('utf-8')
#			print id.encode('utf-8')
#			print lis[no]['content'].encode('utf-8')
		#s = js
		#if s!={}:
		#	comments = s['productCommentSummary']
			#print len(comments)
		#	f=codecs.open('demo_comment.json','a',encoding='utf-8')
		#	id = s['comments'][5]
		#	cont = s['comments'][2]
		#	print id
		#	print cont
			print "--------------------------------------------------insert one goods comment----------------------------------------"
			#print line
			#line = json.dumps(comments,ensure_ascii=False)+"\n"
			#f.write(line)
			#f.close()
			#f.write("--------------------------------------------------insert one goods comment----------------------------------------")
			print "--------------------------------------------------insert one goods comment----------------------------------------"
			#line = json.dumps(comments,ensure_ascii=False)+"\n"
			#f.write(line)
			#f.close()
	#		item = InforItem()
	#		
	#		print "************************************"
	#		item['Id'] = "Id "+str(s['productCommentSummary']['productId'] )
	#		item['goodCount'] = "goodCount "+str(s['productCommentSummary']['goodCount'])
	#		item['good'] = "goodRate "+str(s['productCommentSummary']['goodRate'])
	#

	#		print "generalCount "+str(s['productCommentSummary']['generalCount'])
	#		print "generalRate "+str(s['productCommentSummary']['generalRate'])
		

	#		print "poorCount "+str(s['productCommentSummary']['poorCount'])
	#		print "poorRate "+str(s['productCommentSummary']['poorRate'])

	#		for i in s['comments']:
	#			print i['content']
				#with open("comment.json",'w') as f:
					#f.write(jsonobj)
	
		
