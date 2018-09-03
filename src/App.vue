<!-- The ref attr used to find the swiper instance -->
<template>
  <div class="sea-more sea-more--sun">
      <div class="md-subhead">
        <Header />
      </div>
      <swiper :options="swiperOption" ref="mySwiper">
      <!-- slides -->
      <swiper-slide><Pages pageIndex="0"/></swiper-slide>
      <swiper-slide><Pages pageIndex="1"/></swiper-slide>
      <swiper-slide><Pages pageIndex="2"/></swiper-slide>
      <!-- Optional controls -->
      <div class="space-man">
          <div class="chat">太陽很大喔～建議中午時段不要曝曬超過30分鐘！</div>
          <img src="/src/assets/spaceman.svg">
      </div>
    </swiper>
  </div>
</template>

<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper';
import Header from './components/Header.vue';
import Pages from './components/Pages.vue';
export default {
  data() {
    return {
      swiperOption: {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        onTransitionStart(swiper){
          var bgColor = ['sun', 'rain', 'dusk'],
          app = document.querySelector('.sea-more');
          app.className = 'sea-more';
          app.classList.add('sea-more--' + bgColor[swiper.activeIndex]);
          var time = ['2017/4/30 上午 9 點', '2017/5/1 下午 12 點', '2017/5/1 下午 6 點'],
          appTime = document.querySelector('.header__time__name');
          appTime.innerText = time[swiper.activeIndex];
        }
      }
    }
  },
  components: {
    swiper,
    swiperSlide,
    Header,
    Pages
  }
}
</script>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.swiper-pagination {
  width: 100%;
  margin-top: -35px;
}

.swiper-pagination-bullet {
  margin-right: 5px;
}
.swiper-pagination-bullet-active {
    background-color: rgba(255,255,255,.9) !important;
}

.sea-more {
  font-family: Quicksand, Helvetica, Arial, sans-serif;
  width: 375px;
  height: auto;
  margin-top: 20px;
  color: white;
  line-height: 18px;
  letter-spacing: 1px;
  box-sizing: border-box;
  position: relative;
  left: 50%;
  transform: translateX(-50%);

  &.sea-more--sun {
    background: #00C9FF;  /* fallback for old browsers */
    background: -webkit-linear-gradient(to bottom, #00C9FF, #92FE9D);  /* Chrome 10-25, Safari 5.1-6 */
    background: linear-gradient(to bottom, #00C9FF, #92FE9D); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }

  &.sea-more--rain {
      background: #859398;  /* fallback for old browsers */
      background: -webkit-linear-gradient(to bottom, #859398, #283048);  /* Chrome 10-25, Safari 5.1-6 */
      background: linear-gradient(to bottom, #859398, #283048); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }

  &.sea-more--dusk {
      background: #FF5F6D;  /* fallback for old browsers */
      background: -webkit-linear-gradient(to bottom, #FF5F6D, #FFC371);  /* Chrome 10-25, Safari 5.1-6 */
      background: linear-gradient(to bottom, #FF5F6D, #FFC371); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  }
}

h1, h2 {
  font-weight: normal;
  text-align: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}

img {
  width: 200px;
  margin: 0 auto;
  display: block;
}

// reset css
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
	margin: 0;
	padding: 0;
	border: 0;
	font-size: 100%;
	font: inherit;
	vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
	display: block;
}
body {
	line-height: 1;
}
ol, ul {
	list-style: none;
}
blockquote, q {
	quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
	content: '';
	content: none;
}
table {
	border-collapse: collapse;
	border-spacing: 0;
}
.swiper-slide {
    height: 600px !important;
    overflow-y: scroll;
}
.space-man {
    background-color: rgba(0,0,0,.2);
    width: 100%;
    height: 100px;
    position: fixed;
    bottom: -100px;
    z-index: 30;
    display: flex;
    transition: all 0.6s;
}
.space-man .chat {
    width: calc(100% - 100px);
    margin: 20px 10px 20px 20px;
    background-color: #fff;
    color: #576372;
    border-radius: 10px;
    padding: 10px;
}
.space-man img {
    width: 100px;
    height: 100px;
}
</style>
