import csv
import http.client
import json
from configs.check_ms_addresses import networks, signers, ms_list

def check_ms_addresses(output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["signer", "address", "network", "safe_address", "commettee"])

        for signer in signers:
            for network in networks:
                conn = http.client.HTTPSConnection(f"safe-transaction-{network}.safe.global")
                conn.request("GET", f'/api/v1/owners/{signer[1]}/safes/')
                response = conn.getresponse()
                if response.status == 200:
                    response_data = response.read()
                    response_str = response_data.decode("utf-8")
                    parsed_data = json.loads(response_str)
                    safes = parsed_data.get("safes", [])
                print(signer[0], signer[1], network, response.status, "Safes:", safes)
                conn.close()
                if safes:
                    for safe_address in safes:
                        if safe_address in ms_list:
                            ms_name = ms_list[safe_address]
                        else:
                            ms_name = 'NOT FOUND'
                        writer.writerow([signer[0], signer[1], network, safe_address, ms_name])
                else:
                    writer.writerow([signer[0], signer[1], network, "No safes found", '-'])

    print(f"Results saved to {output_file}")