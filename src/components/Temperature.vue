<template>
    <div class="temperature">
        <div class="temperature__info">
            <img class="temperature__info__icon" :src="weatherType" alt="">
            <p class="temperature__info__number">{{ tempStr }}</p>
            <div class="temperature__info__chart"></div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'non-vue-line-chart',
  template: '<div></div>',
  props: ['pageIndex'],
  data () {
    var pageIndex = this.pageIndex;
    var temp = ['氣溫 23°', '氣溫 27°', '氣溫 23°'];
    var weatherType = ["/src/assets/icon_sun.svg", "/src/assets/icon_cloud.svg", "/src/assets/icon_rain.svg"];
    return {
      tempStr: temp[pageIndex],
      weatherType: weatherType[pageIndex]
    }
  },
  mounted() {
    var pageIndex = this.pageIndex,
        charts = document.querySelectorAll('.temperature__info__chart');

    for(var i = 0; i < charts.length; i++){
        charts[i].classList.add('chart-'+i);
    }

    function create(target, config, data, color) {
        var line = d3.line()
            .x(config.line.x)
            .y(config.line.y);

        var axis = {
            x1: d3.axisBottom()
                .scale(config.scale.x)
                .ticks(config.ticks.x)
                .tickFormat(config.ticksFormat),
            x2: d3.axisBottom()
                .scale(config.scale.x)
                .ticks(config.ticks.x)
                .tickFormat(config.ticksFormat),
            y: d3.axisLeft()
                .scale(config.scale.y)
                .ticks(config.ticks.y)
        };

        target
            .append('g')
                .attr('class', 'axis x temp')
                .call(axis.x1)
                .attr('transform',`translate(0, ${config.height})`)
            .selectAll('text')
                .text((d,i)=>{return data[i].count + '°';})
                .attr('y', 15)
                .attr('x', 0);

        target
            .append('g')
                .attr('class', 'axis x time')
                .call(axis.x2)
                .attr('transform',`translate(0, 0)`)
            .selectAll('text')
                .attr('y', -20)
                .attr('x', 0);

        target
            .append('g')
                .attr('class', 'axis y')
                .call(axis.y);

        target
            .append('path')
                .attr('class', 'line')
                .attr('d', line(data))
                .attr('stroke', color);

        target.append('g').selectAll("circle").data(data)
            .enter()
            .append("circle")
                .attr('class', 'line-dot')
                .attr('cx', config.points.cx)
                .attr('cy', config.points.cy)
                .attr('fill', color);
    }

    function init(){
        var margin = {top: 25, right: 30, bottom: 35, left: 30},
            width = 720 - margin.left - margin.right, // svgWidth - margin.left - margin.right
            height = 100 - margin.top - margin.bottom; // svgHeight - margin.top - margin.bottom

        var svg = d3.select('.temperature__info__chart.chart-'+pageIndex).append('svg')
            .attr('width', width + margin.left + margin.right)
            .attr('height', height + margin.top + margin.bottom);

        // 產生一個四周有 maring 的 <g> 將內容物包起來，調整置中
        var container = svg.append('g')
            .attr('transform', `translate(${margin.left}, ${margin.top})`)

        var timeformat = d3.timeFormat('%H:00');

        var mainData = [[
            { date: new Date(2017, 3, 30, 9), count: 23 },
            { date: new Date(2017, 3, 30, 12), count: 24 },
            { date: new Date(2017, 3, 30, 15), count: 25 },
            { date: new Date(2017, 3, 30, 18), count: 26 },
            { date: new Date(2017, 3, 30, 21),  count: 22 },
            { date: new Date(2017, 4, 1, 0),  count: 20 },
            { date: new Date(2017, 4, 1, 3), count: 19 },
            { date: new Date(2017, 4, 1, 6), count: 19 },
            { date: new Date(2017, 4, 1, 9), count: 26 },
            { date: new Date(2017, 4, 1, 12), count: 26 },
            { date: new Date(2017, 4, 1, 15), count: 25 },
            { date: new Date(2017, 4, 1, 18), count: 23 }
        ],[
            { date: new Date(2017, 3, 30, 9), count: 27 },
            { date: new Date(2017, 3, 30, 12), count: 30 },
            { date: new Date(2017, 3, 30, 15), count: 30 },
            { date: new Date(2017, 3, 30, 18), count: 26 },
            { date: new Date(2017, 3, 30, 21),  count: 25 },
            { date: new Date(2017, 4, 1, 0),  count: 24 },
            { date: new Date(2017, 4, 1, 3), count: 24 },
            { date: new Date(2017, 4, 1, 6), count: 24 },
            { date: new Date(2017, 4, 1, 9), count: 30 },
            { date: new Date(2017, 4, 1, 12), count: 32 },
            { date: new Date(2017, 4, 1, 15), count: 32 },
            { date: new Date(2017, 4, 1, 18), count: 28 }
        ],[
            { date: new Date(2017, 3, 30, 9), count: 23 },
            { date: new Date(2017, 3, 30, 12), count: 26 },
            { date: new Date(2017, 3, 30, 15), count: 25 },
            { date: new Date(2017, 3, 30, 18), count: 26 },
            { date: new Date(2017, 3, 30, 21),  count: 21 },
            { date: new Date(2017, 4, 1, 0),  count: 20 },
            { date: new Date(2017, 4, 1, 3), count: 20 },
            { date: new Date(2017, 4, 1, 6), count: 19 },
            { date: new Date(2017, 4, 1, 9), count: 25 },
            { date: new Date(2017, 4, 1, 12), count: 26 },
            { date: new Date(2017, 4, 1, 15), count: 25 },
            { date: new Date(2017, 4, 1, 18), count: 23 }
        ]];


        var config = {
            margin: margin,
            width: width,
            height: height,
            scale: {
                x: d3.scaleTime()
                    .domain([mainData[pageIndex][0].date, mainData[pageIndex][mainData[pageIndex].length-1].date])
                    .range([0, width]),
                y: d3.scaleLinear()
                    .domain([
                        d3.min(mainData[pageIndex], function(d) { return d.count; }),
                        d3.max(mainData[pageIndex], function(d) { return d.count; })
                    ])
                    .range([height, 0])
                    .nice()
            },
            ticks: { x: 12, y: 3 },
            ticksFormat: function(d, i){
                return i === 0 ? '現在' : timeformat(d);
            },
            ticksTextSetting: function(selector){
              selector
                  .attr('y', -10)
                  .attr('x', 0);
            },
            line: {
                x: function(d, i){return config.scale.x(mainData[pageIndex][i].date)},
                y: function(d){return config.scale.y(d.count)}
            },
            points: {
                cx: function(d, i) {return config.scale.x(mainData[pageIndex][i].date)},
                cy: function(d) {return config.scale.y(d.count);}
            },
            format: {
                x: d3.timeFormat('%m/%d'),
                y: d3.format(',')
            }
        };

        create(container, config, mainData[pageIndex], '#fff');
    };
    init();
  }
}
</script>

<style>
.temperature {
    margin-top: 50px;
    text-align: center;
}
.temperature__info__icon {
    width: 20px;
    height: 20px;
    display: inline-block;
    vertical-align: bottom;
    cursor: pointer;
}
.temperature__info, .temperature__info__number {
    display: inline-block;
    cursor: pointer;
    text-align: center;
}
.temperature__info__chart {
    margin-top: 33px;
    overflow-x: scroll;
    overflow-y: hidden;
    width: 375px;
}
.axis path,
.axis line {
    fill: none;
    stroke: black;
}
.axis.y > path,
.axis.x > path,
.axis.y .tick,
.tick line {
  display: none;
}

.tick text{
    fill: #fff;
    stroke: none;
}
.temp {
   font-size: 14px;
}
.time {
    font-size: 12px;
}

.line {
  stroke-width: 2;
  fill: none;
}
.line-dot {
  r: 4;
}
</style>
