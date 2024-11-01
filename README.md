# SHA256 Decimal Finder

## Introduction

Welcome to the SHA256 Decimal Finder project! This project is about trying to find the first three digits of decimal numbers that are hidden as SHA256 hashes. For example, we want to find out the hash for a number like `1.300000000000000000000000000000`. Unfortunately, we can’t easily find this hash because SHA256 is very secure and hard to reverse.

## What This Project Tries to Do

I wanted to combine two techniques: **brute force** and a **rainbow table**. The idea is to save every possible SHA256 version of decimal numbers, so we can later determine which numbers fall into the range we are looking for. 

However, I found out that this project is not ideal for regular computers. While there are websites that can solve 12-character long SHA256 passwords using similar techniques, my approach quickly created a massive amount of data. When I only ran the code for **74,622,138** hash values, the data size grew to about **4.6 GB**.

### Data Size Calculation

Here’s the math behind the data size:
- Each SHA256 hash takes **64 bytes**.
- If we generate **74,622,138 hash values**(this is how many hash values are I created to try my code efficiency), the total size in bytes is calculated as follows:
  
**For example:**

`Total Bytes = 74,622,138 * 64 = 4,780,200,832 bytes`

To calculate the total bytes, use the following formula:

$$
\text{Total Bytes} = \text{Number of Hashes} \times \text{Bytes per Hash}
$$
$$
\mathbf{Total \ Bytes} = 74,622,138 \times 64 = 4,780,200,832 \ \text{bytes}
$$
To convert bytes to gigabytes, we use the following calculation:
$$
\text{Total Gigabytes} = \frac{\text{Total Bytes}}{1024^3}
$$
For example:
$$
\text{Total Gigabytes} = \frac{4,780,200,832}{1,073,741,824} \approx 4.6 \text{ GB}
$$

After doing a few calculations, I realized that using .txt files would be insufficient for this type of project (I noticed that after running the code for about 10 seconds, the .txt files couldn't handle more than 500 MB of data! :)

After researching online, I chose HDF5 as the storage medium where I could easily and comfortably store and organize my data, and it can be considered successful.


### Data Size Table

| Number          | Name        | Zeros (Trailing) |
|------------------|-------------|------------------|
| 1                | One         | 0                |
| 1,000            | Thousand    | 3                |
| 1,000,000        | Million     | 6                |
| 1,000,000,000    | Billion     | 9                |
| 1,000,000,000,000| Trillion    | 12               |
| 1,000,000,000,000,000| Quadrillion| 15             |
| 1,000,000,000,000,000,000| Quintillion| 18         |
| 1,000,000,000,000,000,000,000| Sextillion| 21      |
| 1,000,000,000,000,000,000,000,000,000| Septillion| 24  |
| 1,000,000,000,000,000,000,000,000,000,000,000| Octillion| 27 |
| 1,000,000,000,000,000,000,000,000,000,000,000,000,000| Nonillion| 30 |
| 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000| Decillion| 33 |

### Limitations

The problem is that if we continue processing this code, our data will become too large for normal storage solutions. When we need to find a specific hash, the amount of data we have to search through will be enormous, and it will take a long time to find anything. Even using a hash table or storing data in binary format might not help much with our current technology.

## Conclusion

After all my efforts, I learned that this approach is not possible with my current resources. This project might not be a successful attempt, but it has taught me a lot about the limitations of technology and I should have conducted more thorough research before attempting this. I realized the fact that the only structures that can decode SHA256 are rainbow table and brute force. However, if you are looking for smaller ranges or numbers, this code might still work for you and could be improved with better algorithms.

Thank you for reading!
