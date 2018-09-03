<template>
    <div class="location">
        <div class="swiper-pagination"  slot="pagination"></div>
        <h1 class="location__city">{{cityStr}}</h1>
        <h1 class="location__name">{{nameStr}}</h1>
        <img class="location__icon" src="../assets/icon_pin.svg" alt="">
    </div>  
</template>

<script>
    export default {
        props: ['pageIndex'],
        data() {
            var pageIndex = this.pageIndex;
            var citys = ['新北市', '屏東縣', '新北市'];
            var names = [ '白沙灣', '墾丁海水浴場', '福隆海水浴場'];

            return {
                cityStr: citys[pageIndex],
                nameStr: names[pageIndex]
            }
        }
    }
</script>

<style lang="scss">
    .location {
        text-align: center;
        margin-top: 40px;

        .location__icon {
            width: 30px;
            margin: 5px auto 0;
        }

        .location__city{
            font-size: 20px;
            line-height: 30px;
        }

        .location__name  {
            font-size: 30px;
            line-height: 40px;
        }
    }
</style>
