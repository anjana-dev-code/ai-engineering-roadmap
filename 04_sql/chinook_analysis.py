import sqlite3

# Chinook.db must sit in the same folder as this script (or change the path)
conn = sqlite3.connect("Chinook.db")
cur = conn.cursor()


def run(title, query):
    print(f"\n--- {title} ---")
    for row in cur.execute(query):
        print(row)


# ---------- Level 1: top 5 best-selling genres ----------
run("Top 5 genres by units sold", """
SELECT g.Name AS genre, SUM(il.Quantity) AS units_sold
FROM InvoiceLine il
JOIN Track t ON t.TrackId = il.TrackId
JOIN Genre g ON g.GenreId = t.GenreId
GROUP BY g.GenreId
ORDER BY units_sold DESC
LIMIT 5;
""")

# ---------- Level 2: revenue per country ----------
run("Revenue per country", """
SELECT BillingCountry AS country, ROUND(SUM(Total), 2) AS revenue
FROM Invoice
GROUP BY BillingCountry
ORDER BY revenue DESC
LIMIT 10;
""")

# ---------- Level 3: top 10 customers by spend ----------
run("Top 10 customers by spend", """
SELECT c.FirstName || ' ' || c.LastName AS customer,
       ROUND(SUM(i.Total), 2) AS total_spent
FROM Customer c
JOIN Invoice i ON i.CustomerId = c.CustomerId
GROUP BY c.CustomerId
ORDER BY total_spent DESC
LIMIT 10;
""")

# ---------- Boss: top 3 artists in each genre (window function) ----------
run("Top 3 artists per genre (first 12 rows)", """
WITH artist_sales AS (
    SELECT g.Name  AS genre,
           ar.Name AS artist,
           SUM(il.UnitPrice * il.Quantity) AS sales
    FROM InvoiceLine il
    JOIN Track t   ON t.TrackId  = il.TrackId
    JOIN Genre g   ON g.GenreId  = t.GenreId
    JOIN Album al  ON al.AlbumId = t.AlbumId
    JOIN Artist ar ON ar.ArtistId = al.ArtistId
    GROUP BY g.GenreId, ar.ArtistId
),
ranked AS (
    SELECT genre, artist, ROUND(sales, 2) AS sales,
           ROW_NUMBER() OVER (PARTITION BY genre ORDER BY sales DESC) AS rank_in_genre
    FROM artist_sales
)
SELECT genre, artist, sales, rank_in_genre
FROM ranked
WHERE rank_in_genre <= 3
ORDER BY genre, rank_in_genre
LIMIT 12;
""")

conn.close()