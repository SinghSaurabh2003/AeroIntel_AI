import os
import requests
from bs4 import BeautifulSoup


class NTSBDownloader:

    def __init__(self):

        self.base_url = "https://www.ntsb.gov"

        self.report_url = (
            "https://www.ntsb.gov/investigations/AccidentReports/Pages/default.aspx"
        )

        self.save_dir = "data/raw/ntsb_accidents"

        os.makedirs(
            self.save_dir,
            exist_ok=True
        )

    # --------------------------------------------------
    # Get Latest PDF Links
    # --------------------------------------------------

    def get_report_links(self):

        response = requests.get(
            self.report_url,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        pdf_links = []

        for link in soup.find_all("a", href=True):

            href = link["href"]

            if href.lower().endswith(".pdf"):

                if href.startswith("/"):

                    href = self.base_url + href

                pdf_links.append(href)

        return list(set(pdf_links))

    # --------------------------------------------------
    # Download New Reports
    # --------------------------------------------------

    def download_reports(self):

        downloaded = []

        links = self.get_report_links()

        print(f"Found {len(links)} reports.")

        for url in links:

            filename = url.split("/")[-1]

            save_path = os.path.join(
                self.save_dir,
                filename
            )

            if os.path.exists(save_path):

                continue

            print(f"Downloading {filename}")

            r = requests.get(
                url,
                timeout=60
            )

            with open(save_path, "wb") as f:

                f.write(r.content)

            downloaded.append(save_path)

        print(f"Downloaded {len(downloaded)} new reports.")

        return downloaded
