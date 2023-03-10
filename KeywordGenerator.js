require('dotenv').config()

function program() {
    const fs = require("fs");
    var randomWords = require('random-words');
    var request = require('request');
    
    var apiKey = process.env["AdobeAPIKey"]
    var keyword = process.env["SearchKeyword"]
    var leastNumOfKeywords = process.env["LeastNumOfKeywords"]

    var headers = {
        'x-api-key': apiKey,
        'x-product': 'MySampleApp/1.0'
    };

    var randomWord = randomWords();
    var options = {
        url: "https://stock.adobe.io/Rest/Media/1/Search/Files?locale=en_US&search_parameters%5Bwords%5D=" + keyword + "&result_columns%5B%5D=keywords&result_columns%5B%5D=id",
        headers: headers
    };

    if (keyword == "Random" || keyword == "random" || keyword == "") {
        options.url = "https://stock.adobe.io/Rest/Media/1/Search/Files?locale=en_US&search_parameters%5Bwords%5D=" + randomWord + "&result_columns%5B%5D=keywords&result_columns%5B%5D=id"
    }

    function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
            
            const obj = JSON.parse(body)
            for (let y = 0; y < obj.files.length; y++) {

                var flag = false;
                if (obj.files[y].keywords.length < leastNumOfKeywords) {
                    var flag = true;
                }

                for (let i = 0; i < obj.files[y].keywords.length; i++) {
                    if (isNaN(obj.files[y].keywords[i]["name"]) == false) {
                        var flag = true;
                        console.log(obj.files[y].keywords[i]["name"])
                    }
                }

                console.log(flag)
                if (flag == false) {
                    var flag = true;
                    console.log(obj.files[y].keywords.length)

                    fs.appendFileSync("./KeywordList.txt", "Generative AI; Generative; AI; ", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })

                    for (let i = 0; i < obj.files[y].keywords.length; i++) {
                        fs.appendFileSync("./KeywordList.txt", obj.files[y].keywords[i].name + "; ", (err) => {
                            if (err) {
                                console.error(err);
                            return;
                            }
                        })
                        
                        console.log(obj.files[y].keywords[i].name, i)
                    }

                    fs.appendFileSync("./KeywordList.txt", "\r\n", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })

                    fs.appendFileSync("./KeywordList.txt", "/imagine prompt: ", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })
                    
                    for (let i = 0; i < obj.files[y].keywords.length; i++) {
                        fs.appendFileSync("./KeywordList.txt", obj.files[y].keywords[i].name + " ", (err) => {
                            if (err) {
                                console.error(err);
                            return;
                            }
                        })
                        
                    }

                    fs.appendFileSync("./KeywordList.txt", "realistic high quality detailed --v 4 --ar 3:2\r\n", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })
                }
            }
        } 
    }

    request(options, callback);
}

const timer = ms => new Promise(res => setTimeout(res, ms))

//async function load () { 
for (let i = 0; i < process.env["NumberOfIterations"]; i++) {
    program();

    //await timer(3000); 
    }
//}
console.log(process.env["NumberOfIterations"])

//load();