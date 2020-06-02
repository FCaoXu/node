from django.shortcuts import HttpResponse
import json
import datetime
from admin_app import public
from admin_app import models
from django.db import connection, transaction

### 联桥科技评审单接口
def main(request):
    if request.method == "POST":
        log = public.logger
        #请求body转为json
        tmp =request.body
        tmp = tmp.decode(encoding='utf-8')
        reqest_body = json.loads(tmp)

        trantype = reqest_body['trantype']
        log.info('trantype=[%s]' % trantype)
        if trantype == 'ndformView':
            resp = ndformView(request,reqest_body)
        elif trantype == 'bomView':
            resp = bomView(request,reqest_body)
        elif trantype == 'softwareView':
            resp = softwareView(request,reqest_body)
        elif trantype == 'uploadndform':
            resp = uploadndform(request,reqest_body)
        elif trantype == 'uploadbomform':
            resp = uploadbomform(request, reqest_body)
        elif trantype == 'uploadsoftwareform':
            resp = uploadsoftwareform(request, reqest_body)
        elif trantype == 'ndformdetail':
            resp = ndformdetail(request, reqest_body)
        else:
            s = public.setrespinfo({"respcode": "100000", "respmsg": "api error"})
            resp = HttpResponse(s)
    elif request.method == "GET":
        s = public.setrespinfo({"respcode": "100000", "respmsg": "api error"})
        resp = HttpResponse(s)

    return resp


