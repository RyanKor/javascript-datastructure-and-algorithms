console.log(this)

function test() {
    'use strict';
    return this
}

function test2() {
    return this
}
console.log(test)
console.log(test2)