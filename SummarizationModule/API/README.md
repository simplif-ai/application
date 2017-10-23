# Simplif.ai's API

#### API URL: https://ir.thirty2k.com/summarize

## How to request a summarization
- You must make a POST request to the API URL, any other request will return an error.
- The format of the body of the data must be as follows
    * Must be JSON data or Form Data
    * The text that you want summarized must be stored in a JSON variable called "text"
#### Example
    {
        "text": "Text that I wish to summarize. Please summarize me."
    }
    
## What does the response look like
- The returned data will be JSON data
- If your request format is not correct then the response will look as follows
    * The JSON will contain a variable called "error" that contains a message that will tell you either that you did not 
    have a "text" variable in the request or if you used an incorrect request method
    * The JSON will also have a variable called "success" and it will be set to false in this case
- If your request format is correct then the response will look as follows
    * The JSON will contain a variable called "text" that is an array.  Every index in the array that is contained in 
    "text" will be an array of size three.  For each of the arrays of size three the first index will contain a sentence 
    from the original input text, the next index will be the strength of that sentence and the last index will contain 
    the position of the sentence in the original input text.
    * The JSON will also contain a variable called "success" that will be set to true in this case. 

#### Example
    {
        "text": [
                    ["Text that I wish to summarize", 1, 0],
                    ["Please summarize me", 0, 1]
                ],
         "success": true
    }

_Note the response may take longer based on the input text length_

    