# 评审单页面数据（初始化）
def ndformView(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-ndformView-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
        "ndforminfo": {}
    }

    user_id = reqest_body.get('uid', None)

    ndformdata = {}
    ndformdata["title"]="需求评审单"

    billdata = {}
    billdata["name"] = "评审单号"
    billdata["billid"] = ""
    billdata["billtype_name"]=['订单', '备货计划', '小批送样']
    billdata["billtype"]=""
    billdata["billdate"]=""
    ndformdata["billdata"]=billdata

    orderdata = []
    orderdata_temp = {}
    orderdata_temp["order_name"] = '受订单号'
    orderdata_temp["order_value"] = ''
    orderdata_temp["plan_name"] = '计划单号'
    orderdata_temp["plan_value"] = ''
    orderdata_temp["cus_name"] = '客户名称'
    orderdata_temp["cus_value"] = ''
    orderdata.append(orderdata_temp)
    ndformdata["orderdata"] = orderdata

    cpdata = []
    cpkey = ['产品名称','规格型号','数量','交货日期','业务员','使用地区',]
    for i in range(len(cpkey)):
        cpdata_temp = {}
        cpdata_temp["cpkey"] = cpkey[i]
        cpdata_temp["cpvalue"] = ['','']
        cpdata.append(cpdata_temp)
    ndformdata["cpdata"]=cpdata

    ndformdata["page"] = ''
    ndformdata["tsyq"] = '特殊要求：'
    ndformdata["tbgz"] = ''

    htyq = []
    htyq_name = ['芯片ID','是否要求与送样产品一致','说明要求','纸箱要求','装箱要求','箱贴格式','备品','出厂检验报告','发货要求','其他']
    for i in range(len(htyq_name)):
        htyq_temp = {}
        htyq_temp["name"] = htyq_name[i]
        htyq_temp["value"] = ['']
        htyq_temp["cltime"] = ['']
        htyq_temp["wctime"] = ['']
        htyq.append(htyq_temp)
    ndformdata["htyq"]=htyq
    ndformdata["htyqFzr"] = ''

    ndformdata["pzdata_remask"] = ['BOM', 'PCB1', 'PCB2', 'PCB3', 'PCB4']
    pzdata = []
    pzname = ['产品母配方（*）','硬件版本（*）','软件版本（*）','关键元器件清单','结构件（*）','包材','耗材','铭牌图纸','接线图纸','其他要求']
    for i in range(len(pzname)):
        pzdata_temp = {}
        if i ==1:
            pzdata_temp["name"] = pzname[i]
            pzdata_temp["value"] = ['', '', '', '', '']
            pzdata_temp["cltime"] = ['', '', '', '', '']
            pzdata_temp["wctime"] = ['', '', '', '', '']
            pzdata.append(pzdata_temp)
        else:
            pzdata_temp["name"] = pzname[i]
            pzdata_temp["value"] = ['']
            pzdata_temp["cltime"] = ['']
            pzdata_temp["wctime"] = ['']
            pzdata.append(pzdata_temp)
    ndformdata["pzdata"] = pzdata
    ndformdata["pzFzr"] = ''

    wldata = []
    wlname=['物料齐套','外加工','其他']
    for i in range(len(wlname)):
        wldata_temp = {}
        wldata_temp["name"] = wlname[i]
        wldata_temp["value"] = ['']
        wldata_temp["cltime"] = ['']
        wldata_temp["wctime"] = ['']
        wldata.append(wldata_temp)
    ndformdata["wldata"] = wldata
    ndformdata["wlFzr"] = ''

    zldata = []
    zlname = ['检验标准', '其他']
    for i in range(len(zlname)):
        zldata_temp = {}
        zldata_temp["name"] = zlname[i]
        zldata_temp["value"] = ['']
        zldata_temp["cltime"] = ['']
        zldata_temp["wctime"] = ['']
        zldata.append(zldata_temp)
    ndformdata["zldata"] = zldata
    ndformdata["zlFzr"] = ''

    gydata = []
    gyname = ['SOP-作业指导', '工艺流程','烧录软件版本','产测软件版本','抄表软件版本','入库时间','其他']
    for i in range(len(gyname)):
        gydata_temp = {}
        gydata_temp["name"] = gyname[i]
        gydata_temp["value"] = ['']
        gydata_temp["cltime"] = ['']
        gydata_temp["wctime"] = ['']
        gydata.append(gydata_temp)
    ndformdata["gydata"] = gydata
    ndformdata["gyFzr"] = ''

    pcmdata = []
    pcmname = ['入库时间', '其他']
    for i in range(len(pcmname)):
        pcmdata_temp = {}
        pcmdata_temp["name"] = pcmname[i]
        pcmdata_temp["value"] = ['']
        pcmdata_temp["cltime"] = ['']
        pcmdata_temp["wctime"] = ['']
        pcmdata.append(pcmdata_temp)
    ndformdata["pcmdata"] = pcmdata
    ndformdata["pcmFzr"] = ''

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
    ndformdata["psdata"] = psdata
    # 权限设置
    cur = connection.cursor()
    sql = "select ROLE_ID from irsadmin_user_rule where USER_ID = %s"
    cur.execute(sql, user_id)
    row = cur.fetchone()
    power = [True,True,True,True,True]
    if row:
        print("row=",row)
        if "administrator" in row:
            for i in range(len(power)):
                power[i] = False
        elif "lqkj_oa_shichang" in row:
            power[0] = False
        elif "lqkj_yanfa" in row:
            power[1] = False
        elif "lqkj_wukong" in row:
            power[2] = False
        elif "lqkj_zhikong" in row:
            power[3] = False
        elif "lqkj_shengchan" in row:
            power[4] = False
    print('power=',power)
    cur.close()

    ndformdata["scpower"] = power[0]
    ndformdata["yfpower"] = power[1]
    ndformdata["wkpower"] = power[2]
    ndformdata["zkpower"] = power[3]
    ndformdata["propower"] = power[4]

    ndform = {}
    ndform["ndform"] = ndformdata
    jsondata["ndforminfo"]=ndform

    s = json.dumps(jsondata,cls = models.JsonCustomEncoder,ensure_ascii=False)
    log.info(s)
    log.info('----------------------lqkjbill-ndformView-end---------------------------')
    return HttpResponse(s)

