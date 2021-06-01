import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Index from '@/components/Index'
import Login from '@/components/Login'
import  Register from '@/components/Register'
import FreeCourse from '@/components/FreeCourse'
import CourseDetail from '@/components/CourseDetail'
import PracticalCourse from '@/components/PracticalCourse'
import AllCourse from '@/components/AllCourse'
import CourseListSelect from '@/components/CourseListSelect'
import Search from '@/components/Search'
import MyInfo from '@/components/MyInfo'
import Video from '@/components/Video'
import Freeback from '@/components/Freeback'

Vue.use(Router)

export default new Router({
  routes: [
    //首页
    {
      path: '/',
      name: 'Index',
      component: Index
    },

    // 登录页面
    {
      path:'/Login',
      name:'Login',
      component:Login
    },

    // 注册页面
    {
      path:'/Register',
      name:'Register',
      component:Register
    },

    // 免费课程
    {
      path:'/FreeCourse',
      name:'FreeCourse',
      component:FreeCourse
    },
    // 实战课程
    {
      path:'/PracticalCourse',
      name:'PracticalCourse',
      component:PracticalCourse
    },
    // 全部课程
    {
      path:'/AllCourse',
      name:'AllCourse',
      component:AllCourse
    },

    // 课程筛选
    {
      path:'/CourseListSelect',
      name:'CourseListSelect',
      component:CourseListSelect
    },

    // 课程详情页
    {
      path:'/CourseDetail',
      name:'CourseDetail',
      component:CourseDetail,
    },
    // 视频页面
    {
      path:'/Video',
      name:'Video',
      component:Video,
    },
    // 搜索课程
    {
      path:'/Search',
      name:'Search',
      component:Search
    },
    // 个人中心
    {
      path:'/MyInfo',
      name:'MyInfo',
      component:MyInfo

    },
    // 反馈页面
    {
      path:'/Freeback',
      name:'Freeback',
      component:Freeback
    }
  ]
})
