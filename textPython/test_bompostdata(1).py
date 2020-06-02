


bomformdata = {'billid': 'ps123',
               'hardware_head': [{'name': '客户名称', 'value': '许继仪表'}, {'name': '订单区域', 'value': '许昌'},
                                               {'name': '受订单号', 'value': 'SDid20191021'},
                                               {'name': '计划号', 'value': 'Plan20191021'},
                                               {'name': '安装区域/用途', 'value': '不知道啥用途'},
                                               {'name': '技术要求', 'value': '不知道啥要求'}],
               'product_data': [{'name': '产品种类', 'value': '抄控器'}, {'name': '订单数量', 'value': '20'},
                                {'name': 'PCB版本', 'value': 'PcbV1.0'}, {'name': '安装图版本', 'value': 'TuV2.0'},
                                {'name': '确认人', 'value': '张三'}, {'name': '确认时间', 'value': '2019.10.21 09:23:00'}],
               'categoryID': [{'name': '外壳类型', 'value': '未知'}, {'name': '芯片LOGO', 'value': '无'},
                              {'name': '芯片ID', 'value': 'SNid20191021'}],
               'special_msg': {'name': '特殊物料替换', 'value': '无'},
               'LQ_confirmation': {'name': '联桥确认人', 'value': '李华', 'date': '2019.10.21 09:23:00'},
               'receive_sign': {'name': '研发中心', 'value': '赵六', 'date': '2019.10.21 09:23:00'}, 'file_number': 'wj123'}

bomdata = []
billid = bomformdata["billid"]
file_number  = bomformdata["file_number"]
hardware_head = bomformdata["hardware_head"]
product_data = bomformdata["product_data"]
categoryID = bomformdata["categoryID"]
special_msg = bomformdata["special_msg"]
LQ_confirmation = bomformdata["LQ_confirmation"]
receive_sign = bomformdata["receive_sign"]

bomdata.append(billid)
bomdata.append(file_number)

list = [hardware_head,product_data,categoryID]
for i in range(len(list)):
    for j in range(len(list[i])):
        bomdata.append(list[i][j]["value"])

bomdata.append(special_msg["value"])
bomdata.append(LQ_confirmation["value"])
bomdata.append(LQ_confirmation["date"])
print(bomdata)







