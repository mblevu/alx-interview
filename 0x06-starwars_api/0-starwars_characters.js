#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const movie = JSON.parse(body);
  for (const character of movie.characters) {
    const p = new Promise((resolve, reject) => {
      request(character, function (error, response, body) {
        if (error) {
          reject(error);
        }
        resolve(JSON.parse(body).name);
      });
    });
    try {
      console.log(await p);
    } catch (error) {
      console.error('error:', error);
    }
  }
});
