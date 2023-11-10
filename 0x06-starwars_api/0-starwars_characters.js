#!/usr/bin/node
/* *
 * Write a script that prints all characters of a Star Wars movie:
 *
 * The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order as the “characters” list in the /films/ endpoint
 * You must use the Star wars API
 * You must use the request module
 * */
const url = "https://swapi-api.alx-tools.com/api/films/" + process.argv[2];
const request = require('request');

request(url, (error, response, body) => {
  const obj_body = JSON.parse(body);
  for (const arg in obj_body.characters) {
    request(obj_body.characters[arg], (cerror, cresponse, cbody) => {
     const  obj_cbody = JSON.parse(cbody);
      console.log(obj_cbody.name);
    });
  }
});
