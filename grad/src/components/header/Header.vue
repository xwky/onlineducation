<template>
    <div class="box">
        <div id="logo">
            <a @click="change"> 
                <router-link to="/"><img title="学习网" src="static/image/课程.png" width="50px" height="50px"></router-link>              
                               
            </a>
        </div>
        <div class="lanmu">
            <ul >
            <li  @click="change"><router-link  to="/FreeCourse">基础课程</router-link></li>
            <li  @click="change"><router-link  to="/PracticalCourse">实战课程</router-link></li>
            <li  @click="change"><router-link  to="/AllCourse">全部课程</router-link></li>
            <li @click="change"><router-link  to="/Freeback">意见反馈</router-link></li>

            </ul>
        </div>
        <div class="search">
            <van-search v-model="searchData" show-action placeholder="请输入搜索关键词" @search="onSearch">
            <div slot="action" @click="onSearch()">搜索</div>
           
            </van-search>
            
        </div>

        <div class="registe">
            <ul class="reg">
                <li @click="change" v-show="!userInfo.username">
                    <router-link  to="/Login">登录  /</router-link> 
                    <router-link  to="/Register">注册</router-link>
                </li>
                <li v-show="!!userInfo.username">
                    <div class="show_hidden">
                        <div @click="change" class="my_page">
                            <div class="info" >
                                <p @click="myinfo"><span class="iconfont icon-ren"></span>
                            <!-- <router-link :to="{path:'/MyInfo/', query:{username:userInfo.username,id:localStorage.getItem('userid')}}">{{userInfo.username}}</router-link> -->
                            {{userInfo.username}}/ 
                            </p>
                            </div>
                        </div>
                        <div @click="change" class="sign_out" >
                            <p @click="signOutFun()">  退出登录</p>
                            
                        </div>

                    </div>

                </li>
            </ul>
        </div>
        
    </div>
</template>

<script>
import store from '@/vuex/store';
import { mapState, mapActions } from 'vuex';
export default {
    created(){
        this.isLogin();
        // this.myinfo();
    },
    data(){
        return{
            value:'',
            searchData:''
        }
    },
    computed:{
        ...mapState(['userInfo'])
    },
    methods:{
        ...mapActions(['signOut','isLogin']),
        signOutFun(){
            this.signOut()
            this.$router.push({path:'/'});
        },       
        change(){
            window.location.reload();        
        },
        onSearch(){
            this.$router.push({path:'/Search',query: { searchData: this.searchData }});
            window.location.reload();
        },
        myinfo(){
            let userId=localStorage.getItem('userid')
            this.$router.push({
                path:'/MyInfo',name:'MyInfo',query:{
                    // username:this.userInfo.username,
                    uid:userId
                }
            })
        
    }
    
}
}
</script>

<style >
.box{
    background:gainsboro;
    height: 90px;
    margin-top: -60px;
}
#logo{
    float: left;
    width: 100px;
    height: 100px;
}
#logo img{
    /* 图片居中 */
    vertical-align: middle;
    margin-top: 15px;
}
.info{
    cursor: pointer;
}
.box ul{
    /* 去掉li标签前面的黑点 */
    list-style: none;
    margin-left: 100px;
}
.box li{
    float: left;
    font-size: 20px;
    margin-right: 15px;
    color: black;
    margin-top: 25px;
}
.box:link{
    color: black;
}
.search{
    width: 1100px;
    padding-top: 15px;
}
.registe{
    float: right;
    font-size: 20px;
    margin-top: -70px;
}
.show_hidden{
    float: left;
}
.my_page{
    float: left;
}
.sign_out{
    float: left;
    cursor: pointer;
    
}
a:hover{
    color: red;
}
a:active{
    color: red;
}
a{
    color: black;
}
</style>