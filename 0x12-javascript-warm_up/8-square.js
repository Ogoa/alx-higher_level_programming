#!/usr/bin/node

const { argv } = require('node:process');

if (!(argv[2] === undefined)) {
  const size = parseInt(argv[2]);

  if (!isNaN(size)) {
    let i = 0;
    for (i; i < size; i++) {
      console.log('X'.repeat(size));
    }
  } else {
    console.log('Missing size');
  }
} else {
  console.log('Missing size');
}
