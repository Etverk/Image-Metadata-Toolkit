function program() {
    const fs = require("fs");
    var randomWords = require('random-words');
    var request = require('request');

    function getFirstLine(filePath) {
        const fileContent = fs.readFileSync(filePath, 'utf-8');
        return (fileContent.match(/(^.*)/) || [])[1] || '';
    } 

    var apiKey = getFirstLine("./info.txt")

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
            
            const obj = JSON.parse(body)
            console.log(obj.files)
            
            for (let y = 0; y < obj.files.length; y++) {

                fs.appendFileSync("./test.txt", "Generative AI; Generative; AI; ", (err) => {
                    if (err) {
                        console.error(err);
                    return;
                    }
                })

                for (let i = 0; i < obj.files[y].keywords.length; i++) {
                    fs.appendFileSync("./test.txt", obj.files[y].keywords[i].name + "; ", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })
                    
                    console.log(obj.files[y].keywords[i].name, i)
                }

                fs.appendFileSync("./test.txt", "\r\n", (err) => {
                    if (err) {
                        console.error(err);
                    return;
                    }
                })

                fs.appendFileSync("./test.txt", "/imagine prompt: ", (err) => {
                    if (err) {
                        console.error(err);
                    return;
                    }
                })
                
                for (let i = 0; i < obj.files[y].keywords.length; i++) {
                    fs.appendFileSync("./test.txt", obj.files[y].keywords[i].name + " ", (err) => {
                        if (err) {
                            console.error(err);
                        return;
                        }
                    })
                    
                    console.log(obj.files[y].keywords[i].name, i)
                }

                fs.appendFileSync("./test.txt", "realistic high quality detailed --v 4 --ar 3:2\r\n", (err) => {
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
for (let i = 0; i < 100; i++) {
    program();

    //await timer(3000); 
    }
//}

//load();