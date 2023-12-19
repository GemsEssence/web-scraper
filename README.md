# Web Scraper

This Python script is designed for scraping dynamic websites and extracting publicly available data from various platforms.

## Supported Platforms and Extracted Data

### LinkedIn
- Company Name
- Industry
- Website
- Specialties
- Size
- Headquarters
- Organization Type
- Founded On
- Followers
- Branches
- Employees Name

### Instagram
- User ID
- Number of Posts
- Followers
- Following
- Biography
- External URL

### Facebook
- Emails
- Contact numbers
- Address

### Real Estate
- Building Name
- Location
- Price
- Area (in sq ft.)
- Average Price
- Number of Rooms
- EMI
- Contact

## How to Run

1. Clone the repository
2. Set up a virtual environment
    ```bash
    $ python3 -m venv env
    ```
3. Activate the virtual environment
    ```bash
    $ source env/bin/activate
    ```
4. Install dependencies
    ```bash
    $ pip install -r requirements.txt
    ```
5. **To Scrape LinkedIn**

    - Enter LinkedIn URLs of the companies you want to scrape in `linkedIn_users.txt`
    
    - Run LinkedIn Python file
        ```bash
        $ python linkedIn.py
        ```

6. **To Scrape Instagram**

    - Enter usernames you want to scrape in `instagram_users.txt`
    
    - Run Instagram Python file
        ```bash
        $ python instagram.py
        ```

7. **To Scrape Facebook**

    - Enter Facebook URLs of the companies you want to scrape in `facebook_users.txt`
    
    - Run Facebook Python file
        ```bash
        $ python facebook.py
        ```

8. **To Scrape Real Estate Website**

    - Run Real Estate Python file
        ```bash
        $ python real_estate.py
        ```
