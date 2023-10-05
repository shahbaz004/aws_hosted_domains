# Amazon Domain Filter

The **Amazon Domain Filter** is a Python script designed to filter domain names and their associated IP addresses based on whether they are related to Amazon.com. It utilizes the `socket`, `requests`, `multiprocessing`, and `csv` libraries to achieve this functionality.

## Purpose

The primary purpose of this script is to analyze a list of domain names stored in text files, resolve their IP addresses, and identify whether the corresponding company is Amazon.com or an Amazon-related entity. If the domain is associated with Amazon.com, it saves the domain name, IP address, and company information into a CSV file for further analysis.

## How It Works

Here's how the script works:

1. It reads a list of domain names from one or more text files specified as input.
2. For each domain name, it uses the `socket` library to resolve the domain name into an IP address.
3. It then utilizes the `requests` library to retrieve information about the IP address, specifically the organization (company) associated with it from the [ipinfo.io](https://ipinfo.io) API.
4. If the company information contains "Amazon.com" or is related to Amazon, it saves the domain name, IP address, and company information in a CSV file named "amazon_domains.csv."

## Usage

To use this script, follow these steps:

1. Place your text files containing a list of domain names in a folder.
2. Open a terminal.
3. Navigate to the directory containing the script.
4. Run the script with the path to the folder containing the text files as a command-line argument:

   ```shell
   python domains.py data
