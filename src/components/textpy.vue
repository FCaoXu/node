<template>
  <div>
<el-table :data = table_text style="width: 600px" border>
  <el-table-column type="index"
  label="序号"
  width="180">  </el-table-column>
  <el-table-column
    prop="name"
    label="姓名"
  >
  </el-table-column>
  <el-table-column
    prop="sex"
    label="性别"
    width="180"
  >
  </el-table-column>
</el-table>
 <el-button type="primary"@click="submit">
   提交
 </el-button>
  </div>
</template>
<script>
  export default {
      name:'textpy',
      data() {
          return {
              table_text:[
                  {
                  name:'张三',
                  sex:'男',
                  },
                  {
                  name:'李四',
                  sex: '男',
                  },
                  {
                  name:'王二',
                  sex:'男',
                  }
                  ]
          }
      },
  methods:{
       submit(){
         this.$axios.post('/api',
             {
               table_data:this.table_text
             }
             )
          .then((response) => {
              this.$message.success('提交成功')
              // this.table_text= response.data
              console.log(response)
          })
          .catch((error) => {
              this.$message.error('提交失败')
          })
     }
  }
    }
</script>
