class Solution {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string encoded;
        for (const string& s : strs) {
            encoded += to_string(s.size()) + "#" + s;
        }
        return encoded; // input = ["Hello", "World"] output = "5#Hello5#World"
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> result; // for storing the decoded words
        int i = 0;
        while (i < s.size()) {
            // 1️⃣ Read length
            int j = i;
            while (s[j] != '#') j++; // go till you find a hash character
            int length = stoi(s.substr(i, j - i)); // find the length of the word
            // 2️⃣ Extract string of that length
            string word = s.substr(j + 1, length); // extract that part of word
            result.push_back(word); // push the word in result array
            // 3️⃣ Move pointer
            i = j + 1 + length; // move the pointer to the next word
        }
        return result;
    }
};
