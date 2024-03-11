#!/usr/bin/node

const { argv } = require('node:process');

if (!(argv[2] === undefined)) {
  let myNumber = parseInt(argv[2]);

  if (!isNaN(myNumber)) {
    while (myNumber) {
      console.log('C is fun');
      myNumber--;
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
