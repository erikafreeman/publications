# publication_manager.py
from datetime import datetime

def generate_markdown():
   markdown = "# PUBLICATIONS\n\n"
   
    publications_data = {
      "first_author": {
          "published": [
              {
                  "title": "Ecosystem ecology needs an ecology of molecules",
                  "journal": "Trends in Ecology and Evolution",
                  "year": 2025,
                  "coauthors": ["Tianna Peller", "Florian Altermatt"],
                  "doi": "10.1016/j.tree.2024.xxx"
              },
              {
                  "title": "Ticking Clock",
                  "journal": "Science",
                  "year": 2024,
                  "coauthors": ["Cecilia Padilla-Iglesias"],
                  "notes": "Most popular Working Life essays of 2024",
                  "doi": "10.1126/science.2024.xxx",
                  "equal_contribution": True
              },
              {
                  "title": "Cyanobacteria in the Anthropocene - synanthropism forged in an era of global change",
                  "journal": "Water Environmental Research",
                  "year": 2024,
                  "coauthors": ["Erratt KJ"],
                  "doi": "10.1002/wer.2024.xxx",
                  "equal_contribution": True
              },
              {
                  "title": "Universal Microbial Processes Rework Dissolved Organic Matter along Environmental Gradients",
                  "journal": "Nature Communications",
                  "year": 2024,
                  "coauthors": ["Emilson EJS", "Braga L", "Emilson C", "Martineau C", "Dittmar T", "Goldhammer T", "Singer G", "Tanentzap AJ"],
                  "doi": "10.1038/s41467-024-xxx"
              },
              {
                  "title": "Global Changes May Be Promoting a Rise in Select Cyanobacteria in Nutrient-poor Northern Lakes",
                  "journal": "Global Change Biology",
                  "year": 2020,
                  "coauthors": ["Jones B", "Bergstrom AK", "Creed IF"],
                  "doi": "10.1111/gcb.2020.xxx"
              },
              {
                  "title": "Turning on the Tap: Demand for Resources as a Driver of Change in the Boreal Zone, Canada",
                  "journal": "Environmental Reviews",
                  "year": 2019,
                  "coauthors": ["Erdozain M", "Daillaire CO", "Teichert S", "Creed IF", "Nelson HW"],
                  "doi": "10.1139/er.2019.xxx",
                  "equal_contribution": ["Erdozain M", "Daillaire CO"]
              }
          ],
          "under_review": [
              {
                  "title": "Forest Harvest Disrupts the Ecology of Molecules in Headwater Streams",
                  "journal": "PNAS",
                  "coauthors": ["Emilson EJS", "Webster K", "Dittmar T", "Tanentzap AJ"],
                  "preprint": True,
                  "doi": "10.1101/2024.xxx"
              },
              {
                  "title": "A Unified Conceptual Model of Organic Matter Scaling in River Corridors",
                  "journal": "Scientific Reports",
                  "coauthors": ["McClure EA", "Mudunuru ML", "Ward CS", "Bottos EM", "González-Pinzón R", "Feeser KL", "Krause S", "Peña J", "Newcomer ME"]
              }
          ],
          "in_preparation": [
              {
                  "title": "Examining the Efficacy of Fluorescence Spectroscopy to Detect Forest Harvest in Temperate and Boreal Forests",
                  "coauthors": ["Tanentzap AJ", "Emilson EJS", "Dittmar T"]
              },
              {
                  "title": "A cheat sheet for the environmental metabolomics revolution",
                  "journal": "Science",
                  "coauthors": ["Tianna Peller", "Francois Keck", "Florian Altermatt"]
              },
              {
                  "title": "Leveraging community ecology to understand dissolved organic matter",
                  "coauthors": ["Florian Altermatt", "Roman Alter"]
              }
          ]
      },
      "contributing_author": {
          "published": [
              {
                  "title": "Making Waves: Deep Cyanobacteria Layers Pose a Known Unknown Risk to Water Security",
                  "journal": "Water Security",
                  "year": 2023,
                  "authors": ["Erratt KJ", "Creed IF", "Freeman EC", "Trick C"],
                  "doi": "10.1016/j.wasec.2023.xxx"
              },
              {
                  "title": "Exploring Global River Corridor OM Chemistry through the Ecological Concept of Core-satellite Species",
                  "journal": "Frontiers in Water",
                  "year": 2023,
                  "authors": ["Stadler M", "de Melo M", "Garayburu-Caruso V", "Freeman EC", "Bice K", "Mateus-Barros E", "Lu Y", "Barnard M", "Cheng S", "Dwivedi D", "Tanentzap A", "Meile C"],
                  "doi": "10.3389/frwa.2023.xxx"
              },
              {
                  "title": "Determining the Biogeochemical Transformations of Organic Matter Composition in Global Rivers Using Molecular Signatures",
                  "journal": "Frontiers in Water",
                  "year": 2023,
                  "authors": ["Buser-Young J", "Garcia P", "Schrenk M", "Regier P", "Ward ND", "Biçe K", "Brooks S", "Freeman EC", "Lønborg C"],
                  "doi": "10.3389/frwa.2023.xxx"
              },
              {
                  "title": "Deep Cyanobacteria Layers: An Overlooked Aspect of Managing Risks of Cyanobacteria",
                  "journal": "Environmental Science & Technology",
                  "year": 2022,
                  "authors": ["Erratt KJ", "Creed IF", "Freeman EC", "Westrick J", "Trick CG", "Birbeck J", "Watson L", "Zastepa A"],
                  "doi": "10.1021/acs.est.2022.xxx"
              },
              {
                  "title": "It Takes a Village: Using a Crowdsourced Approach to Investigate Organic Matter Composition in Global Rivers Through the Lens of Ecological Theory",
                  "journal": "Frontiers in Water",
                  "year": 2022,
                  "authors": ["Borton MA", "Collins SM", "Graham EB", "Garayburu-Caruso VA", "Goldman AE", "de Melo M", "Freeman EC"],
                  "consortium": "WHONDRS Crowdsourced Consortium",
                  "doi": "10.3389/frwa.2022.xxx"
              },
              {
                  "title": "Feasibility of Instance Segmentation of Phytoplankton Using Brightfield Microscopy & Deep Learning",
                  "journal": "Journal of Computational Vision and Imaging Systems",
                  "year": 2021,
                  "authors": ["Deglint JL", "Park JA", "Freeman EC", "Erratt KJ", "Allaf MM", "Wong A"],
                  "doi": "10.15353/jcvis.2021.xxx"
              },
              {
                  "title": "Global Maps of Soil Temperature",
                  "journal": "Global Change Biology",
                  "year": 2021,
                  "authors": ["Lembrechts J", "Van den Hoogen J", "Aalto J", "Ashcroft M", "De Frenne P", "Kemppinen J", "Freeman EC", "Hoffrén R"],
                  "doi": "10.1111/gcb.2021.xxx"
              },
              {
                  "title": "Global Change-driven Effects on Dissolved Organic Matter Composition: Implications for Food Webs of Northern Lakes",
                  "journal": "Global Change Biology",
                  "year": 2018,
                  "authors": ["Creed IF", "Bergstrom AK", "Trick CG", "Grimm NB", "Hessen DO", "Karlsson J", "Kidd KA", "Kritzberg E", "McKnight DM", "Freeman EC", "Senar OE"],
                  "doi": "10.1111/gcb.2018.xxx"
              }
          ],
          "in_preparation": [
              {
                  "title": "Microbes decrease organic matter persistence in lakes",
                  "authors": ["Fonvielle JA", "Sandor SR", "Freeman EC", "Dittmar T", "Tanentzap AJ"]
              },
              {
                  "title": "Soil Temp Global Database",
                  "journal": "Global Ecology and Biogeography",
                  "authors": ["Lembrechts J", "Freeman EC"]
              },
              {
                  "title": "Wildfires change dissolved organic matter in boreal headwater streams",
                  "journal": "JGR Biogeosciences",
                  "authors": ["Matula E", "Emilson EJS", "Smenderovac E", "Fonvielle J", "Freeman EC", "Tanentzap AJ"]
              }
          ],
          "technical_reports": [
              {
                  "title": "Protocol for the analysis of phytoplankton using the FlowCAM® from Fluid Imaging Technologies",
                  "type": "Standard Operating Procedure 001-2016",
                  "year": 2016,
                  "authors": ["Creed IF", "Trick CG", "Freeman EC", "Oakes B"]
              }
          ]
      }
    }


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
