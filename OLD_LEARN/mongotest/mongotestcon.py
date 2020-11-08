from pymongo import MongoClient

conn = MongoClient('mongodb://admin:admin@192.168.2.64:22020/')
db=conn['order']
coll=db['inventory_orders']
ret = coll.find()

print()
print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

for record in ret:
	#print out the document.
	#print(record['_id'] + ',',record['ord_master_id'] + ',',record['status'])
	print(record['_id'])
print()
conn.close()