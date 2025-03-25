import sqlite3
import webbrowser

def highlight(text, query):
    return text.replace(query, f"\033[1;32m{query}\033[0m")  # green highlight

def search_publications(keyword, db_name="publications.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT title, authors, year, publication_link, author_profiles
        FROM publications
        WHERE title LIKE ? OR authors LIKE ? OR year LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%", f"%{keyword}%"))

    results = cursor.fetchall()
    conn.close()

    if not results:
        print("\n❌ No results found for your query.")
        return

    print(f"\n🔍 Showing results for: \033[1;34m{keyword}\033[0m\n")

    for idx, (title, authors, year, pub_link, profiles) in enumerate(results, 1):
        print(f"{idx}. \033[1m{highlight(title, keyword)}\033[0m")
        print(f"   👤 Authors: {highlight(authors, keyword)}")
        print(f"   📅 Year: {year}")
        print(f"   🔗 Publication Link: {pub_link}")
        print(f"   🔗 Author Profile(s): {profiles}")
        print()

    # Optional: Ask user to open a link
    choice = input("Enter result number to open publication link (or press Enter to skip): ")
    if choice.isdigit() and 1 <= int(choice) <= len(results):
        pub_link = results[int(choice)-1][3]
        print("🌐 Opening in your browser...")
        webbrowser.open(pub_link)

# Main loop
if __name__ == "__main__":
    print("\n🎓 Coventry Uni Publication Search")
    print("Search publications by department members.\n")
    while True:
        query = input("🔎 Enter a keyword (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        search_publications(query)
