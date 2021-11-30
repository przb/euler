
/*
If the numbers 1 to 5 are written out in words: one, two, three, four,
 five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
 out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
*/

// There is probably a way to optimize this, but at this time i do not know how to do so.
const int ONE = 3;
const int TWO = 3;
const int THREE = 5;
const int FOUR = 4;
const int FIVE = 4;
const int SIX = 3;
const int SEVEN = 5;
const int EIGHT = 5;
const int NINE = 4;
const int TEN = 3;
const int ELEVEN = 6;
const int TWELVE = 6;
const int THIRTEEN = 8;
const int FOURTEEN = 8;
const int FIFTEEN = 7;
const int SIXTEEN = 7;
const int SEVENTEEN = 9;
const int EIGHTEEN = 8;
const int NINETEEN = 8;
const int TWENTY = 6;
const int THIRTY = 6;
const int FORTY = 5;
const int FIFTY = 5;
const int SIXTY = 5;
const int SEVENTY = 7;
const int EIGHTY = 6;
const int NINETY = 6;
const int HUNDRED = 7;
const int THOUSAND = 8;
const int AND = 3;

int numOnes(int n)
{
    switch (n)
    {
    case 1:
        return ONE;
        break;
    case 2:
        return TWO;
        break;
    case 3:
        return THREE;
        break;
    case 4:
        return FOUR;
        break;
    case 5:
        return FIVE;
        break;
    case 6:
        return SIX;
        break;
    case 7:
        return SEVEN;
        break;
    case 8:
        return EIGHT;
        break;
    case 9:
        return NINE;
        break;
    }
}

int numTens(int n)
{
    switch (n)
    {
    case 1:
        return 0;
        break;
    case 2:
        return TWENTY;
        break;
    case 3:
        return THIRTY;
        break;
    case 4:
        return FORTY;
        break;
    case 5:
        return FIFTY;
        break;
    case 6:
        return SIXTY;
        break;
    case 7:
        return SEVENTY;
        break;
    case 8:
        return EIGHTY;
        break;
    case 9:
        return NINETY;
        break;
    case 0:
        return TEN;
        break;
    }
}

int main()
{

    return 0;
}