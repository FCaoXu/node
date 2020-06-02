import pymysql
db = pymysql.connect(host = '192.168.2.174',port = 3306,user = 'root',passwd = 'Admin2019',db='lqkj_db',charset='utf8',connect_timeout=10)
cursor = db.cursor()
select = "select * from yw_bill_hardware_version_confirm where head_id='PS20191023' order by id desc limit 1"
cursor.execute(select)
row = cursor.fetchone()
# print(row)
bomform = {}
bomform["file_number"] = row[2]
name = ['客户名称','订单区域','受订单号','计划号','安装区域/用途','技术要求']
hardware_list=[]
for i in range(len(name)):
  hardware_dict ={}
  hardware_dict['name'] = name[i]
  hardware_dict['value'] = row[i+3]
  hardware_list.append(hardware_dict)
bomform['hardware_head'] = hardware_list
name = ['产品种类','订单数量','PCB版本','安装图版本','确认人','确认时间']
cursor.close()
