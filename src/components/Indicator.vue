<template>
    <div class="indicator-container">
        <div class="indicator-row">
            <div v-for="(item, index) in indicatorsRow1" :class="item.className">
                <div class="name">{{ item.name }}</div>
                <img class="icon" :src="item.icon" />
                <div class="value">{{ item.value }}</div>
            </div>
        </div>
        <div class="indicator-row">
            <div v-for="(item, index) in indicatorsRow2" :class="item.className">
                <div class="name">{{ item.name }}</div>
                <img class="icon" :src="item.icon" />
                <div class="value">{{ item.value }}</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'indicator',
  props: ['pageIndex'],
  data () {
    var row1 = [[
            {
                className: 'indicator-item rainfall',
                name: '降雨機率',
                icon: '/src/assets/icon_umbrella.svg',
                value: '10%'
            },
            {
                className: 'indicator-item uv',
                name: '紫外線',
                icon: '/src/assets/icon_uv.svg',
                value: '中量'
            },
            {
                className: 'indicator-item temperature-diff',
                name: '海水溫度',
                icon: '/src/assets/icon_temp.svg',
                value: '22°'
            }
        ],[
            {
                className: 'indicator-item rainfall',
                name: '降雨機率',
                icon: '/src/assets/icon_umbrella.svg',
                value: '20%'
            },
            {
                className: 'indicator-item uv',
                name: '紫外線',
                icon: '/src/assets/icon_uv.svg',
                value: '中量'
            },
            {
                className: 'indicator-item temperature-diff',
                name: '海水溫度',
                icon: '/src/assets/icon_temp.svg',
                value: '28°'
            }
        ],[
            {
                className: 'indicator-item rainfall',
                name: '降雨機率',
                icon: '/src/assets/icon_umbrella.svg',
                value: '10%'
            },
            {
                className: 'indicator-item uv',
                name: '紫外線',
                icon: '/src/assets/icon_uv.svg',
                value: '中量'
            },
            {
                className: 'indicator-item temperature-diff',
                name: '海水溫度',
                icon: '/src/assets/icon_temp.svg',
                value: '22°'
            }
        ]];
    var row2 = [[
            {
                className: 'indicator-item tidal',
                name: '潮汐',
                icon: '/src/assets/icon_tidal.svg',
                value: '退潮'
            },
            {
                className: 'indicator-item wave-height',
                name: '浪高',
                icon: '/src/assets/icon_wave.svg',
                value: '1m'
            },
            {
                className: 'indicator-item wind',
                name: '風速',
                icon: '/src/assets/icon_wind.svg',
                value: '1km/hr'
            }
        ],[
            {
                className: 'indicator-item tidal',
                name: '潮汐',
                icon: '/src/assets/icon_tidal.svg',
                value: '退潮'
            },
            {
                className: 'indicator-item wave-height',
                name: '浪高',
                icon: '/src/assets/icon_wave.svg',
                value: '0.56m'
            },
            {
                className: 'indicator-item wind',
                name: '風速',
                icon: '/src/assets/icon_wind.svg',
                value: '1km/hr'
            }
        ],[
            {
                className: 'indicator-item tidal',
                name: '潮汐',
                icon: '/src/assets/icon_tidal.svg',
                value: '退潮'
            },
            {
                className: 'indicator-item wave-height',
                name: '浪高',
                icon: '/src/assets/icon_wave.svg',
                value: '1m'
            },
            {
                className: 'indicator-item wind',
                name: '風速',
                icon: '/src/assets/icon_wind.svg',
                value: '1km/hr'
            }
        ]];
    var pageIndex = this.pageIndex;
    return {
        indicatorsRow1: row1[pageIndex],
        indicatorsRow2: row2[pageIndex]
    }
  }
}
</script>

<style lang="css">
.indicator-container {
    margin-top: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
.indicator-row {
    display: flex;
    position: relative;
}
.indicator-row:nth-child(1)::after {
    content: "";
    position: absolute;
    left: 10px;
    bottom: 0px;
    width: 280px;
    height: 1px;
    background-color: #485F79;
    opacity: .7;
}

.indicator-row:nth-child(1) .indicator-item:nth-child(1) {
  border-radius: 10px 0 0 0;
}
.indicator-row:nth-child(1) .indicator-item:nth-child(3) {
  border-radius: 0 10px 0 0;
}
.indicator-row:nth-child(2) .indicator-item:nth-child(1) {
  border-radius: 0 0 0 10px;
}
.indicator-row:nth-child(2) .indicator-item:nth-child(3) {
  border-radius: 0 0 10px 0;
}

.indicator-item {
    color: #485F79;
    width: 100px;
    height: 100px;
    background: rgba(255,255,255,.8);
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}
.indicator-item > .name {
    opacity: .7;
    font-size: 12px;
    line-height: 1;
}
.indicator-item > .value {
    font-size: 14px;
    line-height: 1;
}
.indicator-item > .icon {
    width: 30px;
    height: 30px;
    margin: 9px 0 12px 0;
}
</style>
