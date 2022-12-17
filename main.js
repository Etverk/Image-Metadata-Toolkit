const fs = require("fs");
var randomWords = require('random-words');
var request = require('request');


var apiKey = fs.readFileSync("./info.txt",'utf8')

var headers = {
    'x-api-key': apiKey,
    'x-product': 'MySampleApp/1.0'
};

var randomWord = randomWords();

var options = {

    url: "https://stock.adobe.io/Rest/Media/1/Search/Files?locale=en_US&search_parameters%5Bwords%5D=" + randomWord + "&result_columns%5B%5D=keywords&result_columns%5B%5D=id",
    headers: headers
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        fs.writeFile("./test.txt", body + "\n\n", (err) => {
            if (err) {
                console.error(err);
            return;
              }
        });

        console.log(JSON.stringify(body, null, 10));
        console.log(randomWord);
        const obj = JSON.parse(body)

        for (let y = 0; y < obj.files.length; y++) {
            for (let i = 0; i < obj.files[y].keywords.length; i++) {
                console.log(obj.files[y].keywords[i].name)
            }
            console.log("-----------\n")
        }
    }
}

request(options, callback);

