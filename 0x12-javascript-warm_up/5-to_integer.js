#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] !== undefined) {
  const myNumber = parseInt(argv[2]);
  if (!isNaN(myNumber)) {
    console.log(`My number: ${myNumber}`);
  } else {
    console.log('Not a number');
  }
} else {
  console.log('Not a number');
}
