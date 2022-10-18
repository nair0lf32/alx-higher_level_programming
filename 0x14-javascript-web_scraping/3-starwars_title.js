#!/usr/bin/node
const request = require('request');
const { argv } = require('process');
const req_url = 'https://swapi-api.hbtn.io/api';
request(req_url + '/films/' + argv[2], (error, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
