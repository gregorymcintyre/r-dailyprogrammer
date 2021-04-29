/*
Caesar cipher
Warmup

Given a lowercase letter and a number between 0 and 26, return that letter Caesar shifted by that number. To Caesar shift a letter by a number, advance it in the alphabet by that many steps, wrapping around from z back to a:

warmup('a', 0) => 'a'
warmup('a', 1) => 'b'
warmup('a', 5) => 'f'
warmup('a', 26) => 'a'
warmup('d', 15) => 's'
warmup('z', 1) => 'a'
warmup('q', 22) => 'm'

Hint: taking a number modulo 26 will wrap around from 25 back to 0. This is commonly represented using the modulus operator %. For example, 29 % 26 = 3. Finding a way to map from the letters a-z to the numbers 0-25 and back will help.
Challenge

Given a string of lowercase letters and a number, return a string with each letter Caesar shifted by the given amount.

caesar("a", 1) => "b"
caesar("abcz", 1) => "bcda"
caesar("irk", 13) => "vex"
caesar("fusion", 6) => "layout"
caesar("dailyprogrammer", 6) => "jgorevxumxgsskx"
caesar("jgorevxumxgsskx", 20) => "dailyprogrammer"

Hint: you can use the warmup function as a helper function.
Optional bonus 1

Correctly handle capital letters and non-letter characters. Capital letters should also be shifted like lowercase letters, but remain capitalized. Leave non-letter characters, such as spaces and punctuation, unshifted.

caesar("Daily Programmer!", 6) => "Jgore Vxumxgsskx!"

If you speak a language that doesn't use the 26-letter A-Z alphabet that English does, handle strings in that language in whatever way makes the most sense to you! In English, if a string is encoded using the number N, you can decode it using the number 26 - N. Make sure that for your language, there's some similar way to decode strings.
Optional bonus 2

Given a string of English text that has been Caesar shifted by some number between 0 and 26, write a function to make a best guess of what the original string was. You can typically do this by hand easily enough, but the challenge is to write a program to do it automatically. Decode the following strings:

Zol abyulk tl puav h ulda.

Tfdv ef wlikyvi, wfi uvrky rnrzkj pfl rcc nzky erjkp, szx, gfzekp kvvky.

Qv wzlmz bw uiqvbiqv iqz-axmml dmtwkqbg, i aeittwe vmmla bw jmib qba eqvoa nwzbg-bpzmm bquma mdmzg amkwvl, zqopb?

One simple way is by using a letter frequency table. Assign each letter in the string a score, with 3 for a, -1 for b, 1 for c, etc., as follows:

3,-1,1,1,4,0,0,2,2,-5,-2,1,0,2,3,0,-6,2,2,3,1,-1,0,-5,0,-7

The average score of the letters in a string will tell you how its letter distribution compares to typical English. Higher is better. Typical English will have an average score around 2, and strings of random letters will have an average score around 0. Just test out each possible shift for the string, and take the one with the highest score. There are other good ways to do it, though.

(This challenge is based on Challenge #47 [easy], originally posted by u/oskar_s in May 2012.)
*/

#include <iostream>

using namespace std;

char warmup(char c, int i){
    int output;

    if((int)c >= 97)
        output = (int(c)-97+i)%26+97;
    else if((int)c >= 65)
        output = (int(c)-65+i)%26+65;
    else
        output = c;
    return (char)output;
}

string caesar(string c, int i){
    string s;
    for (int j=0 ; j < c.length() ; j++){
        //cout << warmup(c[j], i) << endl;
        s += warmup(c[j], i);
    }
    //cout << s << endl;
    return s;
}

int main()
{
    cout << "Caeser Cipher\n------------------" << endl;
    cout << "Warm Up\n------------------" << endl;
    cout << warmup('a', 0) << endl; // => 'a'
    cout << warmup('a', 1) << endl; // => 'b'
    cout << warmup('a', 5) << endl; // => 'f'
    cout << warmup('a', 26) << endl; // => 'a'
    cout << warmup('d', 15) << endl; // => 's'
    cout << warmup('z', 1) << endl; // => 'a'
    cout << warmup('q', 22) << endl; // => 'm'

    cout << "\nChallenge \n------------------" << endl;
    cout << caesar("a", 1) << endl; // => "b"
    cout << caesar("abcz", 1) << endl; // => "bcda"
    cout << caesar("irk", 13) << endl; // => "vex"
    cout << caesar("fusion", 6) << endl; // => "layout"
    cout << caesar("dailyprogrammer", 6) << endl; // => "jgorevxumxgsskx"
    cout << caesar("jgorevxumxgsskx", 20) << endl; // => "dailyprogrammer"

    cout << "\nOptional bonus 1 \n------------------" << endl;
    cout << caesar("Daily Programmer!", 6) << endl; // => "Jgore Vxumxgsskx!"
}