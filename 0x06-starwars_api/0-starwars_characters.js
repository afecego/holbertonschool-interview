#!/usr/bin/node
// script that prints all characters of a Star Wars movie
const request = require('request');
const argv = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[0];

request(url, async (error, response, body) => {
  if (error) return console.error(error);
  const characters = JSON.parse(body).characters;
  for (const charact of characters) {
    await new Promise((resolve, reject) => {
      request(charact, (error, response, body) => {
        if (error) return console.error(error);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
