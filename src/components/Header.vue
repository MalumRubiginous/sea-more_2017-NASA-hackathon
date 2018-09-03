<template>
    <header class="header">
        <img class="header-icon header__setting" src="../assets/icon_setting.svg" alt="">
        <div class="header__time">
            <div>
                <img class="header-icon header-icon--arrow" src="../assets/icon_back.svg" alt="">
                <p class="header__time__name">2017/4/30 上午 9 點</p>
                <img class="header-icon header-icon--arrow" src="../assets/icon_next.svg" alt="">
            </div>
        </div>
        <img class="header-icon header__pin" src="../assets/icon_pin_plus.svg" alt="">
    </header>  
</template>

<script>
    
</script>

<style lang="scss">
    .header {
        padding: 10px;
        text-align: center;

        .header-icon {
            width: 20px;
            height: 20px;
            display: inline-block;
            vertical-align: bottom;
            cursor: pointer;

            &.header-icon--arrow {
                width: 15px;
                height: 15px;
            }
        }

        .header__setting {
            position: fixed;
            left: 10px;
        }

        .header__pin {
            position: fixed;
            right: 10px;
        }

        .header__time, .header__time__name {
            display: inline-block;
            cursor: pointer;
            text-align: center;
        }
    }
</style>
