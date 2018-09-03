# sea-more-hackathon

> NASA hackathon with Vue.js project

***

## 簡介
### Sea-More！

![](https://github.com/AnnaSu/sea-more-hackathon/blob/master/demo_gif_files/demo1%20-%20change%20Pages.gif?raw=true)

```
讓你看見更多海灘資訊！
提供你海灘天氣和海洋資訊，貼心的外出建議和推薦文章參考，享受海岸更輕鬆！
```

> 海洋與人之間的互動See More !! 給你更多連結環境資訊

- 海灘資訊 - 整合氣象局的資料
- 結合痞客邦搜尋及大數據系統，尋找各海灘的相關文章
- 紫外線估測 - 利用估算的公式，獲得白天的紫外線
- 水母偵測 - 利用海水溫度來預測是否會出現水母
- 整合機器人服務 - 利用 NLP 技術，來作人工智慧應答機器人，來更貼近使用者



***

## API 資訊
### 基礎天氣資訊

```
  input:
    地點(海灘編號或海灘字串),
    時間(日期與小時)
  output:
    未來36小時的氣溫,
    未來36小時的天氣型態(for切換天氣icon)
```

### 指標資訊

```
  input:
    地點(海灘編號或海灘字串),
    時間(日期與小時)
  output:
    浪高(公尺或描述文字)
    風速(節或描述文字-蒲福風級-)
    紫外線(量級),
    潮汐(漲潮/乾潮),
    降雨機率(%),
    威脅或海溫
```

### 海灘資訊

```
  output:
    海灘列表
        海灘地區,
        海灘名稱,
        海灘類型,
        海灘編號: 供回傳查表轉換經緯度用
```

### 個人建議

```
  input:
    地點(海灘編號或海灘字串),
    時間(日期與小時),
    個人資訊(性別, 是否下水, 有沒有小朋友)
  output: (根據紫外線, 海浪, 威脅程度, 地點設施, 天氣型態和氣溫來判斷)
    攜帶物品
        水壺
        傘
        防曬油
        太陽眼鏡
        防曬帽子
        禦寒帽子
        玩沙工具
        毛巾
        衝浪板
    穿著
        泳衣/泳褲
        t-shirt
        防曬薄外套
        禦寒厚外套

```

### 文章推薦

```
  input:
    地點(海灘編號或海灘字串)
  output:
    推薦文章列表
    縮圖(圖片網址)
    文章標題(字串)
    文章內文一些擷取 <- optional
```

***
## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build
```

***