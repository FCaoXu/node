<template>
<div class="ndform"ref="printform">
<!--  市场部-->
  <table width="100%"cellspacing="0"align="center">
    <thead>
   <tr>
     <td rowspan="2"style="border-right: none;"></td>
     <td rowspan="2"style="border-left: none"><img src="@/assets/LQlogo.jpg"/></td>
    <td rowspan="2"colspan="4"style="font-size:40px;">{{ndform.title}}</td>
    <td>{{ndform.billdata.name}}</td>
    <td colspan="2"><el-input type="textarea" autosize  v-model="ndform.billdata.billid" :disabled="ndform.scpower"></el-input></td>
   </tr>
   <tr>
    <td>共 2 页</td>
    <td colspan="2">{{ndform.page}}</td>
   </tr>
   <tr>
    <td colspan="8">合同产品明细</td>
   </tr>
   <tr>
    <td  style="font-size:20px;width: 40px">类型</td>
    <td colspan="5">
      <template v-for="(item,index) in ndform.billdata.billtype_name">
        <label>
          <input type="radio":disabled="ndform.scpower" v-model="ndform.billdata.billtype" :value="ndform.billdata.billtype_name[index]"/>
        </label>
        <span style="margin-left: 25px;margin-right: 120px">{{ndform.billdata.billtype_name[index]}}</span>
      </template>
    </td>
    <td >填表日期:</td>
    <td ><input type="text" :disabled="ndform.scpower" v-model="ndform.billdata.billdate"/></td>
   </tr>
    <tr v-for="(item,index) in ndform.orderdata">
    <td rowspan="2" style="font-size:20px">序号</td>
    <td>{{item.order_name}}</td>
    <td>
       <el-input type="textarea" autosize  v-model="item.order_value" :disabled="ndform.scpower"></el-input>
    </td>
    <td>
     {{item.plan_name}}
    </td>
    <td> <el-input type="textarea" autosize  v-model="item.plan_value" :disabled="ndform.scpower"></el-input>
    </td>
    <td>
     {{item.cus_name}}
    </td>
    <td colspan="2">
      <el-input type="textarea" autosize  v-model="item.cus_value" :disabled="ndform.scpower"></el-input>
    </td>
   </tr>
   <tr style="height: 40px">
     <td v-for="(item,index) in ndform.cpdata" v-if="index<ndform.cpdata.length-1"> {{item.cpkey}} </td>
     <td v-for="(item,index) in ndform.cpdata" colspan="2" v-if="index>=ndform.cpdata.length-1"> {{item.cpkey}} </td>
   </tr>
   </thead>
   <tr v-for="(item,index) in ndform.cpdata[0].cpvalue">
     <td >{{index+1}}</td>
     <td v-for="(item,index1) in ndform.cpdata" v-if="index1<ndform.cpdata.length-1">
        <el-input type="textarea" autosize  v-model="item.cpvalue[index]" :disabled="ndform.scpower"></el-input>
     </td>
     <td v-for="(item,index1) in ndform.cpdata" colspan="2" v-if="index1>=ndform.cpdata.length-1">
        <el-input type="textarea" autosize  v-model="item.cpvalue[index]" :disabled="ndform.scpower"></el-input>
     </td>
   </tr>
   <tr>
    <td colspan="8">§本合同要求</td>
   </tr>

    <tr>
      <td :rowspan="ndform.htyq.length+2" style="font-size:20px;">其<br><br>他<br><br>要<br><br>求</td>
      <td colspan="7"style="height:60px">
        <el-input type="textarea" autosize style="height: 100%;" v-model="ndform.tsyq" :disabled="ndform.scpower"></el-input>
      </td>
     </tr>
    <tr>
        <td height="40px">特别关注</td>
      <td colspan="3">
        <el-input type="textarea" autosize v-model="ndform.tbgz" :disabled="ndform.scpower"></el-input>
      </td>
        <td>承诺时间</td>
        <td>完成时间</td>
        <td>负责人</td>
    </tr>
   <tr v-for="(item,index) in ndform.htyq">
   	<td height="40px"style="text-align:left">{{index+1}}、{{item.name}}</td>
    <td colspan="3" v-for="(value_item,value_index) in item.value">
       <el-input type="textarea" autosize v-model="item.value[value_index]" :disabled="ndform.scpower"></el-input>
    </td>
    <td v-for="(cltime_item,cltime_index) in item.cltime">
     <el-input type="textarea" autosize v-model="item.cltime[cltime_index]" :disabled="ndform.scpower"></el-input>
    </td>
    <td v-for="(wctime_item,wctime_index) in item.wctime">
      <el-input type="textarea" autosize v-model="item.wctime[wctime_index]" :disabled="ndform.scpower"></el-input>
    </td>
    <td v-if="index==0" :rowspan="ndform.htyq.length">
      <el-input type="textarea" autosize v-model="ndform.htyqFzr" :disabled="ndform.scpower"></el-input>
    </td>
   </tr>

