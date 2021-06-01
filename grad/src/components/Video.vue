<template>
<div class="video">
    <div class="video_detail">
        <video-player class="vjs-custom-skin" :options="playerOptions"></video-player>
    </div>

</div>
    
</template>

<script>
// import 'video.js/dist/video-js.css'
// import 'vue-video-player/src/custom-theme.css'
//   //引入hls.js
// import 'videojs-contrib-hls.js/src/videojs.hlsjs'
export default {
    data () {
      return {
        playerOptions: {
         playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
        autoplay: false, //如果true,浏览器准备好时开始回放。
        muted: false, // 默认情况下将会消除任何音频。
        loop: false, // 导致视频一结束就重新开始。
        preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
        language: 'zh-CN',
        aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
        fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
        sources: [{
          type: "",
          src: "https://vdept.bdstatic.com/634d74574e4655616b636e785a706e7a/33554d36354d6356/c0e3a25be2457bf5fe193840916222ba0581eaf0a87d64c35027f081189ac4d5c7aa4a9f142d933b3d0c129dbc916281.mp4?auth_key=1589339986-0-0-32a70d71c6e18ffb047d16a15584c556" //url地址
        }],
        // poster: "../../static/images/test.jpg", //你的封面地址
        // width: document.documentElement.clientWidth,
        notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
        controlBar: {
          timeDivider: true,
          durationDisplay: true,
          remainingTimeDisplay: false,
          fullscreenToggle: true  //全屏按钮
        }
        }
      }
    }
}
</script>

<style>
.video{
    width: 90%;
    height: 700px;
    /* background: antiquewhite; */
    margin-left: 5%;
}
.video_detail{
    width: 90%;
    background: aqua;
    height: 600px;
    margin-left: 5%;
}
.video-js .vjs-big-play-button{}

</style>