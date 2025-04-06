const generateSubdomains = function(length) {
    const charset = 'abcdefghijklmnopqrstuvwxyz'.split('');
    let subdomains = charset;
    let subdomain;
    let letter;
    let temp;

    for (let i = 1; i < length; i++) {
        temp = []
        for (let k = 0; k < subdomains.length; k++) {
            subdomain = subdomains[k];
            for (let m = 0; m < charset.length; m++) {
                letter = charset[m];
                temp.push(subdomain + letter);
            }
        }
        subdomains = temp
    }
    return subdomains;
}


const subdomains = generateSubdomains(4);


const dns = require('dns');
const { constrainedMemory } = require('process');
const promises = [];

const subdomains = [];

subdomains.forEach((subdomain) => {
    promises.push(new Promise((resolve, reject) => {
        dns.resolve(`${subdomain}.example.com`, function (err, ip) {
            return resolve({ subdomain: subdomain, ip: ip });
        });
    }));
});


Promise.all(promises).then(function(results) {
    results.forEach((result) => {
        if (!!result.ip) {
            console.log(result);
        }
    });
});


const discoverHTTPVerbs = function(url) {
    const verbs = ['POST', 'GET', 'PUT', 'PATCH', 'DELETE'];
    const promises = [];

    verbs.forEach((verb) => {
        const promise = new Promise((resolve, reject) => {
            const http = new XMLHttpRequest();

            http.open(verb, url, true)
            http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

            http.onreadystatechange = function() {
                if (http.readyState === 4) {
                    return resolve({ verb: verb, status: http.status });
                }
            }

            setTimeout(() => {
                return resolve({ verb: verb, status: -1 });
            }, 1000);

            http.send({});
        });
        promises.push(promise);
    });

    Promise.all(promises).then(function(values) {
        console.log(values);
    });
}


let  base64_str = atob('am9l0jEyMzQ=');


{
    "response_type": code,
    "client_id": id,
    "scope": [scopes],
    "state": state,
    "redirect_uri": uri
}


{
    'user_id': 12345,
    'privacy': {
        'publicProfile': true
    }
}


react_version = React.version;
vue_version = React.version;
ember_version = Ember.VERSION;
console.log(ember_version);
console.log(react_version);
console.log(vue_version);
