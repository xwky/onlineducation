<template>
    <div class="contain">
        <div class="top" v-for="(item,index) in course" :key="index" >
            <div class="space"></div>
            <div class="title">{{item.name}}</div>
            <div class="img"><img width="330px" :src="item.image"/></div>
            <div class="detail">难度  {{item.degree}}  |   时长   {{item.learn_time}} 小时  |  学习人数 {{item.students}}  | 点击次数 {{item.fav_nums}} | </div>          
        <div class="line">      </div>
        </div>       
        <div class="middle">
            <div><div class="course_chapters">**课程章节**</div></div>
            <div class="lesson_name">
                <!-- 课程章节 -->
                <!-- <div class="course_lesson" v-for="item in course_lesson" :key="item.id">                -->

                <!-- 章节名称 -->
                    <!-- <div class="lesson_name" :id="item.id">
                        {{item.name}} -->
                        <!-- <router-link :to="{path:'/CourseDetail',query:{lid:item.id}}">{{item.name}}</router-link> -->
                    <!-- 每一节课 -->
                        <div v-for="(items,index) in lesson_video" :key="index">
                            <div class="lesson_sort" @click="video">{{items.name}}</div>
                            <!-- <div class="lesson_sort"><router-link :to="{path:'/Video'}">{{items.name}}</router-link></div> -->
                        </div>
                    <!-- </div> -->
                
                <!-- </div> -->
            </div>
            
        </div>

    </div>
    
</template>

<script>
export default {
    data(){
        return {
            course:[],
            course_lesson:'',
            lesson_video:[],
        }
    },
    created(){
        this.showcourse()
    },
    methods:{
        showcourse:function(){
            let father = this
            this.axios.all[(
                this.axios.get('http://127.0.0.1:8000/api/course/coursedetail/',{params:{cid:this.$route.query.id}}).then(response=>{
                console.log(response);
                console.log(response.data.course)
                father.course = response.data.course;
                // 章节
                console.log('2',response.data.course_lesson)
                father.course_lesson = response.data.course_lesson
                // 每一节课
                console.log(response.data.lesson_video)
                father.lesson_video = response.data.lesson_video
                
                // window.location.reload();
                // this.change()
            })
            // this.axios.get('http://127.0.0.1:8000/api/course/coursedetail/',{params:{lid:this.$route.query.lid}}).then(response=>{
            //     // 每一节课
            //     console.log(response.data.lesson_video)
            //     father.lesson_video = response.data.lesson_video
                
            //     // window.location.reload();
            //     // this.change()
            // })
            )]
            
            },

        change(){
            window.location.reload();
        },
        video(){
            let userId=localStorage.getItem('userid')
            if (userId){
                this.$router.push({path:'/Video'})
                }else{
            this.$router.push('/Login')
        }
            }
        }
    }
    

</script>

<style>
.top{
    width: 100%;
    height: 250px;
    background: #F8FAFC;
}
.space{
    width: 100%;
    height: 50px;
}
.title{
    width: 60%;
    font-size: 45px;
    font-style: initial;
    font-weight: 400;
    color: black;
    float: left;
}
.img img{
    border-radius: 10%;
    width: 200px;
    height: 150px;
}
.detail{
    width: 55%;
    margin-top: -30px;
    font-size: 15px;
    float: left;
}
.line{
    width: 100%;
    float: left;
    height: 5px;
    background:  rgba(230, 229, 225, 0.952);
    float: left;
    margin-top: 10px;
}
.middle{
    width: 80%;
    margin-left: 10%;
    height: 1000px;
    /* background: red; */
}
.course_chapters{
    /* float: left; */
    font-size: 30px;
}
.course_lesson{
    /* padding-top: 10px; */
    /* float: left; */
}
.lesson_sort{
    margin-left: 15%;
    text-align: left;
    font-size: 25px;
    cursor: pointer;
}
</style>