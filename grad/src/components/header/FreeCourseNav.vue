<template>
    <div class="free">
        <div class="title">          
            <div class="font">
                《 基础课程 》
            </div>
            <div class="line">      </div>
            <div class="tag">
                <div class="taginfo" v-for="(item,index) in tagsInfo" :key="index">
                    <div class="tagname">{{item.tagName}}：</div>
                    <div class="list_ul" v-for="(item,subindex) in item.tag" :key="subindex">
                        <div class="list_li" @click="change"><router-link  :to="{path:'/CourseListSelect/',query:{tag:item}}">{{item}}</router-link></div>
                    </div> 
                </div>                    
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            tagsInfo:[
                {
                    tagName:'分类',
                    tag:['java','python','计算机基础','c','前端']
                }
            ]
        }
    }
    
}
</script>

<style>
.free{
    width: 100%;
    height: 200px;
    background:white;
}
.title{
    width: 100%;
    /* height: 100px; */
    background: white;
}
.font{
    float: left;
    font-size: 25px;
    padding-top: 15px;
    padding-left: 10px;
}
.line{
    width: 100%;
    height: 2px;
    background: rgba(230, 229, 225, 0.952);
    float: left;
    margin-top: 10px;
}
.tag{
    width: 100%;
    height: 190px;
    float: left;
    margin-top: 20px;
}
.taginfo{
    font-size: 25px;
}
.tagname{
    float: left;  
}
.list_ul{
    float: left;
    padding-left: 20px;
    color: black;
}
.list_li{
    font-size: 25px;
}
a:hover{
    color: orange;
}
a:active{
    color: red;
}
a{
    color: black;
}
</style>