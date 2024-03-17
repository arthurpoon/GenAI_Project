import os
import subprocess

# List of URLs
urls = [
    "https://www.sec.gov/Archives/edgar/data/718877/000162828021002828/atvi-20201231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/874761/000087476123000010/aes-20221231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1018724/000101872420000004/amzn-20191231x10k_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1748790/000174879021000031/amcr-20210630_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1410636/000141063621000101/awk-20201231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1410636/000141063622000048/awk-20211231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/764478/000076447820000017/bby-20200201x10k_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1512673/000151267321000008/sq-20201231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/12927/000001292719000010/a201812dec3110k_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/21344/000002134422000009/ko-20211231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/21344/000002134423000011/ko-20221231_htm.xml",
    "https://www.sec.gov/ixviewer/ix.html?doc=/Archives/edgar/data/0000024741/000156276221000023/glw-20201231x10k.htm",
    "https://www.sec.gov/Archives/edgar/data/24741/000143774922003247/glw20211231_10k_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/909832/000090983221000014/cost-20210829_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/40704/000119312520186469/d89717d10k_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/1637459/000163745920000027/form10-k2019_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/936468/000093646821000013/lmt-20201231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/936468/000093646822000008/lmt-20211231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/936468/000093646823000009/lmt-20221231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/789570/000156459021009205/mgm-10k_20201231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/320187/000032018721000028/nke-20210531_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/77476/000007747622000010/pep-20211225_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/77476/000007747623000007/pep-20221231_htm.xml",
    "https://www.sec.gov/Archives/edgar/data/104169/000010416920000011/wmtform10-kx1312020_htm.xml"
]

# Directory to save output JSON files
output_json_dir = "/Users/arthurpoon/Downloads/XBRL_JSON_files"

# Create directory if it doesn't exist
os.makedirs(output_json_dir, exist_ok=True)

# Loop through URLs and execute command for each
for url in urls:
    filename = url.split("/")[-1]
    output_json_file = os.path.join(output_json_dir, filename.split('.')[0] + ".json")
    command = f"/Applications/Arelle.app/Contents/MacOS/arelleCmdLine --plugins=saveLoadableOIM --saveLoadableOIM={output_json_file} -f {url}"
    print("Executing command:", command)
    subprocess.run(command, shell=True)
