import PyPDF2
import json
import re

# Define your search terms here
SEARCH_TERMS = [
    'Trump', 'Herring', 'Don King', 'microfilm', 'Charles'
    ]


def search_pdf(pdf_path, search_terms):
    results = {}
    item_number = 1

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for term in search_terms:
            term_results = []
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if re.search(re.escape(term), text, re.IGNORECASE):
                    term_results.append(str(page_num + 1))

            if term_results:
                results[str(item_number)] = {
                    "term": term,
                    "pages": ",".join(term_results) + ","
                }
                item_number += 1

    return results


def main():
    pdf_path = "/Users/yehiamokhtar/Downloads/Software/projects/indexer/content/TrumpNetworkGuy.pdf"

    results = search_pdf(pdf_path, SEARCH_TERMS)

    with open("search_results2.json", "w") as json_file:
        json.dump(results, json_file, indent=2)

    print("Search completed. Results saved in search_results.json")


if __name__ == "__main__":
    main()