# bom页面数据
def bomView(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-bomView-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))
    billid = reqest_body.get('billid',None)

    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
        "bominfo": {}
    }
    bomdata = {}

    # 查询数据库中是否存在对应评审单号的纪录，取最新的一条记录
    sql = "select * from yw_bill_hardware_version_confirm where head_id = %s order by id desc limit 1"
    cursor = connection.cursor()
    cursor.execute(sql,billid)
    log.info(sql % billid)
    row = cursor.fetchone()

    bomdata["billid"] = billid
    hardware_head = []
    hardware_head_name = ['客户名称','订单区域','受订单号','计划号','安装区域/用途',"技术要求"]
    for i in range(len(hardware_head_name)):
        hardware_head_temp = {}
        hardware_head_temp["name"] = hardware_head_name[i]
        if row:
            hardware_head_temp["value"] = row[i+3]
        else:
            hardware_head_temp["value"] = ''
        hardware_head.append(hardware_head_temp)
    bomdata["hardware_head"] = hardware_head

    product_data = []
    product_data_name = ['产品种类','订单数量','PCB版本','安装图版本','确认人','确认时间']
    for i in range(len(product_data_name)):
        product_data_temp = {}
        product_data_temp["name"] = product_data_name[i]
        if row:
            product_data_temp["value"] = row[i+9]
        else:
            product_data_temp["value"] = ''
        product_data.append(product_data_temp)
    bomdata["product_data"] = product_data

    categoryID = []
    categoryID_name = ['外壳类型','芯片LOGO','芯片ID']
    for i in range(len(categoryID_name)):
        categoryID_temp = {}
        categoryID_temp["name"] = categoryID_name[i]
        if row:
            categoryID_temp["value"] = row[i+16]
        else:
            categoryID_temp["value"] = ''
        categoryID.append(categoryID_temp)
    bomdata["categoryID"] = categoryID

    special_msg = {}
    special_msg["name"] = '特殊物料替换'
    if row:
        special_msg["value"] = row[15]
    else:
        special_msg["value"] = ''
    bomdata["special_msg"] = special_msg

    LQ_confirmation = {}
    LQ_confirmation["name"] ='联桥确认人'
    if row:
        LQ_confirmation["value"] = row[19]
        LQ_confirmation["date"] = row[20]
    else:
        LQ_confirmation["value"] = ''
        LQ_confirmation["date"] = ''
    bomdata["LQ_confirmation"] = LQ_confirmation

    receive_sign = {}
    receive_sign["name"] = '研发中心'
    receive_sign["value"] = ''
    receive_sign["date"] = ''
    bomdata["receive_sign"] = receive_sign

    bomdata["file_number"] = 'LQYX' + billid[4:]

    bomform = {}
    bomform["bomform"] = bomdata
    jsondata["bominfo"] = bomform

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)
    log.info('----------------------lqkjbill-bomView-end---------------------------')
    return HttpResponse(s)


