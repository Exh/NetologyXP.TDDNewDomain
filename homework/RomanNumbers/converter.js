"use strick"

class Converter
{
    arabicToRoman(n)
    {
        if (n > 500)
            return this.arabicToRoman(500) + this.arabicToRoman(n - 500);
        else if (n == 500)
            return "D";
        if (n > 400)
            return this.arabicToRoman(400) + this.arabicToRoman(n - 400);
        else if (n == 400)
            return "CD";
        if (n > 100)
            return this.arabicToRoman(100) + this.arabicToRoman(n - 100);
        else if (n == 100)
            return "C";
        else if (n > 90)
            return  this.arabicToRoman(90) + this.arabicToRoman(n - 90);
        else if (n == 90)
            return "XC";
        else if (n == 50)
            return "L";
        else if (n > 40)
            return this.arabicToRoman(40) + this.arabicToRoman(n - 40);
        else if (n == 40)
            return "XL";
        else if (n > 10)
            return this.arabicToRoman(10) + this.arabicToRoman(n - 10);
        else if (n == 10)
            return "X";
        else if (n == 9)
            return "IX";
        else if (n > 5)
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