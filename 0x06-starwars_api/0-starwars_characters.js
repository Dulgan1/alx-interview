#!/usr/bin/node
/* *
 * Write a script that prints all characters of a Star Wars movie:
 *
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * You must use the Star wars API
 * You must use the request module
 * */
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
const request = require('request');

function ask (link) {
  return new Promise((resolve, reject) => {
    request(link, (error, response, body) => {
      if (response.statusCode === 200 && !error) {
        resolve(JSON.parse(body));
      } else {
        reject(error);
      }
    });
  });
}

async function run (link) {
  const res = await ask(link);
  for (const value of res.characters) {
    const cObj = await ask(value);
    console.log(cObj.name);
  }
}

run(url);
