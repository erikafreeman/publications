# publication_manager.py
from datetime import datetime

def generate_markdown():
   markdown = "# PUBLICATIONS\n\n"
   
   # First Author Publications
   markdown += "## First Author Publications\n\n"
   
   # Published
   markdown += "### Published\n"
   for pub in publications_data["first_author"]["published"]:
       markdown += f"[{pub['title']}](https://doi.org/{pub['doi']}). *{pub['journal']}* {pub['year']}.\n"
       coauthors = "with " + ", ".join(pub['coauthors'])
       if "equal_contribution" in pub and pub["equal_contribution"]:
           coauthors += "*"
       markdown += f"{coauthors}\n\n"
   
   # Under Review
   markdown += "### Under Review\n"
   for pub in publications_data["first_author"]["under_review"]:
       title_text = f"{pub['title']}"
       if "preprint" in pub and pub["preprint"]:
           markdown += f"[{title_text}](https://doi.org/{pub['doi']}). *{pub['journal']}*. [preprint]\n"
       else:
           markdown += f"{title_text}. *{pub['journal']}*.\n"
       markdown += f"with {', '.join(pub['coauthors'])}\n\n"
   
   # Contributing Author Publications
   markdown += "## Contributing Author Publications\n\n"
   for pub in publications_data["contributing_author"]["published"]:
       markdown += f"[{pub['title']}](https://doi.org/{pub['doi']}). *{pub['journal']}* {pub['year']}.\n"
       authors = pub['authors'].copy()
       author_index = authors.index("Freeman EC")
       authors[author_index] = "**Freeman EC**"
       markdown += f"{', '.join(authors)}\n\n"
   
   markdown += "*Note: Equal contribution indicated by asterisk (*)"
   return markdown

def generate_html():
   html = f"""
   <!DOCTYPE html>
   <html>
   <head>
       <title>Publications - Erika C. Freeman</title>
       <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
       <style>
           .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
           a {{ color: #2962ff; text-decoration: none; }}
           a:hover {{ text-decoration: underline; }}
       </style>
   </head>
   <body>
       <div class="container">
           {generate_markdown()}
           <footer>Last updated: {datetime.now().strftime('%Y-%m-%d')}</footer>
       </div>
   </body>
   </html>
   """
   with open("index.html", "w") as f:
       f.write(html)

if __name__ == "__main__":
   generate_html()
