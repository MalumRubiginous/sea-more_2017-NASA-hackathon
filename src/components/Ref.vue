<template>
    <div>
    <div class="ref">
        <h3 class="ref__title">人氣美食</h3>
        <article class="ref__article" v-for="food in foods">
            <div  class="ref__article__cover"><img class="ref__article__img" :src="food.coverImg" alt=""></div>
            <p class="ref__article__title">{{food.title}}</p>
        </article>
    </div>
    <div class="ref">
        <h3 class="ref__title">約會聖地</h3>
        <article class="ref__article" v-for="like in likes">
            <div  class="ref__article__cover"><img class="ref__article__img" :src="like.coverImg" alt=""></div>
            <p class="ref__article__title">{{like.title}}</p>
        </article>
    </div>
    <div class="ref">
        <h3 class="ref__title">防曬彩妝</h3>
        <article class="ref__article" v-for="ref in refs">
            <div  class="ref__article__cover"><img class="ref__article__img" :src="ref.coverImg" alt=""></div>
            <p class="ref__article__title">{{ref.title}}</p>
        </article>
    </div>
    </div>
</template>

<script>

export default {
    data () {
        return {
            likes: [
                {
                    coverImg: 'https://pic.pimg.tw/janewang0125/1449156969-3125167786_n.jpg',
                    title: '就是要放閃！夏天就是來白沙灣海水浴場玩水'
                },{
                    coverImg: 'https://pic.pimg.tw/babytina0709/1469889311-3835770872.jpg',
                    title: '♥新北半日游♥浪漫北海岸石門～白水灣沙灘/戲水/咖啡聽'
                }
            ],
            refs: [
                {
                    coverImg: 'https://pic.pimg.tw/izzychou/1469519688-633713788_n.jpg?v=1469520043',
                    title: '每到夏天我要去海邊♥我的海灘化妝包分享♥海邊補妝不可不知的tips'
                },
                {
                    coverImg: 'https://pic.pimg.tw/miihuang/1405508283-3780237105.jpg',
                    title: '【美妝】夏日限定♥♥到海邊也不用擔心的快速底妝教學'
                }
            ],
            foods: [
                {
                    coverImg: 'https://pic.pimg.tw/beautychu060/1431092720-4014355429_n.jpg',
                    title: '墾丁美食‧南灣地中海料理【迷路小章魚】、好吃【橘子早餐】、泰緬料理【弄海】、墾丁大街'
                },
                {
                    coverImg: 'https://pic.pimg.tw/wkitty/1470804327-406507553.jpg',
                    title: '墾丁大街必吃美食小吃14攤'
                }
            ]
        }
    }
}

</script>

<style lang="scss">
    .ref {
        margin-top: 30px;
        text-align: center;
    }

    .ref__title {
        margin-bottom: 20px;
    }

    .ref__article {
        width: 300px;
        height: auto;
        margin: 0 auto 10px;
        padding: 10px 0px;
        border-radius: 5px;
        background-color: white;
        text-align: center;

        &:last-child {
            margin-bottom: 50px;
        }

        .ref__article__cover {
            width: 280px;
            height: 100px;
            margin: 0 auto;
            overflow: hidden;
        }

        .ref__article__img {
            width: 280px;
            height: auto;
        }

        .ref__article__title {
            width: 280px;
            padding: 10px;
            text-align: left;
            font-size: 14px;
            color: black;
        }
    }

</style>