<!--  研发中心-->
   <tr style="background-color:#84C1FF">
    <td colspan="5">一、配置要求（研发中心）</td>
    <td>承诺时间</td>
    <td>完成时间</td>
    <td>负责人</td>
   </tr>
      <tr v-for="(item,index) in ndform.pzdata" v-if="item.value.length==1">
        <td colspan="2"style="text-align:left" v-if="index ==2 ">
          <el-button type="text" style="font-size: 1rem !important;"@click="showsoftwart = true" :disabled="ndform.yfpower">
            {{index+1}}、{{item.name}}</el-button>
        </td>
        <td colspan="2"style="text-align:left;" v-else>{{index+1}}、{{item.name}}</td>

         <td colspan="3" v-for="(value1,index1) in item.value">
           <el-input type="textarea" autosize v-model="item.value[index1]" :disabled="ndform.yfpower"></el-input>
         </td>
         <td v-for="(value2,index2) in item.cltime">
          <el-input type="textarea" autosize v-model="item.cltime[index2]" :disabled="ndform.yfpower"></el-input>
         </td>
         <td v-for="(value3,index3) in item.wctime">
           <el-input type="textarea" autosize v-model="item.wctime[index3]" :disabled="ndform.yfpower"></el-input>
         </td>
         <td :rowspan="pzlength+1" v-if="index==0"style="border-left: none;">
            <el-input type="textarea" autosize  v-model="ndform.pzFzr" :disabled="ndform.yfpower"></el-input>
         </td>
       </tr>

   <template v-else>
      <tr >
        <td :rowspan="item.value.length+1" colspan="2" height="40px"style="text-align:left">{{index+1}}、{{item.name}}</td>
      </tr>
       <template>
         <tr v-for="(value,index) in item.value">
            <td style="border-right: none">
             <span v-if="index==0">
               <el-button type="text" style="font-size: 1rem !important;" @click="showbom = true" :disabled="ndform.yfpower">
                 {{ndform.pzdata_remask[index]}}
               </el-button></span>
              <span v-else>{{ndform.pzdata_remask[index]}}</span>
          </td>
         <td colspan="2" style="border-left: none">
            <el-input type="textarea" autosize :disabled="ndform.yfpower" v-model="item.value[index]"></el-input>
         </td>
         <td>
           <el-input type="textarea" autosize  v-model="item.cltime[index]" :disabled="ndform.yfpower"></el-input>
         </td>
         <td>
           <el-input type="textarea" autosize  v-model="item.wctime[index]" :disabled="ndform.yfpower"></el-input>
         </td>
        </tr>
      </template>
   </template>

<!--    物控中心-->
   <tr style="background-color:#84C1FF">
    <td colspan="5"height="40px">二、物料齐套（物控中心）</td>
    <td>承诺时间</td>
    <td>完成时间</td>
    <td>负责人</td>
   </tr>
    <tr v-for="(item,index) in ndform.wldata">
      <td colspan="2" style="text-align:left;height: 40px;">{{index+1}}、{{item.name}}</td>
      <td colspan="3" v-for="(value_item,value_index) in item.value">
        <el-input type="textarea" autosize v-model="item.value[value_index]" :disabled="ndform.wkpower"></el-input>
      </td>
      <td v-for="(cltime_item,cltime_index) in item.cltime">
        <el-input type="textarea" autosize v-model="item.cltime[cltime_index]" :disabled="ndform.wkpower"></el-input>
      </td>
      <td v-for="(wctime_item,wctime_index) in item.wctime">
        <el-input type="textarea" autosize v-model="item.wctime[wctime_index]" :disabled="ndform.wkpower"></el-input>
      </td>
      <td :rowspan="ndform.wldata.length" v-if="index==0"style="border-left: none;">
        <el-input type="textarea" autosize v-model="ndform.wlFzr" :disabled="ndform.wkpower"></el-input>
      </td>
    </tr>

