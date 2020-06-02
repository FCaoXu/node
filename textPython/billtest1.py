import re
import pymysql

db = pymysql.connect(host = '192.168.2.174',port = 3306,user = 'root',passwd = 'Admin2019',db='lqkj_db',charset='utf8',connect_timeout=10)
cursor = db.cursor()
sql_one = "select * from  yw_bill_review_form_head where head_id = 'PS20191023' order by id desc limit 1"
cursor.execute(sql_one)

row= cursor.fetchone()
print(row)
print(row[1])

exit(0)

ndform = {}
ndform["title"] = '需求评审单'
if row:
    ndform["billdata"]={'name':'评审单号','billid':row[1],'billtype_name':['订单','备货计划','小批送样'],'billtype':row[2],'billdate':row[3]}
    ndform["orderdata"]=[{'order_name':'受订单号','order_value':row[4],'plan_name':'计划单号','plan_value':row[5],'cus_name':'客户名称','cus_value':row[6]},]
    cpkey = ['产品名称','规格型号','数量','交货日期','业务员','使用地区']
    tmplsit = []
    for i in range(len(cpkey)):
        tmpdict = {}
        tmpdict['cpkey'] =cpkey[i]
        tmpdict['cpvalue'] = [row[i+7],'']
        tmplsit.append(tmpdict)
    ndform["cpdata"] = tmplsit
    ndform['tsyq'] = row[13]
    ndform['tbgz'] = row[14]
cursor.close()

cursor = db.cursor()
sql_two = "select * from  yw_bill_review_form_body where head_id = 'PS20191023'"

cursor.execute(sql_two)
rows = cursor.fetchall()

htyq_name = ['芯片ID','是否要求与送样产品一致','说明要求','纸箱要求','装箱要求','箱贴格式','备品','出厂检验报告','发货要求','其他']
pzname = ['产品母配方（*）','硬件版本（*）','软件版本（*）','关键元器件清单','结构件（*）','包材','耗材','铭牌图纸','接线图纸','其他要求']
wlname=['物料齐套','外加工','其他']
zlname = ['检验标准', '其他']
gyname = ['SOP-作业指导', '工艺流程','烧录软件版本','产测软件版本','抄表软件版本','入库时间','其他']
pcmname = ['入库时间', '其他']
section_list = ['htyq','pzdata','wldata','zldata','gydata','pcmdata']
fzr_list = ['htyqFzr','pzFzr','wlFzr','zlFzr','gyFzr','pcmFzr']
section_name_list = [htyq_name,pzname,wlname,zlname,gyname,pcmname]
temp = []
for i in range(len(section_list)):
    temp.append([])
print(temp)
temp_value = []
temp_cltime = []
temp_wctime = []
if rows:
    for i in range(len(section_list)):
        for item in rows:
            print(type(item[2]))
            if int(item[2])==i:
                if item[2] == '1' and int(item[3])>0 and int(item[3])<6:
                    print('333333')
                    temp_value.append(item[5])
                    temp_cltime.append(item[6])
                    temp_wctime.append(item[7])
                    if item[3]=='5':
                        temp[i].append({'name':item[4],'value':temp_value,'cltime':temp_cltime,'wctime':temp_wctime})
                        ndform[section_list[i]] = temp[i]
                        ndform[fzr_list[i]] = item[8]
                else:
                    temp[i].append({'name':item[4],'value':[item[5]],'cltime':[item[6]],'wctime':[item[7]]})
                    ndform[section_list[i]] = temp[i]
                    ndform[fzr_list[i]] = item[8]

for i in range(len(temp)):
    if len(temp[i]) ==0:
        for index,other_item in enumerate(section_name_list[i]):
            if index==1:
                temp[i].append({'name': other_item, 'value': ['','','','',''], 'cltime': ['','','','',''], 'wctime': ['','','','','']})
                ndform[section_list[i]] = temp[i]
                ndform[fzr_list[i]] = ''
            else:
                temp[i].append({'name':other_item,'value':[''],'cltime':[''],'wctime':['']})
                ndform[section_list[i]] = temp[i]
                ndform[fzr_list[i]] = ''
cursor.close()
ndform['pzdata_remask'] = ['BOM','PCB1','PCB2','PCB3','PCB4']
psdata = []
name_key = ['营销中心', '研发中心', '物控中心', '质控中心', '制造中心', '财务部']
for i in range(len(name_key)):
    psdata_temp = {}
    psdata_temp["name_key"] = name_key[i]
    psdata_temp["name_value"] = ''
    psdata_temp["date_key"] = '日期'
    psdata_temp["date_value"] = ''
    psdata_temp["num_key"] = name_key[i]
    psdata_temp["num_value"] = ''
    psdata.append(psdata_temp)
ndform["psdata"] = psdata

# 权限设置
user_id = '111112'
cursor = db.cursor()
sql = "select ROLE_ID from irsadmin_user_rule where USER_ID = %s" %user_id
cursor.execute(sql)
rowdata = cursor.fetchone()
power = [True,True,True,True,True]
if rowdata:
    print("rowdata=",rowdata)
    if "administrator" in rowdata:
        for i in range(len(power)):
            power[i] = False
    elif "lqkj_oa_shichang" in rowdata:
        power[0] = False
    elif "lqkj_yanfa" in rowdata:
        power[1] = False
    elif "lqkj_wukong" in rowdata:
        power[2] = False
    elif "lqkj_zhikong" in rowdata:
        power[3] = False
    elif "lqkj_shengchan" in rowdata:
        power[4] = False
print('power=',power)

ndform["scpower"] = power[0]
ndform["yfpower"] = power[1]
ndform["wkpower"] = power[2]
ndform["zkpower"] = power[3]
ndform["propower"] = power[4]
cursor.close()


