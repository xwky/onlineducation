<template>
    <div class="freecourse">
        <FreeCourseNav></FreeCourseNav>
        <div class="course_list">
            
            <div class="list" v-for="(item,index) in course" :key="index" >
                <div @click="click_nums(item.id)">
                    <div @click="change">
                    <router-link :to="{path:'/CourseDetail/', query:{id:item.id}}">
                <div  class="course-image"><img width="330px" :src="item.image"/></div>
                </router-link>
                </div>
                </div>
                
                <div class="course-title">{{item.name}}
                <!-- <div class="desc">免费</div> -->
                <!-- <p style="align:center margin-top:20px"><span class="iconfont icon-ren"></span></p>   -->
                <div class="course-detail">{{item.detail}}</div>
                </div>               
                <div class="collect" @click="collection(item.id)">
                   收藏                  
                    </div>
                <div class="course-span">{{item.degree}}</div>                               
            </div>
                
            <div class="page">
                <Page :total="dataCount" :page-size="pageSize"  @on-change="changepage"  show-total></Page>
            </div>
            
        </div>
        
        
    </div>
    
</template>

<script>
import FreeCourseNav from '@/components/header/FreeCourseNav'
export default {
    data(){
        return {
            // 全部课程
            list:[],
            course:[],
            // 一页显示的数据数
            pageSize:12,
            dataCount:"",
            userId:localStorage.getItem('userid')
        }
    },
    created(){
        this.getData();
        this.changepage();
        this.click_nums();
    },
    methods:{
        getData(){
            const father = this
            this.axios.get('http://127.0.0.1:8000/api/course/freecourse/').then(function(response){
                console.log(response.data)
                father.list = response.data
                father.dataCount = response.data.freecourse.length
                console.log(father.dataCount)
                if(father.dataCount<father.pageSize){
                    father.course = response.data.freecourse
                }else{
                    father.course = response.data.freecourse.slice(0,father.pageSize)
                    console.log(father.course)
                }
            })
    },
    // 改变每一个页面的数据
    changepage(index){
        var father = this
        let _start = (index - 1)*father.pageSize;
        let _end = index*father.pageSize;
        father.course = father.list.freecourse.slice(_start,_end)
    },
    change(){
            window.location.reload();
        },
    collection(id){
        let userId=localStorage.getItem('userid')
        const params = {
                uid:userId,
                cid:id
            };
        if(userId){
            console.log(params)
            this.$router.push({path:'/MyInfo',query:{uid:userId,cid:id}}),            
            this.axios.post('http://127.0.0.1:8000/api/course/addcourse/',
            {...params}).then(response => {
                console.log('123')
            })
            
        }else{
            this.$router.push('/Login')
        }
        
    },
    click_nums(id){
        this.axios.get('http://127.0.0.1:8000/api/course/clicknums/',{params:{cid:id,count:'1'}}).then(response=>{
            console.log(123)
        })
    }
    },

    components:{
        FreeCourseNav
    }
    
}
</script>

<style>
.freecourse{
    width: 90%;
    /* background: antiquewhite; */
    height: 1200px;
    margin-left: 5%;
}
.course_list{
    margin-top:-65px;
    float: left;
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
/* .course-title:hover{
    color: red;
} */
.course-title{
    font-size: 15px;
    font-weight: 900;
    text-align: left;
    color: black;
}
a:hover{
    color: red;
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
.collect{
    float: left;
    font-size: 15px;
    color: rosybrown;
    cursor: pointer;
}
.page{
    margin-top: 50px;
    display: flex;
    justify-content: flex-end;
    float: right; 
  }

</style>