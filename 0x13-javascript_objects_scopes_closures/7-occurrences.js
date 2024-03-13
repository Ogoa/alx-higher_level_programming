#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;

  if (list === undefined || searchElement === undefined) {
    return 0;
  }

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      occurences++;
    }
  }

  return occurences;
};
