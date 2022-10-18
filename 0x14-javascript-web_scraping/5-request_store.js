#!/usr/bin/node
const f = require('fs');
const request = require('request');
request(process.argv[2]).pipe(f.createWriteStream(process.argv[3]));
