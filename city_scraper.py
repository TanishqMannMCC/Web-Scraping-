import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# --- Configuration ---
URL = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
OUTPUT_FILENAME = "india_cities_population_cleaned_final.csv"

def clean_text_from_html(text):
    """Cleans text extracted from HTML cells by removing bracketed numbers and extra whitespace."""
    cleaned = re.sub(r'\[.*?\]', '', text)
    return cleaned.strip()

def scrape_and_clean_cities():
    """
    Scrapes both tables, cleans the data by converting population columns to numbers,
    and saves the final result to a single, clean CSV file.
    """
    print("Attempting to scrape data...")

    try:
        headers_request = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        response = requests.get(URL, headers=headers_request, verify=True)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        all_stats_tables = soup.find_all('table', class_=['wikitable', 'sortable'])
        print(f"Found {len(all_stats_tables)} tables. Processing...")

        all_dataframes = []
        for table_idx, stats_table in enumerate(all_stats_tables[:2]):
            print(f"\nProcessing Table {table_idx + 1}...")
            current_table_data = []
            rows = stats_table.find('tbody').find_all('tr')

            for row in rows[1:]:
                all_cells = row.find_all(['th', 'td'])

                # --- FINAL LOGIC ---
                # Use flexible check and negative indexing to handle parser inconsistencies.
                # Check for at least 5 cells to ensure we have enough data to unpack.
                if len(all_cells) >= 5:
                    try:
                        # Use negative indices to grab the last 5 cells, which are the consistent data columns.
                        # [-5]=City, [-4]=Pop2011, [-3]=Pop2001, [-2]=State, [-1]=Ref
                        row_data = {
                            'City': clean_text_from_html(all_cells[-5].text),
                            'Population (2011)': clean_text_from_html(all_cells[-4].text),
                            'Population (2001)': clean_text_from_html(all_cells[-3].text),
                            'State or union territory': clean_text_from_html(all_cells[-2].text),
                            'Ref': clean_text_from_html(all_cells[-1].text)
                        }
                        current_table_data.append(row_data)
                    except IndexError:
                        # This will catch any truly malformed rows and skip them.
                        continue
            
            print(f"Extracted {len(current_table_data)} data rows.")
            if current_table_data:
                all_dataframes.append(pd.DataFrame(current_table_data))

        if not all_dataframes:
            print("No data was successfully scraped.")
            return

        # --- Combine and Clean Data ---
        print("\nCombining and cleaning the scraped data...")
        combined_df = pd.concat(all_dataframes, ignore_index=True)

        population_cols = ['Population (2011)', 'Population (2001)']
        for col in population_cols:
            combined_df[col] = combined_df[col].str.replace(',', '', regex=False)
            combined_df[col] = pd.to_numeric(combined_df[col], errors='coerce')
        
        print("Population columns have been converted to numbers.")

        # --- Save Final File ---
        combined_df.to_csv(OUTPUT_FILENAME, index=False)
        print(f"\nSuccess! Fully cleaned data for both tables saved to {OUTPUT_FILENAME}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_and_clean_cities()