<template>
<div class="register">
    <div class="register-image">
        <img src="static/image/register1.jpg"/>
    </div>
    <div class="form">
        <!-- <div class="title">
            <p>欢迎登录</p>
        </div> -->
        <div class="regist">
            <el-form ref="formInline" :model="formData" :rules="ruleInline">
            <el-form-item>
                <p>欢迎登录</p>
            </el-form-item>
              <el-form-item prop="username">
                  <el-input type="text" v-model="formData.username" clearable size="large" placeholder="用户名">
                      <!-- <span class="iconfont icon-ren1"></span> -->
                  </el-input>
              </el-form-item>
              <el-form-item prop="password">
                  <el-input type="password" v-model="formData.password" clearable size="large" placeholder="密码">
                      <!-- <Icon type="ios-locked-outline" slot="prepend"> </Icon> -->
                  </el-input>
              </el-form-item>
              <el-form-item>
                  <Button class="button" size="large" @click="handleSubmit()" long>登录</Button>
              </el-form-item>
          </el-form>
        </div>
    </div>
</div>
    
</template>

<script>
import store from '@/vuex/store';
import { mapMutations, mapActions } from 'vuex';
import qs from 'qs' ;
export default {
    // name: 'Register',
    data(){
        return {
      formData: {
        username: '',
        password: ''
      },
      ruleInline: {
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
          { type: 'string', min: 6, message: '密码不能少于6位', trigger: 'blur' }
        ]
      }
    };
    },
    methods:{
        ...mapMutations(['SET_USER_LOGIN_INFO']),
        ...mapActions(['login']),
        handleSubmit:function(){
            const params = {
                username : this.formData.username,
                password:this.formData.password
            };
            this.login(this.formData);
            
            console.log('3',this.formData);
            console.log('=============');
            console.log(localStorage.getItem('users'));
            
            console.log('===========');
            this.axios.post('http://127.0.0.1:8000/api/user/register/register/',
            {...params}).then(response =>{
                console.log(response);
                if (response.status === 200){
                    const data = response.data;
                    console.log('data',data);
                    localStorage.setItem('userid',data.user_id)
                    if (data.msg === '登录成功'){
                        console.log(localStorage.getItem('username'));
                        console.log(localStorage.getItem('userInfo'))
                        this.$Message.success('登录成功');
                        this.$router.push('/');
                        window.location.reload();
                    } else{
                        this.$Message.error('用户名或密码错误');
                    }
                }
            });
        }
    },
    store
    
}
</script>

<style>
.register{
    width: 100%;
    height: 500px;
    background: white;
}
.register-image{
    float: left;
    margin-top: 40px;
}
.register-image img{
     border-radius: 5%
}

.form {
    float: left;
    width: 30%;
    height: 320px;
    margin: 5% 160px;
    border: black solid;
    background: whitesmoke;
    /* border-radius: 5%; */
    /* padding: 10px; */
}
/* .title{
    color: #fff;
    background-color: #70A5C5;
    font-size: 30px;
    font-weight: 500;
    margin-top: -25px;
    width: 100%;
    float: left;
    border-radius: 5%;
} */
.regist{
    padding: 10px;
}
.button{
      background:#AAE7FC;
      font-size: 25px;
      /* border-radius: 10%; */
      border:#AAE7FC;
      cursor: pointer;
  }
.button:hover {background-color:#2096D4}

</style>