# 软件版本页面数据
def softwareView(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-softwareView-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    billid = reqest_body.get('billid',None)

    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
        "softwareinfo": {}
    }

    # 查询数据库中是否存在对应评审单号的纪录，取最新的一条记录
    sql = "select * from yw_bill_software_version_confirm where head_id = %s order by id desc limit 1"
    cursor = connection.cursor()
    cursor.execute(sql, billid)
    log.info(sql % billid)
    row = cursor.fetchone()


    softwaredata = {}
    softwaredata["billid"] = billid
    softwaredata["file_number"] = 'LQYX' + billid[4:]
    if row:
        softwaredata["software_special_explanation"] = row[3]
    else:
        softwaredata["software_special_explanation"] = ''

    software_head = []
    software_head_name = ['客户名称','订单区域','受订单号','计划号','安装区域/用途','技术要求']
    for i in range(len(software_head_name)):
        software_head_temp = {}
        software_head_temp["name"] = software_head_name[i]
        if row:
            software_head_temp["value"] = row[i+4]
        else:
            software_head_temp["value"] = ''
        software_head.append(software_head_temp)
    softwaredata["software_head"] = software_head

    product_data = []
    product_data_name = ['产品种类','订单数量','软件内部版本信息','软件外部信息','硬件版本信息','模块ID','厂商代码','芯片代码','确认人','确认时间']
    for i in range(len(product_data_name)):
        product_data_temp = {}
        product_data_temp["name"] = product_data_name[i]
        if row:
            product_data_temp["value"] = row[i+10]
        else:
            product_data_temp["value"] = ''
        product_data.append(product_data_temp)
    softwaredata["product_data"] = product_data

    silk_seal = []
    silk_seal_name = ['厂家名称','规格型号','资产条码','丝印方式','CAD图纸']
    for i in range(len(silk_seal_name)):
        silk_seal_temp = {}
        silk_seal_temp["name"] = silk_seal_name[i]
        if row:
            silk_seal_temp["value"] = row[i+20]
        else:
            silk_seal_temp["value"] = ''
        silk_seal.append(silk_seal_temp)
    softwaredata["silk_seal"] = silk_seal

    pack_require = []
    pack_require_name = ['外箱尺寸','内衬形式','标签要求','贴纸尺寸图纸']
    for i in range(len(pack_require_name)):
        pack_require_temp = {}
        pack_require_temp["name"] = pack_require_name[i]
        if row:
            pack_require_temp["value"] = row[i+25]
        else:
            pack_require_temp["value"] = ''
        pack_require.append(pack_require_temp)
    softwaredata["pack_require"] = pack_require

    shell_else = []
    shell_else_name = ['壳体','芯片ID','芯片logo','资产条码','其他',]
    for i in range(len(shell_else_name)):
        shell_else_temp = {}
        shell_else_temp["name"] = shell_else_name[i]
        if row:
            shell_else_temp["value"] = row[29]
        else:
            shell_else_temp["value"] = ''
        shell_else.append(shell_else_temp)
    softwaredata["shell_else"] = shell_else

    LQ_confirmation = {}
    LQ_confirmation["name"] = '联桥确认人'
    if row:
        LQ_confirmation["value"] = row[34]
        LQ_confirmation["date"] = row[35]
    else:
        LQ_confirmation["value"] = ''
        LQ_confirmation["date"] = ''
    softwaredata["LQ_confirmation"] = LQ_confirmation

    receive_sign = {}
    receive_sign["name"] = '研发中心'
    receive_sign["value"] = ''
    receive_sign["date"] = ''
    softwaredata["receive_sign"] = receive_sign

    softwareform = {}
    softwareform["softwareform"] = softwaredata
    jsondata["softwareinfo"] = softwareform

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)
    log.info('----------------------lqkjbill-softwareView-end---------------------------')
    return HttpResponse(s)


# 提交ndform上传的数据
def uploadndform(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-uploadndform-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    user_id = reqest_body.get('uid', None)
    ndformdata = reqest_body.get('ndformdata',None)

    print('ndformdata=',ndformdata)

    head_data, body_data = ndform_analysis(ndformdata)

    # 数据提交到数据库
    head_insert_sql = review_form_head_sql()
    body_insert_sql = review_form_body_sql()

    print('head_insert_sql=%s'%head_insert_sql)
    print('body_insert_sql=%s'%body_insert_sql)
    print(body_data[0],len(body_data[0]))
    print('slq_body=',body_insert_sql%body_data[0])
    none_count = 0
    for i in range(1,len(head_data)-1):
        if head_data[i]=='':
            none_count +=1
    if none_count != 0:
        s = public.setrespinfo({"respcode": "900001", "respmsg": "数据未填写完整!"})
        return HttpResponse(s)
    else:
        cur = connection.cursor()  # 创建游标
        cur.execute(head_insert_sql,head_data)
        log.info(head_insert_sql % head_data)
        cur.close()

    cur = connection.cursor()  # 创建游标
    for item in body_data:
        cur.execute(body_insert_sql,item)
        log.info(body_insert_sql % item)
    cur.close()


    # 返回成功数据
    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
    }

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)

    log.info('----------------------lqkjbill-uploadndform--end---------------------------')
    return HttpResponse(s)

