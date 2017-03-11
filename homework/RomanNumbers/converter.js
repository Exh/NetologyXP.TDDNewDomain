"use strick"

class Converter
{
    evaluateNum(arabic, roman, n)
    {
        if (n > arabic)
            return this.arabicToRoman(arabic) + this.arabicToRoman(n - arabic);
        else if (n == arabic)
            return roman;
        return "";
    }

    arabicToRoman(n)
    {
        // if (n > 500)
        //     return this.arabicToRoman(500) + this.arabicToRoman(n - 500);
        // else if (n == 500)
        //     return "D";
        var res = this.evaluateNum(1000, "M", n);
        if (res) return res;
        var res = this.evaluateNum(900, "CM", n);
        if (res) return res;
        var res = this.evaluateNum(500, "D", n);
        if (res) return res;
        var res = this.evaluateNum(400, "CD", n);
        if (res) return res;
        var res = this.evaluateNum(100, "C", n);
        if (res) return res;
        var res = this.evaluateNum(90, "XC", n);
        if (res) return res;
        var res = this.evaluateNum(50, "L", n);
        if (res) return res;
        var res = this.evaluateNum(40, "XL", n);
        if (res) return res;
        var res = this.evaluateNum(10, "X", n);
        if (res) return res;
        else if (n == 9)
            return "IX";
        var res = this.evaluateNum(5, "V", n);
        if (res) return res;
        else if (n == 4)
            return "IV";
        else
            return "I".repeat(n);
    }
}

module.exports = Converter;