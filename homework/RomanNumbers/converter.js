"use strick"

class Converter
{
    arabicToRoman(n)
    {
        if (n > 5)
            return this.arabicToRoman(5) + this.arabicToRoman(n - 5);
        else if (n == 5)
            return "V";
        else if (n == 4)
            return "IV";
        else
            return "I".repeat(n);
    }
}

module.exports = Converter;