# 提交bom上传的数据
def uploadbomform(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-uploadbomform-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    user_id = reqest_body.get('uid', None)
    bomformdata = reqest_body.get('bomformdata',None)

    print('bomformdata=',bomformdata)

    bomdata = bomform_analysis(bomformdata)

    # 提交数据到数据库
    bom_sql = hardware_version_confirm_sql()

    none_count = 0
    for i in range(1, len(bomdata) - 1):
        if bomdata[i] == '':
            none_count += 1
    print('none_count=',none_count)
    if none_count != 0:
        s = public.setrespinfo({"respcode": "900001", "respmsg": "数据未填写完整!"})
        return HttpResponse(s)
    else:
        print(bomdata)
        print(len(bomdata))
        print(bom_sql % bomdata)
        cur = connection.cursor()  # 创建游标
        cur.execute(bom_sql, bomdata)
        log.info(bom_sql % bomdata)

        cur.close()

    # 返回成功数据
    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
    }

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)

    log.info('----------------------lqkjbill-uploadbomform--end---------------------------')
    return HttpResponse(s)

# 提交software上传的数据
def uploadsoftwareform(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-uploadsoftwareform-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    user_id = reqest_body.get('uid', None)
    softwareformdata = reqest_body.get('softwareformdata',None)

    print('softwareformdata=',softwareformdata)

    softwaredata = softwareform_analysis(softwareformdata)

    # 提交数据到数据库
    software_sql = software_version_confirm_sql()

    none_count = 0
    for i in range(1, len(softwaredata) - 1):
        if softwaredata[i] == '':
            none_count += 1
    print('none_count=', none_count)
    if none_count != 0:
        s = public.setrespinfo({"respcode": "900001", "respmsg": "数据未填写完整!"})
        return HttpResponse(s)
    else:
        print(softwaredata)
        print(len(softwaredata))
        print(software_sql % softwaredata)
        cur = connection.cursor()  # 创建游标
        cur.execute(software_sql, softwaredata)
        log.info(software_sql % softwaredata)
        cur.close()


    # 返回成功数据
    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
    }

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)

    log.info('----------------------lqkjbill-uploadsoftwareform--end---------------------------')
    return HttpResponse(s)

