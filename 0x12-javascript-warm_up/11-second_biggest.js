#!/usr/bin/node

const { argv } = require('node:process');

const args = {};

/*
 * Find the key of the maximum value in the dictionary
 */
function findMax (dict) {
  return Object.keys(dict).reduce((a, b) => dict[a] > dict[b] ? a : b);
}

/*
 * Populate the dictionary with each item in the argument string
 */
if (argv.length < 3) {
  console.log('0');
} else if (argv.length === 3) {
  console.log('1');
} else {
  for (let i = 2; i < argv.length; i++) {
    args[argv[i]] = parseInt(argv[i]);
  }

  delete args[findMax(args)];

  console.log(args[findMax(args)]);
}