<!--    质控中心-->
   <tr style="background-color:#84C1FF">
    <td colspan="5"height="40px">三、质量要求（质控中心）</td>
    <td>承诺时间</td>
    <td>完成时间</td>
    <td>负责人</td>
   </tr>
   <tr v-for="(item,index) in ndform.zldata">
      <td colspan="2" style="text-align:left;height: 40px;">{{index+1}}、{{item.name}}</td>
      <td colspan="3" v-for="(value_item,value_index) in item.value">
        <el-input type="textarea" autosize v-model="item.value[value_index]" :disabled="ndform.zkpower"></el-input>
      </td>
      <td v-for="(cltime_item,cltime_index) in item.cltime">
        <el-input type="textarea" autosize v-model="item.cltime[cltime_index]" :disabled="ndform.zkpower"></el-input>
      </td>
      <td v-for="(wctime_item,wctime_index) in item.wctime">
        <el-input type="textarea" autosize v-model="item.wctime[wctime_index]" :disabled="ndform.zkpower"></el-input>
      </td>
      <td :rowspan="ndform.zldata.length" v-if="index==0"style="border-left: none;">
        <el-input type="textarea" autosize v-model="ndform.zlFzr" :disabled="ndform.zkpower"></el-input>
      </td>
    </tr>

<!--    制造中心-->
   <tr style="background-color:#84C1FF">
    <td colspan="5"height="40px">四、工艺及生产要求（制造中心）</td>
    <td>承诺时间</td>
    <td>完成时间</td>
    <td>负责人</td>
   </tr>
    <tr v-for="(item,index) in ndform.gydata">
      <td colspan="2" style="text-align:left;height: 40px;">{{index+1}}、{{item.name}}</td>
      <td colspan="3" v-for="(value_item,value_index) in item.value">
        <el-input type="textarea" autosize v-model="item.value[value_index]" :disabled="ndform.propower"></el-input>
      </td>
      <td v-for="(cltime_item,cltime_index) in item.cltime">
        <el-input type="textarea" autosize v-model="item.cltime[cltime_index]" :disabled="ndform.propower"></el-input>
      </td>
      <td v-for="(wctime_item,wctime_index) in item.wctime">
        <el-input type="textarea" autosize v-model="item.wctime[wctime_index]" :disabled="ndform.propower"></el-input>
      </td>
      <td :rowspan="ndform.gydata.length" v-if="index==0"style="border-left: none;">
        <el-input type="textarea" autosize v-model="ndform.gyFzr" :disabled="ndform.propower"></el-input>
      </td>
    </tr>

<!--    物控中心-->
   <tr style="background-color:#84C1FF">
    <td colspan="5"height="40px">五、PMC(物控中心)</td>
    <td>承诺时间</td>
    <td>完成时间</td>
    <td>负责人</td>
   </tr>
     <tr v-for="(item,index) in ndform.pcmdata">
        <td colspan="2" style="text-align:left;height: 40px;">{{index+1}}、{{item.name}}</td>
        <td colspan="3" v-for="(value_item,value_index) in item.value">
          <el-input type="textarea" autosize v-model="item.value[value_index]" :disabled="ndform.wkpower"></el-input>
        </td>
        <td v-for="(cltime_item,cltime_index) in item.cltime">
          <el-input type="textarea" autosize v-model="item.cltime[cltime_index]" :disabled="ndform.wkpower"></el-input>
        </td>
        <td v-for="(wctime_item,wctime_index) in item.wctime">
          <el-input type="textarea" autosize v-model="item.wctime[wctime_index]" :disabled="ndform.wkpower"></el-input>
        </td>
        <td :rowspan="ndform.pcmdata.length" v-if="index==0"style="border-left: none;">
          <el-input type="textarea" autosize v-model="ndform.pcmFzr" :disabled="ndform.wkpower"></el-input>
        </td>
    </tr>
  </table>
<!--    各主管领导评审-->
  <table width="100%"cellspacing="0"align="center" id="table2">
   <tr style="background-color:#84C1FF">
    <td colspan="8">六、评审结论（各主管领导）</td>
   </tr>
    <tr>
      <td colspan="8" style="height: 60px;"></td>
    </tr>
   <tr v-for="(item,index) in ndform.psdata">
    <td :rowspan="ndform.psdata.length" style="font-size:30px;width: 50px" v-if="index==0">签<br><br><br>发</td>
    <td width="150px">{{item.name_key}}</td>
    <td  width="150px">
      <el-input type="textarea" autosize v-model="item.name_value"></el-input>
    </td>
    <td width="150px">{{item.date_key}}</td>
    <td width="150px">
      <el-input type="textarea" autosize v-model="item.date_value"></el-input>
    </td>
    <td width="150px">{{item.num_key}}</td>
    <td width="150px">
      <el-input type="textarea" autosize v-model="item.num_value"></el-input>
    </td>
   </tr>
  </table>