# ndform 详情页
def ndformdetail(reqest,reqest_body):
    log = public.logger
    log.info('----------------------lqkjbill-ndformdetail-begin---------------------------')
    print('123')
    print(reqest_body.get('trantype', None))

    # 返回成功数据
    jsondata = {
        "respcode": "000000",
        "respmsg": "交易成功",
        "trantype": reqest_body.get('trantype', None),
        "ndforminfo": {}
    }

    user_id = reqest_body.get('uid', None)
    infoid = reqest_body.get('infoid',None)
    alter = reqest_body.get('alter',None)

    cursor = connection.cursor()
    sql_one = "select * from  yw_bill_review_form_head where id = %s order by id desc limit 1"
    cursor.execute(sql_one,infoid)
    log.info(sql_one % infoid)
    row = cursor.fetchone()
    billid = row[1]
    ndform = {}
    ndform["title"] = '需求评审单'
    if row:
        ndform["billdata"] = {'name': '评审单号', 'billid': row[1], 'billtype_name': ['订单', '备货计划', '小批送样'],
                              'billtype': row[2], 'billdate': row[3]}
        ndform["orderdata"] = [
            {'order_name': '受订单号', 'order_value': row[4], 'plan_name': '计划单号', 'plan_value': row[5], 'cus_name': '客户名称',
             'cus_value': row[6]}, ]
        cpkey = ['产品名称', '规格型号', '数量', '交货日期', '业务员', '使用地区']
        tmplsit = []
        for i in range(len(cpkey)):
            tmpdict = {}
            tmpdict['cpkey'] = cpkey[i]
            tmpdict['cpvalue'] = [row[i + 7], '']
            tmplsit.append(tmpdict)
        ndform["cpdata"] = tmplsit
        ndform['tsyq'] = row[13]
        ndform['tbgz'] = row[14]
    cursor.close()

    cursor = connection.cursor()
    sql_two = "select * from  yw_bill_review_form_body where head_id = %s "
    cursor.execute(sql_two,billid)
    log.info(sql_two % billid)
    rows = cursor.fetchall()

    htyq_name = ['芯片ID', '是否要求与送样产品一致', '说明要求', '纸箱要求', '装箱要求', '箱贴格式', '备品', '出厂检验报告', '发货要求', '其他']
    pzname = ['产品母配方（*）', '硬件版本（*）', '软件版本（*）', '关键元器件清单', '结构件（*）', '包材', '耗材', '铭牌图纸', '接线图纸', '其他要求']
    wlname = ['物料齐套', '外加工', '其他']
    zlname = ['检验标准', '其他']
    gyname = ['SOP-作业指导', '工艺流程', '烧录软件版本', '产测软件版本', '抄表软件版本', '入库时间', '其他']
    pcmname = ['入库时间', '其他']
    section_list = ['htyq', 'pzdata', 'wldata', 'zldata', 'gydata', 'pcmdata']
    fzr_list = ['htyqFzr', 'pzFzr', 'wlFzr', 'zlFzr', 'gyFzr', 'pcmFzr']
    section_name_list = [htyq_name, pzname, wlname, zlname, gyname, pcmname]
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
                if int(item[2]) == i:
                    if item[2] == '1' and int(item[3]) > 0 and int(item[3]) < 6:
                        print('333333')
                        temp_value.append(item[5])
                        temp_cltime.append(item[6])
                        temp_wctime.append(item[7])
                        if item[3] == '5':
                            temp[i].append(
                                {'name': item[4], 'value': temp_value, 'cltime': temp_cltime, 'wctime': temp_wctime})
                            ndform[section_list[i]] = temp[i]
                            ndform[fzr_list[i]] = item[8]
                    else:
                        temp[i].append({'name': item[4], 'value': [item[5]], 'cltime': [item[6]], 'wctime': [item[7]]})
                        ndform[section_list[i]] = temp[i]
                        ndform[fzr_list[i]] = item[8]

    for i in range(len(temp)):
        if len(temp[i]) == 0:
            for index, other_item in enumerate(section_name_list[i]):
                if index == 1:
                    temp[i].append({'name': other_item, 'value': ['', '', '', '', ''], 'cltime': ['', '', '', '', ''],
                                    'wctime': ['', '', '', '', '']})
                    ndform[section_list[i]] = temp[i]
                    ndform[fzr_list[i]] = ''
                else:
                    temp[i].append({'name': other_item, 'value': [''], 'cltime': [''], 'wctime': ['']})
                    ndform[section_list[i]] = temp[i]
                    ndform[fzr_list[i]] = ''
    cursor.close()
    ndform['pzdata_remask'] = ['BOM', 'PCB1', 'PCB2', 'PCB3', 'PCB4']
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
    power = [True, True, True, True, True]
    if alter == True:
        cursor = connection.cursor()
        sql = "select ROLE_ID from irsadmin_user_rule where USER_ID = %s"
        cursor.execute(sql,user_id)
        log.info(sql % user_id)
        rowdata = cursor.fetchone()

        if rowdata:
            print("rowdata=", rowdata)
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
        print('power=', power)

    ndform["scpower"] = power[0]
    ndform["yfpower"] = power[1]
    ndform["wkpower"] = power[2]
    ndform["zkpower"] = power[3]
    ndform["propower"] = power[4]
    cursor.close()

    ndformdata = {}
    ndformdata["ndform"] = ndform
    jsondata["ndforminfo"] = ndformdata

    s = json.dumps(jsondata, cls=models.JsonCustomEncoder, ensure_ascii=False)
    log.info(s)

    log.info('----------------------lqkjbill-ndformdetail--end---------------------------')
    return HttpResponse(s)




