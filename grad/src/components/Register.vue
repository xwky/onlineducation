<template>
<div class="login">
    <div class="login-image">
        <img src="static/image/login.jpg"/>
    </div>
    <div class="form">
        <el-form :model="formData" ref="formData" :rules="rulelines" >
            <el-form-item prop="phone">
                <el-input v-model="formData.phone" placeholder="请输入手机号" @input="change($event)"></el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input type="password" v-model="formData.password" placeholder="请输入密码"></el-input>
            </el-form-item>
            <el-form-item prop="repassword">
                <el-input type="password" v-model="formData.repassword" placeholder="请确认密码"></el-input>
            </el-form-item>
            <button class="button" @click="handSubmit()">注册</button>
            <!-- <p>已有账户？立即登录</!--> 
        </el-form>
    </div>

</div>
    
</template>

<script>
import store from '@/vuex/store';
import {mapMutations,mapActions} from 'vuex';
import qs from 'qs';
export default {
   data(){
       const validPassword = (rule,value,callback) => {
           if (value === ''){
               callback(new Error('请输入密码'));
           } else if(value !== this.formData.password){
               callback(new Error('两次输入的密码不一致'));
           } else{
               callback();
           }
       };
       return {
           formData:{
               phone:'',
               password:'',
               repassword:''
           },
           rulelines:{
               password: [{
            required: true,
            message: '密码不能为空',
            trigger: 'blur'
          },
          {type:'string', min:4,message:'密码长度不能少于四位',trigger:'blur'}],
          phone: [{
              required: true,
              message: '手机号不能为空',
              trigger: 'blur'
            },

          { type: 'string', pattern: /^1[3|4|5|7|8][0-9]{9}$/, message: '手机号格式出错', trigger: 'blur' }

          ],
          repassword: [{
            required:true,
            validator: validPassword,
            trigger: 'blur'
          }]
           }
       }
   },
   methods:{
    //    ...mapActions(['addSignUpUser']),
       change(e){
           this.$forceUpdate()
       },
       handSubmit:function() {
           const  params = {
               username : this.formData.phone,
               password : this.formData.password,
               password2:this.formData.repassword
           };
           if (this.formData.password !== '' && this.formData.repassword !== '' && this.formData.phone !== ''){
               if (this.formData.password === this.formData.repassword){
               this.axios.post('http://127.0.0.1:8000/api/user/login/login/',
              {...params}
               ).then(response => {
                   console.log(response);
                   if (response.status === 200){
                       const data = response.data;
                       console.log(data);
                    //    this.addSignUpUser(params);
                    //    console.log('7',params)
                       if (data.msg === '注册成功'){                           
                        //    alert('注册成功，请登录')
                        //    this.$router.push({path:'/Login'});
                           this.$Message.success('注册成功，请登录');
                        this.$router.push('/Login');
                        window.location.reload();
                       }
                       if (data.msg === '该用户已经存在'){
                           alert('用户已存在');
                                     }
                   }
                   
                                });
                } else{
                    alert('密码不一致，请重试')
           }
           } else{
               alert('用户名和密码不能为空，请重试')
           }
           
           
       }
   },
   store
};
    
    

</script>

<style>
.login{
    width: 100%;
    height: 500px;
    background: white;
}
.login-image{
    float: left;
    margin-top: 40px;   
}
.login-image img{
    /* 圆角矩形 */
    border-radius: 5%;
}
.form {
    float: left;
    width: 30%;
    height: 400px;
    margin: 40px 100px;
    border: black solid;
    background: whitesmoke;
    border-radius: 5%;
    padding: 50px;
    
  }
  .button{
      width: 100%;
      background:#AAE7FC;
      font-size: 30px;
      border-radius: 5%;
      border:#AAE7FC;
      cursor: pointer;
      margin-top: 50px;
  }
  .button:hover {background-color:#2096D4}
</style>