<!--  打开对话框BOM-->
  <el-dialog :visible.sync="showbom" class="dialog"><BOM @resetshowbom = "resetshowbom" v-bind:showbom="showbom" v-if="showbom"></BOM></el-dialog>
<!--  打开对话框software-->
  <el-dialog :visible.sync="showsoftwart" class="dialog"><software @resetshowsoftware = "resetshowsoftware" v-bind:showsoftwart="showsoftwart" v-if="showsoftwart"></software></el-dialog>
  <div style="width: 100%;height: 100%;margin: 20px 20px 20px 0">
    <el-button class="no-print"type="primary" style="width: 6rem" :loading="submitLoading" @click="uploadndform">提交</el-button>
  </div>
    <el-button @click="printpage">打印</el-button>
</div>
</template>
<script>
  import BOM from "./BOM";
  import software from "./software";
export default{
	name:'ndForm',
  components:{
    BOM,
    software,
  },
	data() {
    return {
      ndform:{
          title:"需求评审单",
          billdata: {
                  name:'评审单号',
                  billid:'',
                  billtype_name:['订单','备货计划','小批送样'],
                  billtype:'',
                  billdate:''
              },
          orderdata:[
              {
                  order_name:'受订单号',
                  order_value:'',
                  plan_name:'计划单号',
                  plan_value:'',
                  cus_name:'客户名称',
                  cus_value:''
              },
          ],
          cpdata:[
              {
                  cpkey:'产品名称',
                  cpvalue:['',''],
              },
              {
                  cpkey:'规格型号',
                  cpvalue:['',''],
              },
              {
                  cpkey:'数量',
                  cpvalue:['',''],
              },
              {
                  cpkey:'交货日期',
                  cpvalue:['',''],
              },
              {
                  cpkey:'业务员',
                  cpvalue:['',''],
              },
              {
                  cpkey:'使用地区',
                  cpvalue:['',''],
              },

          ],
          page:'',
          tsyq:'特殊要求：',
          tbgz:'',
          htyq:[
          {
            name:'芯片ID',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
          {
            name:'是否要求与送样产品一致',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
          {
            name:'说明要求',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
          {
            name:'纸箱要求',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
          {
            name:'装箱要求',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
          {
            name:'箱贴格式',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
              {
            name:'备品',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
              {
            name:'出厂检验报告',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
              {
            name:'发货要求',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
              {
            name:'其他',
            value:[''],
            cltime:[''],
            wctime:[''],
          },
        ],
          htyqFzr:'',
          pzdata_remask:['BOM','PCB1','PCB2','PCB3','PCB4'],
          pzdata:[
              {
                  name:'产品母配方（*）',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'硬件版本（*）',
                  // value:['BOM','PCB1','PCB2','PCB3','PCB4'],
                  value:['','','','',''],
                  cltime:['','','','',''],
                  wctime:['','','','',''],
              },
              {
                  name:'软件版本（*）',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'关键元器件清单',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'结构件（*）',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'包材',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'耗材',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'铭牌图纸',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'接线图纸',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
              {
                  name:'其他要求',
                  value:[''],
                  cltime:[''],
                  wctime:[''],
              },
          ],
          pzFzr:'pzddddd',
          wldata:[
              {
                  name:'物料齐套',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'外加工',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'其他',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
          ],
          wlFzr:'',
          zldata:[
              {
                  name:'检验标准',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'其他',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
          ],
          zlFzr:'',
          gydata:[
              {
                  name:'SOP-作业指导',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'工艺流程',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'烧录软件版本',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'产测软件版本',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'抄表软件版本',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'入库时间',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'其他',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
          ],
          gyFzr:'',
          pcmdata:[
              {
                  name:'入库时间',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
              {
                  name:'其他',
                  value:[''],
                  cltime:[''],
                  wctime:['']
              },
          ],
          pcmFzr:'',
          psdata:[
              {
                  name_key:'营销中心',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'营销中心',
                  num_value:''
              },
              {
                  name_key:'研发中心',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'研发中心',
                  num_value:''
              },
              {
                  name_key:'物控中心',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'物控中心',
                  num_value:''
              },
              {
                  name_key:'质控中心',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'质控中心',
                  num_value:''
              },
              {
                  name_key:'制造中心',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'制造中心',
                  num_value:''
              },
              {
                  name_key:'财务部',
                  name_value:'',
                  date_key:'日期',
                  date_value:'',
                  num_key:'财务部',
                  num_value:''
              },
          ],
          //  编辑权限设置
          // scpower:true,
          // yfpower:true,
          // wkpower:true,
          // zkpower:true,
          // propower:true,

          scpower:false,
          yfpower:false,
          wkpower:false,
          zkpower:false,
          propower:false,
      },
      pzlength:0,
      submitLoading:false,
      showbom:false,
      showsoftwart:false,
      rdcenter:false,

      uid:'',
      checksum:'',
    }
	},

  created(){
      var location=this.$route.query;
      this.uid=location.uid;
      this.checksum=location.checksum;
      this.getview()
  },
  mounted(){
	    this.getpzlen();
  },
	methods:{
	    printpage(){
	        this.$print(this.$refs.printform)
      },
	    // 获取渲染页面数据
      getview(){
        this.$axios.post('/api/lqkjbill',{
           trantype: "ndformView",
           uid:this.uid,
           checksum:this.checksum,
        })
          .then((response)=>{
            let code=response.data.respcode;//返回状态码
            let msg=response.data.respmsg;//返回信息
            let temp_data = response.data.ndforminfo;
            console.log('response',response);
            if(code==="000000"){
              console.log('temp_data=',temp_data);
              this.ndform = temp_data["ndform"]
            }else {
                this.$message.error(msg);//给出异常提示
              }
            })
            .catch((error) => {
              this.$message.error('请求异常');
          });
      },

      //提交表格数据
      uploadndform(){
        this.$axios.post('/api/lqkjbill',{
           trantype: "uploadndform",
           uid:this.uid,
           checksum:this.checksum,
           ndformdata:this.ndform,
        })
          .then((response)=>{
            let code=response.data.respcode;//返回状态码
            let msg=response.data.respmsg;//返回信息
            let temp_data = response.data.ndforminfo;
            console.log('response',response);
            if(code==="000000"){
              this.$message.success(msg);
            }else {
                this.$message.error(msg);//给出异常提示
              }
            })
            .catch((error) => {
              this.$message.error('请求异常');
          });
      },

	    // 获取pzdata中所有value长度和
	    getpzlen(){
	      var len = 0;
        for(var i=0;i<this.ndform.pzdata.length;i++){
            len +=this.ndform.pzdata[i].value.length
        }
        this.pzlength = len
      },

      //修改showbom 值
      resetshowbom(value){
            this.showbom = value
      },

      //修改resetshowsoftware 值
      resetshowsoftware(value){
            this.showsoftwart = value
      },

  },
}
</script>

<style>
  thead {
   display:table-header-group;
}
  @page{

margin:20px 0 10px 0;

}
  .ndform{
    position: relative;
    margin-top: 0px;
    margin-left: 50px;
    margin-right: 50px;
  }
  .ndform .el-dialog{
    width: 80%;
    margin-top: 6% !important;
    margin-right: 5%;
  }
  .ndform .el-dialog__body{
    width: 90%;
    margin: 0 auto;
  }
  .ndform td{
    text-align:center;
    padding:0;
    height:30px;
    border: 1px solid;
  }
  .ndform a{
    text-decoration: none;
  }
  .ndform a:hover{
    text-decoration: none;
  }
  .ndform input{
    width:100%;height:100%;
    border:none;background:none; outline:none;text-align:center;font-size: 17px;
  }
  .ndform .el-textarea__inner{
    width:100%;height:100%;
    border:none;background:none; outline:none;font-size: 16px;resize: none;overflow: hidden;
    font-family: "Microsoft YaHei UI";
    text-align: center;
    word-break: break-all;
    box-sizing: border-box;
  }
  .remask .el-textarea__inner{
    width:100%;height:100%;
    border:none;background:none; outline:none;font-size: 16px;resize: none;overflow: hidden;
    font-family: "Microsoft YaHei UI";
    text-align: left;
    word-break: break-all;
    box-sizing: border-box;
  }
  .ndform .span-style{
    margin-left:30px;
    margin-right: 120px;
    border:none;
  }
  .ndform label{
    position: absolute;
    display: inline-block;
    border: 1px solid #2c2c2c;
    width:20px;
    height:20px;
    border-radius: 1px;

  }
  .ndform label input[type="radio"] {
              appearance: none;
              -webkit-appearance: none;
              outline: none;
              margin: 0;
          }
  .ndform label input[type="radio"]:after {
    display: inline-block;
    position: absolute;
    content:"";
    background-color: transparent;
  }
   .ndform label input[type="radio"]:checked:after {
    font-weight:bold;
    font-size:18px;
    font-family:Sans-serif;
    background: transparent;
    top: -3px;
    left: 5px;
    content:"L";
    transform:matrix(-0.766044,-0.642788,-0.642788,0.766044,0,0);
      -webkit-transform:matrix(-0.766044,-0.642788,-0.642788,0.766044,0,0);
  }
</style>
