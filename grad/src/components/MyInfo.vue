<template>
    <div class="myinfo">
        <div class="head" v-for="(item,index) in userinformation" :key="index">
            <!-- <div class="user_image"><img :src="item.image"/></div> -->
            <div>
                <div class="username">欢迎{{item.username}}用户</div>
            </div>
            
        </div>
        <div class="course_list">
            <div class="my_course_title">**我的课程**</div>
            <div class="list" v-for="(item,index) in mycourse" :key="index" >
                <div  @click="change">
                    <router-link :to="{path:'/CourseDetail/', query:{id:item.id}}">
                <!-- <router-link :to="{name:'CourseDetail',params:{id:item.id}}"> -->
                <div class="course-image"><img width="330px" :src="item.image"/></div>
                <div class="course-title">{{item.name}}</div>
                <!-- <div class="desc">免费</div> -->
                <!-- <p style="align:center margin-top:20px"><span class="iconfont icon-ren"></span></p>   -->
                <div class="course-detail">{{item.detail}}</div>
                </router-link>

                </div>
                
                <div class="collect" @click="uncollect(item.id)">取消收藏</div>
                <div class="course-span">{{item.degree}}</div>               
                
            </div>
                
            <div class="page">
                <Page :total="dataCount" :page-size="pageSize"  @on-change="changepage"  show-total></Page>
            </div>
            
        </div>
    </div>

    
</template>

<script>
import store from '@/vuex/store';
import { mapState, mapActions } from 'vuex';
export default {
    data(){
        return {
            userinformation:[],
            mycourse:[],
            // 一页显示的数据数
            pageSize:12,
            dataCount:"",
        }
    },
    created(){
        this.showmsg();
        this.uncollect()
    },
    computed:{
        ...mapState(['userInfo'])
    },
    methods:{
        change(){
            window.location.reload();        
        },
        showmsg(){
            // const father = this
            this.axios.all([
                console.log(this.$route.query.username),
                this.axios.get('http://127.0.0.1:8000/api/user/userinfo/',{params:{uid:this.$route.query.uid}}).then(response => {                
                console.log(response.data);
                this.userinformation = response.data.userinfo;
                // this.mycourse = response.data.mycourse
            }),
            // this.axios.post('http://127.0.0.1:8000/api/course/addcourse/',{uid:this.$route.query.uid,
            // cid:this.$route.query.cid
            // }).then(response => {                
            //     console.log('123456');
            // }),
            // console.log(this.$route.query.id),
            this.axios.get('http://127.0.0.1:8000/api/course/mycourse/',{params:{uid:this.$route.query.uid
            }}).then(response => {                
                console.log(response.data);
                // this.userinformation = response.data.userinfo;
                this.mycourse = response.data.mycourse
            }),
            ])            
        },
        changepage(index){
        var father = this
        let _start = (index - 1)*father.pageSize;
        let _end = index*father.pageSize;
        father.course = father.list.practicalcourse.slice(_start,_end)
    },
    uncollect(id){
        console.log(id);
        let userId = localStorage.getItem('userid')
        console.log(userId);
        this.axios.all([
            this.axios.post('http://127.0.0.1:8000/api/course/delecourse/',{uid:userId,cid:id}).then(response => {
                console.log(userId,id)
            console.log('删除成功')
        }),

            this.axios.get('http://127.0.0.1:8000/api/course/mycourse/',{params:{uid:this.$route.query.uid
            }}).then(response => {                
                console.log(response.data);
                // this.userinformation = response.data.userinfo;
                this.mycourse = response.data.mycourse
            }),
        ])
        
    }
    }

    
}
</script>

<style>
.myinfo{
    width: 100%;
    /* background: white; */
    height: 1000px;
}
.head{
    width: 100%;
    height: 200px;
    background: whitesmoke;
    font-size: 30px;
    color: whitesmoke;
}
.username{
    font-size: 30px;
    color: black;
    float: left;
    margin-left: 5%;
    margin-top: 60px;
}
.course_list{
    /* background: antiquewhite; */
    width: 90%;
    /* height: 500px; */
    margin-left: 5%;
}
.my_course_title{
    font-size: 30px;
}
.list{
    float: left;
    width: 330px;
    height: 300px;
    /* background: #d9534f; */
    margin-left: 10px;
}
.course-image img{
    height: 180px;
    border-radius: 5%
}  
.course-detail{
    /* float: left; */
    margin-top: 5px;
    font-size: 10px;
    text-align: left;
    color: black;
}
.course-title{
    font-size: 15px;
    font-weight: 900;
    text-align: left;
    color: black;
}
/* .course-title:hover{
    color: red;
} */
.collect{
    float: left;
    font-size: 15px;
    color: rosybrown;
    cursor: pointer;
}
.desc{
    float: left;
    font-size: 15px;
    margin-top: 10px;
    color: #93A5C4;
}
.course-span{
    /* text-align: right; */
    /* margin-top: 20px; */
    float: right;
    font-size: 15px;
    color: #ccc;
}
.page{
    margin-top: 50px;
    display: flex;
    justify-content: flex-end;
    float: right; 
  }

</style>