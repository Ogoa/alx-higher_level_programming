#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * Prints the rectangle instance onto standard output
   * using the 'X' character
   */
  print () {
    let i;

    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  /**
   * Exchanges the width and the height of the rectangle instance
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * Multiplies both the width and the height of the rectangle instance by 2
   */
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