# 评审单ndformdata解析
def ndform_analysis(ndformdata):
    body_data_list = []
    body_fzr_list = []
    billdata = ndformdata["billdata"]
    orderdata = ndformdata["orderdata"]
    cpdata = ndformdata["cpdata"]
    tsyq = ndformdata["tsyq"]
    tbgz = ndformdata["tbgz"]

    htyq = ndformdata["htyq"]
    body_data_list.append(htyq)
    htyqFzr = ndformdata["htyqFzr"]
    body_fzr_list.append(htyqFzr)
    pzdata = ndformdata["pzdata"]
    body_data_list.append(pzdata)
    pzFzr = ndformdata["pzFzr"]
    body_fzr_list.append(pzFzr)
    wldata = ndformdata["wldata"]
    body_data_list.append(wldata)
    wlFzr = ndformdata["wlFzr"]
    body_fzr_list.append(wlFzr)
    zldata = ndformdata["zldata"]
    body_data_list.append(zldata)
    zlFzr = ndformdata["zlFzr"]
    body_fzr_list.append(zlFzr)
    gydata = ndformdata["gydata"]
    body_data_list.append(gydata)
    gyFzr = ndformdata["gyFzr"]
    body_fzr_list.append(gyFzr)
    pcmdata = ndformdata["pcmdata"]
    body_data_list.append(pcmdata)
    pcmFzr = ndformdata["pcmFzr"]
    body_fzr_list.append(pcmFzr)

    print(body_data_list)
    print(body_fzr_list)

    billid = billdata["billid"]
    billtype = billdata["billtype"]
    billdate = billdata["billdate"]
    order_value = orderdata[0]["order_value"]
    plan_value = orderdata[0]["plan_value"]
    cus_value = orderdata[0]["cus_value"]

    power_list = []
    scpower = ndformdata["scpower"]
    power_list.append(scpower)
    yfpower = ndformdata["yfpower"]
    power_list.append(yfpower)
    wkpower = ndformdata["wkpower"]
    power_list.append(wkpower)
    zkpower = ndformdata["zkpower"]
    power_list.append(zkpower)
    propower = ndformdata["propower"]
    power_list.append(propower)
    power_list.append(wkpower)

    product_msg = []
    for i in range(len(cpdata)):
        product_msg.append(cpdata[i]["cpvalue"][0])

    product_tuple = ()
    for item in product_msg:
        protuple = (item,)
        product_tuple = product_tuple + protuple

    # 评审单主体数据
    head_data = (None, billid, billtype, billdate, order_value, plan_value, cus_value) + product_tuple + (
    tsyq, tbgz, '1')
    print(head_data)

    body_data = []  # 评审单明细数据
    for i in range(len(power_list)):
        if power_list[i] == False:
            count = 0
            for item in body_data_list[i]:
                for j in range(len(item["value"])):
                    temp_tuple = (None, billid, i, count, item["name"], item["value"][j], item["cltime"][j], item["wctime"][j], body_fzr_list[i])
                    body_data.append(temp_tuple)
                    count = count + 1
    print(body_data)
    return head_data,body_data

# BOM bomformdata解析
def bomform_analysis(bomformdata):
    bomdata = []
    billid = bomformdata["billid"]
    file_number = bomformdata["file_number"]
    hardware_head = bomformdata["hardware_head"]
    product_data = bomformdata["product_data"]
    categoryID = bomformdata["categoryID"]
    special_msg = bomformdata["special_msg"]
    LQ_confirmation = bomformdata["LQ_confirmation"]
    receive_sign = bomformdata["receive_sign"]

    bomdata.append(billid)
    bomdata.append(file_number)

    list = [hardware_head, product_data, categoryID]
    for i in range(len(list)):
        for j in range(len(list[i])):
            bomdata.append(list[i][j]["value"])

    bomdata.append(special_msg["value"])
    bomdata.append(LQ_confirmation["value"])
    bomdata.append(LQ_confirmation["date"])

    valuedata = (None,)
    for item in bomdata:
        tmptuple = (item,)
        valuedata = valuedata + tmptuple

    data = valuedata + ('1',)

    return data

