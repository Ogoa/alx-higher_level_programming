#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  /**
   * prints the rectangle using the character provided as the argument
   */
  charPrint (c) {
    const charP = (c === undefined) ? 'X' : c;
    let i;

    for (i = 0; i < this.width; i++) {
      console.log(charP.repeat(this.width));
    }
  }
}

module.exports = Square;
