#!/usr/bin/node

exports.converter = function (base) {
  function convertToBase (num) {
    const digits = '0123456789abcdefg';

    if (num < base) {
      return digits[num];
    }

    return convertToBase(Math.floor(num / base)) + digits[num % base];
  }

  return convertToBase;
};
