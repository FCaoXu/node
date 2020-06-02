import Vue from 'vue'
import Router from 'vue-router'
import BOM from '@/components/BOM'
import software from '@/components/software'
import textpy from '@/components/textpy'
import ndForm from '@/components/ndform'
import stamp from "@/components/stamp";
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'ndForm',
      component:ndForm
    },
     {
      path: '/bom',
      name: 'BOM',
      component: BOM
    },
    {
      path:'/software',
      name:'software',
      component: software
    },
    {
      path:'/text',
      name:'textpy',
      component:textpy
    },
    {
      path:'/stamp',
      name:'stamp',
      component:stamp
    }
  ]
})
