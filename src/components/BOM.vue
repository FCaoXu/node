<template>
  <div class="all">
    <el-form :model="bomform" :rules="rule.value" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <table>
      <tr>
        <td><img style="" src="@/assets/LQlogo.jpg"/></td>
        <td style="text-align: right;vertical-align: bottom;width: 80%">内部资料 未经允许不得扩散</td>
      </tr>
      <tr><td colspan="2" style="height: 1px"><hr style="margin: 0 auto"></td></tr>
      <tr><td colspan="2" style="text-align: center;font-size: 40px">硬件版本确认单</td></tr>
      <tr><td colspan="2" style="text-align: left;">
        <span style="margin-left: 1%;font-family: 楷体;font-size: 1rem;font-weight: bold;">文件号:{{bomform.file_number}}</span>
      </td></tr>
    </table>
    <table border="1" width="100%" cellspacing="0" align="center">
      <tr v-for="(item,index) in bomform.hardware_head">
        <td>{{item.name}}</td>
        <td colspan="5">
            <el-form-item :prop="'hardware_head.'+index+'.value'" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.value"></el-input>
            </el-form-item>
        </td>
      </tr>
<!--
      <tr v-for="item in bomform.product_category">
        <td colspan="2">{{item.name}}</td>
        <td>{{item.dan_name}}</td>
        <td>{{item.san_name}}</td>
        <td>{{item.concentrate_name}}</td>
        <td>{{item.collect_name}}</td>
      </tr>
      <tr v-for="item in bomform.hardware_category_quantity">
        <td colspan="2">{{item.name}}</td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_dan"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_san"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_concentrate"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_collect"></el-input>
        </td>
      </tr>
      <tr v-for="(item,index) in bomform.hardware_message">
        <td v-if="index==0" :rowspan="bomform.hardware_message.length+1">硬件</td>
        <td>{{item.name}}</td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_dan"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_san"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_concentrate"></el-input>
        </td>
        <td>
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.hardware_collect"></el-input>
        </td>
      </tr>
 -->
      <tr >
        <td v-for="(item,index) in bomform.product_data" v-if="index<2" rowspan="2">{{item.name}}</td>
        <td v-for="(item,index) in bomform.product_data" v-if="index==2" colspan="4">硬件</td>
      </tr>
      <tr>

        <td v-for="(item,index) in bomform.product_data" v-if="index>=2">{{item.name}}</td>
      </tr>
<!--      <tr>-->
<!--        <td colspan="3">硬件</td>-->
<!--      </tr>-->
<!--      <tr>-->
<!--        <td v-for="(item,index) in bomform.product_data" v-if="index>=2">{{item.name}}</td>-->
<!--      </tr>-->
      <tr>
        <td v-for="(item,index) in bomform.product_data">
          <el-form-item :prop="'product_data.'+index+'.value'" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center" v-model="item.value"></el-input>
          </el-form-item>
        </td>
      </tr>

      <tr>
        <td>{{bomform.special_msg.name}}</td>
        <td colspan="5">
          <el-form-item prop="special_msg.value" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center;" v-model="bomform.special_msg.value"></el-input>
          </el-form-item>
        </td>
      </tr>

      <tr v-for="(item,index) in bomform.categoryID">
        <td>{{item.name}}</td>
        <td colspan="5">
          <el-form-item :prop="'categoryID.'+index+'.value'" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center;" v-model="item.value"></el-input>
          </el-form-item>
        </td>
      </tr>
      <tr>
        <td>{{bomform.LQ_confirmation.name}}</td>
        <td colspan="3" style="border-right:none">
          <el-form-item prop="LQ_confirmation.value" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center;" v-model="bomform.LQ_confirmation.value"></el-input>
          </el-form-item>
        </td>
        <td style="border-left:none;border-right:none;text-align:right">日期:</td>
        <td style="border-left:none">
          <el-form-item prop="LQ_confirmation.date" :rules="rule.value">
          <el-input type="textarea" autosize style="text-align: center;" v-model="bomform.LQ_confirmation.date"></el-input>
          </el-form-item>
        </td>
      </tr>
      <tr>
        <td> 接收部门签字</td>
        <td>{{bomform.receive_sign.name}}</td>
        <td colspan="2" style="border-right:none">
          <el-input type="textarea" autosize style="text-align: center;" v-model="bomform.receive_sign.value"></el-input>
        </td>
        <td style="border-left:none;border-right:none;text-align:right">日期:</td>
        <td style="border-left:none">
          <el-input type="textarea" autosize style="text-align: center;" v-model="bomform.receive_sign.date"></el-input>
        </td>
      </tr>
    </table>
    <div style="width: 100%;height: 100%;margin: 20px 20px 20px 0">
      <el-button type="primary" style="width: 6rem" :loading="handloading" @click="handbom">提交</el-button>
    </div>
        </el-form>
  </div>
