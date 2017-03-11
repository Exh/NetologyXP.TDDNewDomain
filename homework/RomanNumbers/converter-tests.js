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

    test('when input 4 return IV', function() {
        res = converter.arabicToRoman(4);

        assert.equal(res, 'IV')
    });

    test('when input 6 return VI', function() {
        res = converter.arabicToRoman(6);

        assert.equal(res, 'VI')
    });

    test('when input 7 return VII', function() {
        res = converter.arabicToRoman(7);

        assert.equal(res, 'VII')
    });

    test('when input 8 return VIII', function() {
        res = converter.arabicToRoman(8);

        assert.equal(res, 'VIII')
    });

    test('when input 10 return X', function() {
        res = converter.araWbicToRoman(10);

        assert.equal(res, 'X')
    });
});

