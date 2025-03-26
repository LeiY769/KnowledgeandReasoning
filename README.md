# Show Catalog Ontology and Information System

This project was developed as part of the Knowledge Representation and Reasoning course. It provides a solution to enhance the search for movies and TV shows on streaming platforms by integrating a relational database with an ontology. The system maps data from a PostgreSQL database (sourced from Kaggle’s Netflix Movies and TV Shows dataset) onto an OWL 2 QL ontology and demonstrates how to deploy and query the resulting RDF data using SPARQL.

## Authors

- **Alexia Donati** (s200742)
- **Lei Yang** (s201670)
- **Bruce Andriamampianina** (s2302253)

*May 20, 2024*

## Project Overview

The project is divided into several key parts:

- **Database Design:**  
  A conceptual relational database schema was designed based on Bansal Shivam’s Netflix dataset. The schema includes multiple entities (e.g., Show, Person, Country, Genre) and relations that allow efficient filtering of shows based on criteria like genre, rating, and production country.

- **Ontology Development:**  
  An ontology was created using the OWL 2 QL profile. This choice was motivated by the need for computational efficiency while integrating with the relational database. The ontology defines classes for shows, persons (with specific sub-classes for Actor and Director), and other related entities.

- **Mapping to RDF:**  
  A mapping process converts relational data into RDF triples. This process involves generating triples maps for each table and addressing challenges such as handling multiple roles (actor/director) and managing complex join queries.

- **Deployment and Demonstration:**  
  The system is deployed using multiple components:
  - **SPARQL Endpoint:** Apache Jena Fuseki for hosting RDF data.
  - **Linked Data Frontend:** Pubby for visualizing linked data.
  - **Web Server:** Jetty for serving the frontend.
  - Additional instructions are provided for integrating with an Apache2 Web server (LAMP stack) and generating documentation with Widoco.

- **SPARQL Queries:**  
  Several example queries are provided to demonstrate how to search the RDF data:
  - A simple query for movies with a duration over 90 minutes.
  - A join query to list movies featuring a specific actor.
  - Aggregate queries to count movies produced per country.
  - A more advanced query demonstrating how new relationships (e.g., using the `knows` property) can be queried.

## Installation and Deployment

### Prerequisites
- **Operating System:** Ubuntu 22.04.4
- **Java:** OpenJDK 17.0.10
- **Database:** PostgreSQL
- **Web Servers:** Apache Jena Fuseki, Jetty, Apache2 (LAMP stack)

### Deployment Steps

1. **Deploying the SPARQL Endpoint (Apache Jena Fuseki):**
   - Update your `/etc/hosts` file with:  
     `127.0.0.1 data.show-catalog.org`
   - Run the Fuseki server with `./fuseki-server`
   - Create a new dataset (e.g., `ds`) and upload the RDF data from `output.ttl`.

2. **Setting Up the Linked Data Frontend (Pubby):**
   - Build Pubby using Maven:  
     `mvn package -DskipTests -Dmaven.javadoc.skip=true`
   - Replace the default configuration (`./target/pubby/WEB-INF/config.ttl`) with the provided `config.ttl`.
   - Rename the Pubby folder to `ROOT` and copy it to the Jetty `webapps` directory.
   - Run Jetty using:  
     `java -jar start.jar`

3. **Configuring Apache2 Web Server:**
   - Add the following line to `/etc/hosts`:  
     `127.0.0.1 ontology.show-catalog.org`
   - Place the provided `show/` folder into `/var/www/`
   - Add the `ontology.conf` file to `/etc/apache2/sites-available/`
   - Enable the site with:  
     `sudo a2ensite ontology.conf`
   - Reload Apache2:  
     `sudo systemctl reload apache2`

4. **Documentation Generation:**
   - Documentation can be generated using Widoco.

## Usage

Once deployed, users can access:
- **Ontology Documentation:** [http://ontology.show-catalog.org/show](http://ontology.show-catalog.org/show)
- **Linked Data Interface:** [http://data.show-catalog.org](http://data.show-catalog.org)

SPARQL queries can be run either through a SPARQL client or within the provided notebook (`SPARQL.ipynb`), which demonstrates:
- Filtering shows by duration
- Joining data to retrieve movies featuring a specific actor (e.g., "Tom Holland")
- Aggregating counts by production country
- More complex queries that illustrate relationships beyond the original database design

## Project Structure

- **Database Schema:** Conceptual design and normalization details.
- **Ontology Files:** OWL 2 QL based ontology definitions and schema diagrams.
- **Mapping Scripts:** SQL queries and mappings for converting relational data to RDF.
- **Deployment Configurations:** Configuration files for Apache Jena Fuseki, Pubby, Jetty, and Apache2.
- **SPARQL Queries:** Sample queries included in `SPARQL.ipynb`.

## Conclusion

This project demonstrates a comprehensive approach to integrating a relational database with an ontology to facilitate more effective search and filtering of movies and TV shows. The solution leverages efficient OWL 2 QL mappings, robust deployment strategies, and SPARQL querying to create a versatile information system. Future work could include integrating additional datasets to further enrich the database and enhance the system’s capabilities.

## References

- Michael DeBellis. *A Practical Guide to Building OWL Ontologies using Protégé 5.5 and Plugins*, 2021.
- Daniel Garijo. *WIDOCO: a wizard for documenting ontologies*, International Semantic Web Conference, 2017.
- Steffen Lohmann et al. *WebVOWL: Web-based Visualization of Ontologies*, Knowledge Engineering and Knowledge Management, 2015.
- OWL Working Group. *OWL 2 QL*, 2009. [Link](https://www.w3.org/TR/2009/WD-owl2-new-features-20090421/#OWL_2_QL)
- Bansal Shivam. *Netflix Movies and TV Shows*, 2022. [Link](https://www.kaggle.com/datasets/shivamb/netflix-shows/data)
