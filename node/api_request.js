var request = require('request');
function getApiRequest(url){
        request(url, { json: true }, function(err, res, body){
                        if (err) {
                            return console.log(err);
                             }
//                        console.log(res, res.statusCode)
                        console.log(body)
                        console.log(res.statusCode)
                        });

                }



const https = require('https');
function getApiHttp(url){

        https.get(url, (resp) => {
//            let data = '1';
            // A chunk of data has been recieved.
            resp.on('data', (chunk) => {
                    data += chunk;
                    });

            // The whole response has been received. Print out the result.
            resp.on('end', () => {
                    console.log(JSON.parse(data).explanation);
                    });

            }).on("error", (err) => {
            console.log("Error: " + err.message);

            });
        }



var start = new Date();
function executionTime(){
        setTimeout(function(argument){
            var end = new Date() - start;

            console.info("Execution Time: %d ms", end );

        },1000);


}


url = 'https://shuni.tel/api/v1/shuni/post/'
//console.log(getApiHttp(url));
var data = getApiRequest(url);
console.log(data)
//console.log(getApiRequest(url));
console.log(executionTime());

