<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <Header></Header>
    <router-view v-if="isRouterAlive"/>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/header/Header';
import Footer from '@/components/foot/Footer';

export default {
  name: 'App',
  provide(){
    return{
      reload:this.reload
    }
  },
  data(){
    return{
      isRouterAlive:true
    }
  },
  components:{
    Header,
    Footer,
  },
  methods:{
    reload(){
      this.isRouterAlive = false
      this.$nextTick(function(){
        this.isRouterAlive = true
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
