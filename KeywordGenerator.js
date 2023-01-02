function program() {
    const fs = require("fs");
    var randomWords = require('random-words');
    var request = require('request');

    lineArray = []
    const allFileContents = fs.readFileSync('./Information.txt', 'utf-8');
    allFileContents.split(/\r?\n/).forEach(line =>  {
        lineArray.push(line)
    });

    var apiKey = lineArray[4].substring(9)

    var headers = {
        'x-api-key': apiKey,
        'x-product': 'MySampleApp/1.0'
    };

    var randomWord = randomWords();
    var options = {
        url: "https://stock.adobe.io/Rest/Media/1/Search/Files?locale=en_US&search_parameters%5Bwords%5D=" + "camera equipment" + "&result_columns%5B%5D=keywords&result_columns%5B%5D=id",
        headers: headers
    };

    function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
            
            const obj = JSON.parse(body)
            
            for (let y = 0; y < obj.files.length; y++) {

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

    request(options, callback);
}

const timer = ms => new Promise(res => setTimeout(res, ms))

//async function load () { 
for (let i = 0; i < 7; i++) {
    program();

    //await timer(3000); 
    }
//}

//load();