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
        res = converter.arabicToRoman(10);

        assert.equal(res, 'X')
    });

    test('when input 9 return IX', function() {
        res = converter.arabicToRoman(9);

        assert.equal(res, 'IX')
    });

    test('when input 11 return XI', function() {
        res = converter.arabicToRoman(11);

        assert.equal(res, 'XI')
    });

    test('when input 18 return XVIII', function() {
        res = converter.arabicToRoman(18);

        assert.equal(res, 'XVIII')
    });

    test('when input 14 return XIV', function() {
        res = converter.arabicToRoman(14);

        assert.equal(res, 'XIV')
    });

    test('when input 20 return XX', function() {
        res = converter.arabicToRoman(20);

        assert.equal(res, 'XX')
    });

    test('when input 19 return XIX', function() {
        res = converter.arabicToRoman(19);

        assert.equal(res, 'XIX')
    });

    test('when input 50 return L', function() {
        res = converter.arabicToRoman(50);

        assert.equal(res, 'L')
    });

    test('when input 40 return XL', function() {
        res = converter.arabicToRoman(40);

        assert.equal(res, 'XL')
    });

    test('when input 41 return XLI', function() {
        res = converter.arabicToRoman(41);

        assert.equal(res, 'XLI')
    });

    test('when input 49 return XLIX', function() {
        res = converter.arabicToRoman(49);

        assert.equal(res, 'XLIX')
    });

    test('when input 90 return XC', function() {
        res = converter.arabicToRoman(90);

        assert.equal(res, 'XC')
    });

    test('when input 100 return C', function() {
        res = converter.arabicToRoman(100);

        assert.equal(res, 'C')
    });

    test('when input 300 return CCC', function() {
        res = converter.arabicToRoman(300);

        assert.equal(res, 'CCC')
    });

});

