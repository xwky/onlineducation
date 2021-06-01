<template>
    <div class="main">
        <!-- 轮播图 -->
        <div id="rotation">
            <!-- 分栏 -->
            <div class="fenlan">
                <div class="item" data-id="a" @mouseenter="showDetail(1)" @mouseleave="hideDetail(1)">
                    <span class="group">前沿 / 区块链 / 人工智能</span>                   
                    <img src="static/image/箭头 三角形.png" />                   
                    
                </div>
                <div class="item" data-id="b" @mouseenter="showDetail(2)" @mouseleave="hideDetail(2)">
                    <span class="group">前端 / 小程序 / JS</span>
                    <img src="static/image/箭头 三角形.png" />
                </div>
                <div class="item" data-id="c" @mouseenter="showDetail(3)" @mouseleave="hideDetail(3)">
                    <span class="group">后端 / JAVA / Python</span>
                    <img src="static/image/箭头 三角形.png" />
                </div>
                <div class="item" data-id="d" @mouseenter="showDetail(4)" @mouseleave="hideDetail(4)">
                    <span class="group">移动 / Android / iOS</span>
                    <img src="static/image/箭头 三角形.png" />
                </div>
                <div class="item" data-id="e" @mouseenter="showDetail(5)" @mouseleave="hideDetail(5)">
                    <span class="group">云计算 / 大数据 / 容器</span>
                    <img  src="static/image/箭头 三角形.png" />
                </div>
                <div class="item" data-id="f" @mouseenter="showDetail(6)" @mouseleave="hideDetail(6)">
                    <span class="group">运维 / 测试 / 数据库</span>
                    <img src="static/image/箭头 三角形.png" />
                </div>
                <div class="item" data-id="g" @mouseenter="showDetail(7)" @mouseleave="hideDetail(7)">
                    <span class="group">UI设计 / 3D动画 / 游戏</span>
                    <img src="static/image/箭头 三角形.png" />
                </div>
                
            </div>
            <!-- 轮播图部分 -->
            <div class="lunbo">
                <van-swipe :autoplay="3000">
                    <van-swipe-item v-for="(image, index) in images" :key="index">
                        <img v-lazy="image" :src="image" />
                    </van-swipe-item>
                </van-swipe>

            <!-- <van-swipe :autoplay="3000" indicator-color="white" touchable>
                <van-swipe-item>
                    <img src="https://img.mukewang.com/5e5483e5000163c418720764.jpg" alt />
                </van-swipe-item>
                <van-swipe-item>
                    <img src="https://img.mukewang.com/5e52a48c00012a6418720764.jpg" alt />
                </van-swipe-item>
                <van-swipe-item>
                    <img src="https://img.mukewang.com/5e52a4120001d33818720764.jpg" alt />
                </van-swipe-item>
                <van-swipe-item>
                    <img src="https://img.mukewang.com/5e4facf10001a36618720764.jpg" alt />
                </van-swipe-item>
          </van-swipe> -->

            </div>

        </div>
        <transition name="fade">
            <div class="detail-item-panel panel-1" :duration="{enter:100,leave:100}" v-show="panel1" @mouseenter="showDetail(1)" ref="itemPanel1" @mouseleave="hideDetail(1)">
                <div class="nav-detail-item">
                    <span>前沿技术  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData1.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>
        <transition name="fade">
            <div class="detail-item-panel panel-2" :duration="{enter:100,leave:100}" v-show="panel2" @mouseenter="showDetail(2)" ref="itemPanel2" @mouseleave="hideDetail(2)">
                <div class="nav-detail-item">
                    <span>前端开发  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData2.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <transition name="fade">
            <div class="detail-item-panel panel-3" :duration="{enter:100,leave:100}" v-show="panel3" @mouseenter="showDetail(3)" ref="itemPanel3" @mouseleave="hideDetail(3)">
                <div class="nav-detail-item">
                    <span>后端开发  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData3.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <transition name="fade">
            <div class="detail-item-panel panel-4" :duration="{enter:100,leave:100}" v-show="panel4" @mouseenter="showDetail(4)" ref="itemPanel4" @mouseleave="hideDetail(4)">
                <div class="nav-detail-item">
                    <span>移动开发  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData4.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <transition name="fade">
            <div class="detail-item-panel panel-5" :duration="{enter:100,leave:100}" v-show="panel5" @mouseenter="showDetail(5)" ref="itemPanel5" @mouseleave="hideDetail(5)">
                <div class="nav-detail-item">
                    <span>计算机基础  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData5.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <transition name="fade">
            <div class="detail-item-panel panel-6" :duration="{enter:100,leave:100}" v-show="panel6" @mouseenter="showDetail(6)" ref="itemPanel6" @mouseleave="hideDetail(6)">
                <div class="nav-detail-item">
                    <span>运维/测试  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData6.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <transition name="fade">
            <div class="detail-item-panel panel-7" :duration="{enter:100,leave:100}" v-show="panel7" @mouseenter="showDetail(7)" ref="itemPanel7" @mouseleave="hideDetail(7)">
                <div class="nav-detail-item">
                    <span>UI/多媒体  </span>
                </div>
                <ul  @click="change">
                    <li v-for="(items, index) in panelData7.classNav" :key="index" class="detail-item-row">
                        <span class="glyphicon glyphicon-menu-right"></span>
                        <router-link to="/AllCourse" v-for="(item, subIndex) in items.tags" :key="subIndex">
                            <span class="detail-item">{{item}}</span>
                        </router-link>
                    </li>
                </ul>
            </div>
        </transition>

        <!-- 新上好课 -->
        <div class="new">
            <div class="title">
                新上好课
            </div>
            <div class="course">
                <div class="course-card" v-for="(item,index) in content1" :key="index">
                    <div @click="click_nums(item.id)">
                    <div @click="change">
                    <router-link :to="{path:'/CourseDetail/', query:{id:item.id}}">
                <div  class="course-image"><img width="330px" :src="item.image"/></div>
                </router-link>
                </div>
                </div>


                <div class="course-title">{{item.name}}</div>
                <div class="course-span">{{item.degree}}</div>
                <div class="course-price">￥{{item.click_nums}}</div>
                    
            </div>
            </div>
            
        </div>

        <!-- 热门课程 -->
        <div class="new">
            <div class="title">
                热门课程
            </div>
            <div class="course">
                <div class="course-card" v-for="(item,index) in content2" :key="index">
                    <div @click="click_nums(item.id)">
                    <div @click="change">
                    <router-link :to="{path:'/CourseDetail/', query:{id:item.id}}">
                <div  class="course-image"><img width="330px" :src="item.image"/></div>
                </router-link>
                </div>
                </div>


                <div class="course-title">{{item.name}}</div>
                <div class="course-span">{{item.degree}}</div>
                <div class="course-price">￥{{item.click_nums}}</div>
                    
            </div>
                
            </div>
            </div>
            
        </div>
 
    
