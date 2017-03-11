"use strick"

var assert    = require('chai').assert;
var Converter = require('./converter');

suite('converter arabic numerals', function () {

    let converter = {};

    setup(function () {
        converter = new Converter();
    });

    test('when input 1 return I', function(){
        res = converter.arabicToRoman(1);

        assert.equal(res, 'I')
    });

    test('when input 2 return II', function(){
        res = converter.arabicToRoman(2);

        assert.equal(res, 'II')
    });

    test('when input 3 return III', function() {
        res = converter.arabicToRoman(3);

        assert.equal(res, 'III')
    });

    test('when input 5 return V', function() {
        res = converter.arabicToRoman(5);

        assert.equal(res, 'V')
    });
});

