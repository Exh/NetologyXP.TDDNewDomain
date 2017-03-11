"use strick"

var assert    = require('chai').assert;
var Converter = require('./converter');

suite('converter arabic numerals', function () {

    test('when input 1 return I', function(){
        converter = new Converter();
        res = converter.arabicToRoman('1');

        assert.equal(res, 'I')
    });
});

