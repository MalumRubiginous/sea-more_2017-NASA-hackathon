var builder = require('botbuilder');
var restify = require('restify');
var builder = require('botbuilder');
var fs = require('fs');
var request = require('request');
var escape = require('escape-html');



var https_options = {
  key: fs.readFileSync('/etc/letsencrypt/live/ticket51750.pixnet.co/privkey.pem'),
  certificate: fs.readFileSync('/etc/letsencrypt/live/ticket51750.pixnet.co/fullchain.pem')
};


// Setup Restify Server
var server = restify.createServer(https_options);
server.listen(process.env.port || process.env.PORT || 8081, function () {
    console.log('%s listening to %s', server.name, server.url);
});

// Create chat bot
var connector = new builder.ChatConnector({
    appId:'',//process.env.MICROSOFT_APP_ID,
    appPassword: ''//process.env.MICROSOFT_APP_PASSWORD
});

var bot = new builder.UniversalBot(connector);
server.post('/api/messages', connector.listen());


// Create LUIS recognizer that points at our model and add it as the root '/' dialog for our Cortana Bot.
var model = 'https://westus.api.cognitive.microsoft.com/luis/v2.0/apps/9d406472-ead2-47f2-8738-c25de71f6e08?subscription-key=KEY&timezoneOffset=0.0&verbose=true&q=';

// You can provide your own model by specifing the 'LUIS_MODEL_URL' environment variable
// This Url can be obtained by uploading or creating your model from the LUIS portal: https://www.luis.ai/
var recognizer = new builder.LuisRecognizer(model);
bot.recognizer(recognizer);

bot.dialog('/', [
    function (session, args, next) {
        session.beginDialog('/sayhi');
    }
]);

bot.dialog('/sayhi',
    [
        function (session, next) {
            builder.Prompts.text(session, '哈摟，我是 sea more 的小管家，請問你叫什麼名字？');
        },
        function (session, results, next) {
            session.userData.name = results.response;
            session.send("Hi '%s'，很高興認識你～ ", session.userData.name);
            builder.Prompts.choice(session, "請選擇您的性別? ", "男|女", { listStyle: builder.ListStyle.button });
        },
        function (session, results, next) {
            session.userData.gender = results.response.entity;
            next();
        },
        function (session, results, next) {
            session.beginDialog('/getbeachinfo');
        },
        function (session, results, next) {
            session.send(results.returnSentence);
            builder.Prompts.choice(session, " ", "你怕曬黑嗎？|擔心下雨，覺得掃興|氣溫|浪高|潮汐|日夜溫差|風速", { listStyle: builder.ListStyle.button });
        },
        function (session, results, next) {
            session.userData.concernType = results.response.entity;
            session.endDialog('接下來幫您查詢與 %s 有關的資訊', session.userData.concernType);
        }

    ]
).triggerAction({
    matches: 'sayhi'
});

bot.dialog('/getbeachinfo',
    [
        function (session, results, next) {
            builder.Prompts.choice(session, "請問你想去哪邊的海邊玩呀? ", "北部|中部|南部|東部", { listStyle: builder.ListStyle.button });
        },
        function (session, results, next) {
            session.userData.beachRegion = results.response.entity;
            next();
        },
        function (session, results, next) {
            switch (session.userData.beachRegion) {
                case '北部':
                    session.userData.beachName = '白沙灣海水浴場';
                    session.userData.title = '【北海岸】炎炎夏日玩水趣 「白沙灣海水浴場」'
                    session.userData.url = 'http://qpjj.pixnet.net/blog/post/3394374';
                    session.userData.pic = 'http://pic.pimg.tw/qpjj/3f8857067222935d11d7ffe4d6c2c7a1.jpg?v=1287477513';


                    break;
                case '中部':
                    session.userData.beachName = '台中';
                    break;
                case '南部':
                    session.userData.beachName = '西子灣';
                    break;
                case '東部':
                    session.userData.beachName = '福隆';
                    break;
                default:
                    session.send('沒這一區吧！');
                    session.beginDialog('/getbeachinfo');
            }


            var msg = new builder.Message(session)
                .textFormat(builder.TextFormat.xml)
                .attachments([
                    new builder.HeroCard(session)
                        .title(session.userData.title)
                        .text(session.userData.beachName + '的海灘很棒喔！')
                        .images([
                            builder.CardImage.create(session, session.userData.pic)
                        ])
                        .tap(builder.CardAction.openUrl(session, session.userData.url))
            ]);
            session.send(msg);
            next();
        },
        function (session, results, next) {
            builder.Prompts.choice(session, "你想去玩嗎? ", "好喔！|不要，我想看看其他的", { listStyle: builder.ListStyle.button });
        },
        function (session, results, next) {
            if (results.response && results.response.entity == '好喔！') {
                var sentence = `${session.userData.beachName}的資訊，我們已經幫妳記錄下來了～那 ${session.userData.name} , 請問妳去海邊最關心什麼？`;
                session.endDialogWithResult( {returnSentence: sentence} );
            } else if (results.response && results.response.entity == '不要，我想看看其他的') {
                session.beginDialog('/getbeachinfo');
            }
        }
    ]
).triggerAction({
    matches: 'getbeachinfo'
});
