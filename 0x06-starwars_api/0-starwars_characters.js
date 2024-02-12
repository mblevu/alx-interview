#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const film = JSON.parse(body);
    const characterUrls = film.characters;
    characterUrls.forEach((characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (error) {
          console.error('error:', error);
        } else {
          const character = JSON.parse(body);
          console.log(character.name);
        }
      });
    });
  }
});
