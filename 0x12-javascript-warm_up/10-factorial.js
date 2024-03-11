#!/usr/bin/node

const { argv } = require('node:process');

function factorial (num) {
  if (num === 0 || num === 1 || isNaN(num)) {
    return 1;
  }

  return num + factorial(num - 1);
}

/*
 * Extract the number from the arguments string
 */
const a = parseInt(argv[2]);
console.log(`${factorial(a)}`);