</template>

<script>

// import {Lazyload} from 'vant';
// Vue.use(Lazyload);

export default {
    data(){
        return{
            content1:[],
            content2:[],
            images:[
                'https://img.mukewang.com/5e5483e5000163c418720764.jpg',
                'https://img.mukewang.com/5e52a48c00012a6418720764.jpg',
                'https://img.mukewang.com/5e52a4120001d33818720764.jpg',
                'https://img.mukewang.com/5e4facf10001a36618720764.jpg'
            ],
            panel1:false,
            panel2:false,
            panel3:false,
            panel4:false,
            panel5:false,
            panel6:false,
            panel7:false,
            

            panelData1:{
                classNav:
                [
                    {
                     tags:['微服务','区块链','机器学习','自然语言处理','数据分析&挖掘']
                }
                ]                
            },
            panelData2:{
                classNav:
                [
                    {
                     tags:['HTML/CSS','JavaScript','Vue','React','Node','jQuery','Bootstrap','WebApp','小程序']
                }
                ]                
            },

            panelData3:{
                classNav:
                [
                    {
                     tags:['Java','SpringBoot','SSM','Python','爬虫','Django','Go','PHP','C','C++','C#']
                }
                ]                
            },
            panelData4:{
                classNav:
                [
                    {
                     tags:['Android','iOS','React native','WEEX']
                }
                ]                
            },

            panelData5:{
                classNav:
                [
                    {
                     tags:['计算机网络','算法与数据结构','数学','大数据','Spark','Storm','云计算','AWS','Docker']
                }
                ]                
            },
            panelData6:{
                classNav:
                [
                    {
                     tags:['运维','自动化运维','运维工具','中间件','测试','自动化测试','MySQL','Redis','MongoDB','SQL Server']
                }
                ]                
            },

            panelData7:{
                classNav:
                [
                    {
                     tags:['模型设计','动效动画','设计基础','设计工具','Unity 3D']
                }
                ]                
            }
           

        }
    },
    created(){
        this.getData()
    },
    methods:{
    click_nums(id){
        this.axios.get('http://127.0.0.1:8000/api/course/clicknums/',{params:{cid:id,count:'1'}}).then(response=>{
            console.log(123)
        })
    },
        change(){
            window.location.reload();        
        },
        getData(){
            const father = this
            this.axios.all([
            this.axios.get('http://127.0.0.1:8000/api/course/newcourse/').then(function(response){
                console.log(response.data.newcourse)
                father.content1 = response.data.newcourse
                // father.content2 = response.data.coures2
            }),

            this.axios.get('http://127.0.0.1:8000/api/course/hotcourse/').then(function(response){
                console.log(response.data.hotcourse)
                // father.content1 = response.data.newcourse
                father.content2 = response.data.hotcourse
            })
            ])
        },
        showDetail(index){
            if (index === 1){this.panel1 = true}else{this.panel1 = false}
            if (index === 2){this.panel2 = true}else{this.panel2 = false}
            if (index === 3){this.panel3 = true}else{this.panel3 = false}
            if (index === 4){this.panel4 = true}else{this.panel4 = false}
            if (index === 5){this.panel5 = true}else{this.panel5 = false}
            if (index === 6){this.panel6 = true}else{this.panel6 = false}
            if (index === 7){this.panel7 = true}else{this.panel7 = false}
        },
        hideDetail(index){
            if (index === 1){this.panel1 = false}
            if (index === 2){this.panel2 = false}
            if (index === 3){this.panel3 = false}
            if (index === 4){this.panel4 = false}
            if (index === 5){this.panel5 = false}
            if (index === 6){this.panel6 = false}
            if (index === 7){this.panel7 = false}

        }
    },
    mounted(){
        this.$refs.itemPanel1.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel2.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel3.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel4.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel5.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel6.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel7.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
            
        this.$refs.itemPanel1.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel2.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel3.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel4.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel5.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel6.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel7.style.top = this.$refs.navSide.offsetTop + 'px';
    },
    updated(){
        this.$refs.itemPanel1.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';     
        this.$refs.itemPanel2.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel3.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';     
        this.$refs.itemPanel4.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel5.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';     
        this.$refs.itemPanel6.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';
        this.$refs.itemPanel7.style.left =
            this.$refs.navSide.offsetLeft + this.$refs.navSide.offsetWidth + 'px';     


        this.$refs.itemPanel1.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel2.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel3.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel4.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel5.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel6.style.top = this.$refs.navSide.offsetTop + 'px';
        this.$refs.itemPanel7.style.top = this.$refs.navSide.offsetTop + 'px';

    }
}
</script>

