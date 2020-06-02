<template>
<div id="all">
<img src="@/assets/LQlogo.jpg"/>
<div style="text-align:right">内部资料 未经允许不得扩散</div>
<hr>
<div style="text-align:center;font-size:40px">
软件版本确认单
</div>
<label>文件号：</label>
<label>{{file_number}}</label>
<table border="1px"width="1200px"cellspacing="0"align="center">
<tr v-for="item in software_head">
<td>{{item.name}}</td>
<td colspan="5">
   <el-input type="textarea" autosize style="text-align: left;height: 100%" v-model="item.value"></el-input>
</td>
</tr>
<tr v-for="item in product_category">
    <td colspan="2">{{item.name}}</td>
    <td>{{item.dan_name}}</td>
    <td>{{item.san_name}}</td>
    <td>{{item.concentrate_name}}</td>
    <td>{{item.collect_name}}</td>
 </tr>
<tr v-for="item in software_category_quantity">
 <td colspan="2">{{item.name}}</td>
 <td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.software_dan"></el-input>
 </td>
 <td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.software_san"></el-input>
 </td>
 <td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.software_concentrate"></el-input>
 </td>
 <td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.software_collect"></el-input>
 </td>
</tr>
<tr v-for="(item,index) in software_message">
<td v-if="index==0" :rowspan="software_message.length+1">软件</td>
<td>{{item.name}}</td>
<td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.category_dan"></el-input>
</td>
<td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.category_san"></el-input>
</td>
<td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.category_concentrate"></el-input>
</td>
<td>
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.category_collect"></el-input>
</td>
</tr>
<tr>
<td style="border-right:none">软件特殊说明：</td>
<td colspan="4"style="text-align:left;border-left:none">
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="software_special_explanation"></el-input>
</td>
</tr>
<tr v-for="(item,index) in silk_seal">
<td v-if="index==0":rowspan="silk_seal.length">丝印要求</td>
<td colspan="2">{{item.name}}</td>
<td colspan="3">
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.value"></el-input>
</td>
</tr>
<tr v-for="(item,index) in pack_require">
<td v-if="index==0" :rowspan="pack_require.length">包装要求</td>
<td colspan="2">{{item.name}}</td>
<td colspan="3">
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.value"></el-input>
</td>
</tr>
<tr v-for="item in shell_else">
<td>{{item.name}}</td>
<td colspan="5">
   <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="item.value"></el-input>
</td>
</tr>
<tr>
 <td>联桥确认人</td>
 <td colspan="3"style="border-right:none">
    <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="LQ_confirmation"></el-input>
 </td>
 <td style="border-left:none;border-right:none;text-align:right">日期:</td>
 <td style="border-left:none">
     <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="LQ_confirmation_date"></el-input>
 </td>
 </tr>
 <tr>
 <td> 接收部门签字</td>
 <td>研发中心</td>
 <td colspan="2"style="border-right:none">
      <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="receive_sign"></el-input>
 </td>
 <td style="border-left:none;border-right:none;text-align:right">日期:</td>
 <td style="border-left:none">
       <el-input type="textarea" autosize style="text-align: left;height: 100%"v-model="receive_sign_date"></el-input>
 </td>
 </tr>
</table>
</div>
</template>
<script>
export default{
       name:'software',
       data(){
       return{
            LQ_confirmation:'',
            LQ_confirmation_date:'',
            receive_sign:'',
            receive_sign_date:'',
            software_head:
              [
              {
              name:'客户名称',
              value:''
              },
              {
              name:'订单区域',
              value:''
              },
              {
              name:'受订单号',
              value:''
              },
              {
              name:'计划号',
              value:''
              },
              {
              name:'安装区域/用途',
              value:''
              },
              {
              name:'技术要求',
              value:''
              },
              ],
              product_category:
              [{
	           name:'产品种类',
             dan_name:'单相模块',
             san_name:'三相模块',
             concentrate_name:'集中器模块',
             collect_name:'II型采集器模块',
              }],
              software_category_quantity:
	           [
	           {
             name:'订单数量',
	           hardware_dan:'',
	           hardware_san:'',
	           hardware_concentrate:'',
	           hardware_collect:'',
	           },
	           ],
             software_message:
             [
             {
               name:'软件内部版本信息',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'软件外部信息',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'硬件版本信息',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'硬件版本写入',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'模块ID',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'芯片ID',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'厂商代码',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'芯片代码',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'版本日期',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
               name:'确认人',
               category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             {
                name:'确认时间',
                category_dan:'',
               category_san:'',
               category_concentrate:'',
               category_collect:''
             },
             ],
             silk_seal:
             [{
                name:'厂家名称',
                value:''
             },
             {
                name:'规格型号',
                value:''
             },
             {
                name:'资产条码',
                value:''
             },
             {
                name:'丝印方式',
                value:''
             },
             {
                name:'CAD图纸',
                value:'',
             },
             ],
             pack_require:
             [
             {
                name:'外箱尺寸',
                value:''
             },
             {
                name:'内衬形式',
                value:''
             },
             {
                name:'标签要求',
                value:''
             },
             {
                name:'贴纸尺寸图纸',
                value:'',
             },
             ],
             shell_else:
             [{
                name:'壳体',
                value:''
             },
             {
                name:'芯片ID',
                value:'',
             },
             {
                name:'芯片logo',
                value:'',
             },
             {
                name:'资产条码',
                value:''
             },
             {
                name:'其他',
                value:''
             }
             ],
             file_number:'',
             software_special_explanation:'',
       }
       }
}
</script>
<style>
#all{
width:1200px;
margin:0 auto;
}
td{
width:200px;
height:40px;
text-align:center;
}
.el-textarea__inner {
    border: none;
    outline: none;
    font-size: 17px;
    resize: none;
    overflow: hidden;
  }
</style>
