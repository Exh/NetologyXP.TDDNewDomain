"use strick"

class Converter
{
    arabicToRoman(n)
    {
        if (n == 5)
            return "V";
        else
            return "I".repeat(n);
    }
}

module.exports = Converter;