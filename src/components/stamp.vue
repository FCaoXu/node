<template>
<table border="1px"cellspacing="0px">
  <tr>
    <td>序号</td>
    <td v-for="(item,index) in moduel_data">{{item.name}}
    </td>
  </tr>

</table>
</template>

<script>
    export default {
        name: "stamp",
        data(){
            return{
                   moduel_data:[
                       {
                           name:'日期',
                           value:['','','']
                       },
                       {
                           name:'单位名称',
                           value:['','','']
                       },
                       {
                           name:'盖章内容',
                           value:['','','']
                       },
                       {
                           name:'文件号',
                           value:['','','']
                       },
                       {
                           name:'件数',
                           value:['','','']
                       },
                       {
                           name:'填写日期',
                           value:['','','']
                       },
                       {
                           name:'填写人',
                           value:['','','']
                       },
                       {
                           name:'承办人',
                           value:['','','']
                       }
                   ]
            }
        }
    }
</script>

<style scoped>
table{
  text-align: center;
}
td{
  width:100px;
}
</style>
