#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const argv = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[0];


request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  }
  const characters = JSON.parse(body).characters;
  helperChar(characters, 0);
});

function helperChar (chars, i) {
  request(chars[i], (err, res, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (i + 1 < chars.length) {
        helperChar(chars, i + 1);
      }
    }
  });
}