</template>
<script>
    export default {
        name: 'BOM',
        props:["showbom"],
        data() {
            return {
                rule:{
                    value:[
                        { required: true, message: '请输入活动名称', trigger: 'blur' },
                    ]
                },
                bomform:{
                    hardware_head: [
                    {
                        name: '客户名称',
                        value: ''
                    },
                    {
                        name: '订单区域',
                        value: ''
                    },
                    {
                        name: '受订单号',
                        value: ''
                    },
                    {
                        name: '计划号',
                        value: ''
                    },
                    {
                        name: '安装区域/用途',
                        value: ''
                    },
                    {
                        name: "技术要求",
                        value: ''
                    },
                ],
                    product_data:[
                        {
                            name:'产品种类',
                            value:'',
                        },
                        {
                            name:'订单数量',
                            value:'',
                        },
                        {
                            name:'PCB版本',
                            value:'',
                        },
                        {
                            name:'安装图版本',
                            value:'',
                        },
                        {
                            name:'确认人',
                            value:'',
                        },
                        {
                            name:'确认时间',
                            value:'',
                        },
                    ],
                    // hardware_category_quantity:[
                    //         {
                    //             name: '订单数量',
                    //             hardware_dan: '',
                    //             hardware_san: '',
                    //             hardware_concentrate: '',
                    //             hardware_collect: '',
                    //         },
                    //     ],
                    categoryID: [
                        {
                            name: '外壳类型',
                            value: ''
                        },
                        {
                            name: '芯片LOGO',
                            value: ''
                        },
                        {
                            name: '芯片ID',
                            value: ''
                        },
                    ],
                    // hardware_message:[
                    //     {
                    //         name: 'PCB版本',
                    //         hardware_dan_value: '',
                    //         hardware_san_value: '',
                    //         hardware_concentrate_value: '',
                    //         hardware_collect_value: ''
                    //     },
                    //         {
                    //             name: '安装图版本',
                    //             hardware_dan_value: '',
                    //             hardware_san_value: '',
                    //             hardware_concentrate_value: '',
                    //             hardware_collect_value: ''
                    //         },
                    //         {
                    //             name: '确认人',
                    //             hardware_dan_value: '',
                    //             hardware_san_value: '',
                    //             hardware_concentrate_value: '',
                    //             hardware_collect_value: ''
                    //         },
                    //         {
                    //             name: '确认时间',
                    //             hardware_dan_value: '',
                    //             hardware_san_value: '',
                    //             hardware_concentrate_value: '',
                    //             hardware_collect_value: ''
                    //         },
                    //     ],
                    // product_category: [
                    //     {
                    //         name: '产品种类',
                    //         dan_name: '单相模块',
                    //         san_name: '三相模块',
                    //         concentrate_name: '集中器模块',
                    //         collect_name: 'II型采集器模块',
                    //     }],
                    special_msg:{
                        name:'特殊物料替换',
                        value:''
                    },
                    // material_replace: '',
                    LQ_confirmation: {
                        name:'联桥确认人',
                        value:'',
                        date:'',
                    },
                    receive_sign: {
                        name:'研发中心',
                        value:'',
                        date:''
                    },
                    file_number: '',
                },

                handloading:false,
                uid:'',
                checksum:'',
            }
        },
        created(){
          var location=this.$route.query;
          this.uid=location.uid;
          this.checksum=location.checksum;
          // this.getbomview()
      },
        methods:{
            //获取页面渲染数据
            getbomview(){
              this.$axios.post('/api/lqkjbill',{
               trantype: "bomView",
               uid:this.uid,
               checksum:this.checksum,
            })
            .then((response)=>{
              let code=response.data.respcode;//返回状态码
              let msg=response.data.respmsg;//返回信息
              let temp_data = response.data.bominfo;
              console.log('response',response);
              if(code==="000000"){
                    console.log('temp_data=',temp_data);
                    this.bomform = temp_data["bomform"]
                  }else {
                      this.$message.error(msg);//给出异常提示
                    }
                  })
                  .catch((error) => {
                    this.$message.error('请求异常');
                });
              },

            //修改父组件
            handbom(){
                console.log('111');
                this.handloading = true;
                this.$emit('resetshowbom',false)
            }
        }
    }
</script>
<style>
  .all {
    position: relative;
    width: 100%;
    height: 100%;
    /*align: center;*/
    margin: 0 auto;
  }
  table {
    position: relative;
    text-align: center;
  }

  td {
    height: 40px;
    width: 200px;
  }

  .all .el-textarea__inner {
    border: none;
    background: none;
    outline: none;
    font-size: 17px;
    resize: none;
    overflow: hidden;
    height: 100%;
  }
</style>
