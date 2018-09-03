<template>
    <div class="suggestion">
        <h3 class="suggestion__title">外出建議</h3>
        <ul class="suggestion__lists">
            <li class="suggestion__list" v-for="suggestion in suggestions">
                <div class="suggestion__list__bg">
                    <img class="suggestion__list__icon" :src="suggestion.iconUrl" alt="">
                </div>
            </li>
        </ul>
    </div>  
</template>

<script>

export default {
    props: ['pageIndex'],
    data () {
        var pageIndex = this.pageIndex;
        var suggestions = [];
        suggestions[0] = [
            {   
                name: '比基尼',
                iconUrl: './src/assets/icon_bikini.svg'
            },
            {   
                name: '太陽眼鏡',
                iconUrl: './src/assets/icon_glass.svg'
            },
            {   
                name: '草帽',
                iconUrl: './src/assets/icon_hat.svg'
            },
            {   
                name: '乳液',
                iconUrl: './src/assets/icon_lotion.svg'
            }
        ]
        suggestions[1] = [
            {   
                name: '雨傘',
                iconUrl: './src/assets/icon_umbrella.svg'
            },
            {   
                name: '短褲',
                iconUrl: './src/assets/icon_pant.svg'
            }
        ]
        suggestions[2] = [
            {   
                name: '乳液',
                iconUrl: './src/assets/icon_lotion.svg'
            },
            {   
                name: '草帽',
                iconUrl: './src/assets/icon_glass.svg'
            }
        ]

        return {
            suggestions: suggestions[pageIndex]
        }
    }
}
    
</script>

<style lang="scss">
    .suggestion {
        margin-top: 30px;
        text-align: center;
    }

    .suggestion__title {
        margin-bottom: 20px;
    }

    .suggestion__lists {
        .suggestion__list {
            display: inline-block;
            margin-right: 20px;
            margin-bottom: 10px;

            &:nth-child(4n) {
                margin-right: 0;
            }

            .suggestion__list__bg {
                width: 40px;
                height: 40px;
                padding: 10px;
                border-radius: 50%;
                background-color: white;
                box-shadow: 1px 1px 20px rgba(20%,20%,40%,0.5);
            }

            .suggestion__list__icon {
                width: 40px;
                height: 40px;
            }
        }
    }
</style>
