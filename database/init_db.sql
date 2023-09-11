-- Create the manufacturers table
CREATE TABLE manufacturers (
    id BIGSERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- Create the craigslist_cars table
CREATE TABLE cars (
    id BIGINT PRIMARY KEY,
    url TEXT,
    price DECIMAL,
    year INTEGER,
    manufacturer_id BIGINT REFERENCES manufacturers(id),
    model TEXT,
    condition TEXT,
    cylinders TEXT,
    fuel TEXT,
    odometer DECIMAL,
    title_status TEXT,
    transmission TEXT,
    VIN TEXT,
    drive TEXT,
    size TEXT,
    type TEXT,
    paint_color TEXT,
    image_url TEXT,
    description TEXT,
    latitude DECIMAL,
    longitude DECIMAL,
    posting_date TIMESTAMP WITH TIME ZONE
);
