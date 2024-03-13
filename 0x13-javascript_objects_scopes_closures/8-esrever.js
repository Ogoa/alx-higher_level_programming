#!/usr/bin/node

exports.esrever = function (list) {
  const hashMap = new Map();
  let i;

  if (list === undefined) {
    return [];
  }

  for (i = 0; i < list.length; i++) {
    hashMap.set(i, list[i]);
  }

  const newList = [];
  i--;
  while (i >= 0) {
    newList.push(list[i]);
    i--;
  }

  return newList;
};
