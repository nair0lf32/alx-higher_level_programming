#!/usr/bin/node
const { argv } = require('process');
const a = Number(argv[2]);
const b = Number(argv[3]);
const sum = (a, b) => a + b;
console.log(sum(a, b));
