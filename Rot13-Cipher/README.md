
# Rot13 Cipher 

ROT13 (Rotate by 13 places) is a simple letter substitution cipher that replaces each letter in a message with the letter 13 places down or up the alphabet. It is a special case of the Caesar cipher, which is one of the earliest and simplest encryption techniques.

In the ROT13 cipher, the alphabet is shifted by 13 positions. This means that each letter is replaced by the letter 13 positions away in the alphabet, wrapping around if necessary. For example:

'A' becomes 'N'
'B' becomes 'O'
'C' becomes 'P'
...
'N' becomes 'A'
'O' becomes 'B'
'P' becomes 'C'
...
The ROT13 cipher is its own inverse, meaning that applying it twice will return the original text. This property makes it particularly useful for hiding text in plain sight, such as spoiler text in online forums or hiding answers to puzzles.

ROT13 is not a secure encryption method and provides minimal security against determined attackers. It is primarily used for obfuscation and basic text transformations rather than serious encryption. Despite its simplicity, ROT13 remains a popular and widely recognized technique, especially in online culture.










## Acknowledgements

 - [rot13](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjm1fyG8caEAxXQg2MGHUTSDh8QFnoECBEQAQ&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Frot13-cipher%2F&usg=AOvVaw3Ox7lXBByvmxdavfq7VREk&opi=89978449)
 - [rot13 testcases](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiFirme8caEAxVE1jgGHUOdAqcQFnoECCsQAQ&url=https%3A%2F%2Frumkin.com%2Ftools%2Fcipher%2Frot13%2F&usg=AOvVaw2CeIrbHUEG0iteTv9Tqqdr&opi=89978449)


 


## Usage/Examples

### Installation steps
* **Clone the Repository** : Clone the repository containing rot13 Python application to your local machine. 

* **Navigate to the directory** :  Open a terminal or command prompt and navigate to the root directory of your Python application where rot13.py is located.This is where you can find raw python file and implementation

* **Navigate to the build directory** : Navigate to the build directory under the root dir of the project where executable file would be located.


### Usage
Run the executable file using the command 

``.\rot13.exe [options] [message]``

* options indicate encryption or decryption methods 
* -e indicates encryption and -d indicates decryption
* message indicate message that needs to be encrypted/decrypted







 