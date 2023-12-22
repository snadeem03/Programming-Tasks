## Problem Statement : Directory Linker Utility
 You are required to design a Python script that interacts with the terminal to perform specific operations on a given directory path. The script should automate the creation of hard links and soft links for files within the specified directory and generate a mapping list for the created links.


### Requirements :
 1. Input : 
  * Accept a directory path as a string input from the user.
 
 2. Operations:
  * Iterate through the files within the provided directory.
  * For each file:
   * Create a hard link with the filename appended with _hardlink.
   * Create a soft link with the filename appended with _softlink.

 3. Output:
  * Generate a list containing:
   * Original filenames.
   * Corresponding hard link filenames.
   * Corresponding soft link filenames.
 
 4. Functionality :
  * Create a function createHardLink(original_file_name) that:
   * Takes the original filename as input.
   * Uses the terminal command to create a hard link for the file.
 
  * Create a function createSoftLink(original_file_name) that:
   * Takes the original filename as input.
   * Uses the terminal command to create a soft link for the file.

 * Create a function mapHardLinksAndSoftLinks() that:
  * Fetches and returns a list of all files within the directory.
  * Filters the list to only consider files (ignores directories).
  * Returns a list containing original filenames, hard link filenames, and soft link filenames.

 5. Validation & Error Handling:
  * Handle potential errors such as:
   * Invalid directory paths.
   * Failed link creation commands.
   * Invalid or missing terminal commands.


### Instructions:
 1. Prompt the user to input a directory path.
 2. Retrieve the list of files from the specified directory
 3. Iterate over each file in the directory:
  * Check if the file has already been linked.
  * If not, create both hard and soft links for the file.

 4. Generate a mapping list showing the original filenames, hard link filenames, and soft link filenames.
 5. Display the generated mapping list to the user.


### Constraints:
 * Ensure that you handle all exceptions and errors gracefully.
 * The script should be able to run on a Unix-like system due to the usage of terminal commands like ln.
 