# software softwareformdata解析
def softwareform_analysis(softwareformdata):
    billid = softwareformdata["billid"]
    file_number = softwareformdata["file_number"]
    software_special_explanation = softwareformdata["software_special_explanation"]
    software_head = softwareformdata["software_head"]
    product_data = softwareformdata["product_data"]
    silk_seal = softwareformdata["silk_seal"]
    pack_require = softwareformdata["pack_require"]
    shell_else = softwareformdata["shell_else"]
    LQ_confirmation = softwareformdata["LQ_confirmation"]
    receive_sign = softwareformdata["receive_sign"]

    softwaredata = [billid, file_number, software_special_explanation]

    list = [software_head, product_data, silk_seal, pack_require, shell_else]
    for i in range(len(list)):
        for j in range(len(list[i])):
            softwaredata.append(list[i][j]["value"])

    softwaredata.append(LQ_confirmation["value"])
    softwaredata.append(LQ_confirmation["date"])

    valuedata = (None,)
    for item in softwaredata:
        tmptuple = (item,)
        valuedata = valuedata + tmptuple

    data = valuedata + ('1',)
    return data

# 提取yw_bill_review_form_head insert语句
def review_form_head_sql():
    sql_one = "select column_name  from information_schema.columns where table_name='yw_bill_review_form_head'"
    cursor = connection.cursor()  # 创建游标
    cursor.execute(sql_one)
    data_two = cursor.fetchall()
    new_str = "INSERT INTO yw_bill_review_form_head(%s) values(%s)"
    valuelist = ''
    valuedata = ''
    for i in range(len(data_two)):
        temp_value = str(data_two[i][0])
        if i == 0:
            valuelist  = temp_value
            valuedata = '%s'
        else:
            valuelist = valuelist + ',' + temp_value
            valuedata = valuedata + ',' + '%s'
    sql = new_str %(valuelist,valuedata)
    print(sql)
    cursor.close()
    return sql

# 提取yw_bill_review_form_body insert语句
def review_form_body_sql():
    sql_one = "select column_name  from information_schema.columns where table_name='yw_bill_review_form_body'"
    cursor = connection.cursor()  # 创建游标
    cursor.execute(sql_one)
    data_two = cursor.fetchall()
    new_str = "INSERT INTO yw_bill_review_form_body(%s) values(%s)"
    valuelist = ''
    valuedata = ''
    for i in range(len(data_two)):
        temp_value = str(data_two[i][0])
        if i == 0:
            valuelist = temp_value
            valuedata = '%s'
        else:
            valuelist = valuelist + ',' + temp_value
            valuedata = valuedata + ',' + '%s'
    sql = new_str % (valuelist, valuedata)
    print(sql)
    cursor.close()
    return sql

# 提取yw_bill_hardware_version_confirm insert语句
def hardware_version_confirm_sql():
    sql_three = "select column_name  from information_schema.columns where table_name='yw_bill_hardware_version_confirm'"
    cursor = connection.cursor()  # 创建游标
    cursor.execute(sql_three)
    data_two = cursor.fetchall()
    new_str = "INSERT INTO yw_bill_hardware_version_confirm(%s) values(%s)"
    valuelist = ''
    valuedata = ''
    for i in range(len(data_two)):
        temp_value = str(data_two[i][0])
        if i == 0:
            valuelist = temp_value
            valuedata = '%s'
        else:
            valuelist = valuelist + ',' + temp_value
            valuedata = valuedata + ',' + '%s'
    sql = new_str % (valuelist, valuedata)
    print(sql)
    cursor.close()
    return sql

# 提取yw_bill_software_version_confirm insert语句
def software_version_confirm_sql():
    sql_four = "select column_name  from information_schema.columns where table_name='yw_bill_software_version_confirm'"
    cursor = connection.cursor()  # 创建游标
    cursor.execute(sql_four)
    data_two = cursor.fetchall()
    new_str = "INSERT INTO yw_bill_software_version_confirm(%s) values(%s)"
    valuelist = ''
    valuedata = ''
    for i in range(len(data_two)):
        temp_value = str(data_two[i][0])
        if i == 0:
            valuelist = temp_value
            valuedata = '%s'
        else:
            valuelist = valuelist + ',' + temp_value
            valuedata = valuedata + ',' + '%s'
    sql = new_str % (valuelist, valuedata)
    print(sql)
    cursor.close()
    return sql
