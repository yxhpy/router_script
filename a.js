let securityEncode = function (input1, input2, input3) {
    var dictionary = input3;
    var output = "";
    var len, len1, len2, lenDict;
    var cl = 0xBB, cr = 0xBB;

    len1 = input1.length;
    len2 = input2.length;
    lenDict = dictionary.length;
    len = len1 > len2 ? len1 : len2;

    for (var index = 0; index < len; index++) {
        cl = 0xBB;
        cr = 0xBB;

        if (index >= len1) {
            cr = input2.charCodeAt(index);
        } else if (index >= len2) {
            cl = input1.charCodeAt(index);
        } else {
            cl = input1.charCodeAt(index);
            cr = input2.charCodeAt(index);
        }

        output += dictionary.charAt((cl ^ cr) % lenDict);
    }

    return output;
};