<style>
#rotation{
    height: 520px;
    /* background: gold; */
    margin-top: 20px;
    width: 90% ;
    margin-left: 5%;
    /* float: right; */
}
.fenlan{
    float: left;
    height:500px;
    background: whitesmoke;
    width: 270px;
    margin-left: 50px;
    cursor: pointer;
}

.item{
    color: black;
    padding-top: 40px;
    padding-left: 10px;
    font-size: 20px;
    text-align: left;
}
.item img{
    width: 20px;
    height: 20px;
    float: right;
    
}
.lunbo{
    width: 950px;
    height: 500px;
    /* background: red; */
    /* float: left; */
    overflow: hidden;
}
.lunbo img{
    width:936px;
    height:500px;
    border-radius: 3%
}

.detail-item-panel {
  width: 900px;
  height: 500px;
  background-color: ghostwhite;
  position: absolute;
  top: 110px;
  left: 395px;
  z-index: 999;
}
.nav-detail-item{
    font-size: 20px;
    margin-bottom: 30px;
    margin-top: 20px;
}

.detail-item-panel ul {
  list-style: none;
}
.detail-item-panel li {
  line-height: 38px;
  margin-left: 40px;
}

.detail-item{
  font-size: 20px;
  text-align: center;
  padding-left: 12px;
  padding-right: 8px;
  cursor: pointer;
  border-left: 1px solid #ccc;
}
.detail-item:hover {
  color: #d9534f;
}

.new{
    height: 700px;
    background:ghostwhite;
    margin-top: 10px;
    width: 100% ;
    /* margin-left: 5%; */
}
.title{
    font-size: 25px;
	line-height: 60px;
	color: black;
	margin-left: -1150px;
}
.course{
    width: 90%;
    margin-left: 5%;
}
.course-card{
    width: 330px;
    height: 300px;
    /* background: #d9534f; */
    margin-left: 10px;
    float: left;
} 
.course-image img{
    height: 180px;
    border-radius: 5%
}  
.course-lable{
    float: left;
    margin-top: -100px;
}
.course-title{
    font-size: 15px;
    font-weight: 900;
    text-align: left;
}
.course-span{
    float: left;
    font-size: 15px;
    color: #ccc;
}
.course-price{
    float: right;
}


</style>