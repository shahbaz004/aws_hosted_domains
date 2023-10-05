import os
import socket
import requests
import multiprocessing
import csv
import sys


def get_ip_from_domain(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        if ip_address:
            company_name = get_company_name(ip_address)
            return [domain, ip_address, company_name]
        else:
            return ["Invalid Domain"]
    except socket.gaierror:
        return None


def get_company_name(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            return data.get("org", "Company information not available")
    except requests.exceptions.RequestException:
        pass
    return "Company information not available"


def process_domain(domain):
    domain = domain.strip()
    data = get_ip_from_domain(domain)

    if data is not None:
        if "Amazon.com" in data[2]:
            with open("amazon_domains.csv", 'a', newline='') as output_file:
                csv_writer = csv.writer(output_file)

                if output_file.tell() == 0:
                    csv_writer.writerow(['Domain Name', 'IP Address', 'Company'])

                csv_writer.writerow(data)
        else:
            return "Not Found"


def filter_amazon_domains(filename):
    with open(filename, 'r') as file:
        domain_names = file.readlines()
    pool = multiprocessing.Pool(processes=4)

    pool.map(process_domain, domain_names)


if __name__ == "__main__":
    # filename = "/home/ubbuntu/Enigmatix/Engmatix_Marketplace/Marketplace_new_design/temp_domains.txt"
    folder_path = sys.argv[1]
    print(folder_path)

    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
    else:
        files = os.listdir(folder_path)

        for filename in files:
            file = os.path.join(folder_path, filename)
            filter_amazon_domains(file)
            print(f"Original filename: {filename}")
