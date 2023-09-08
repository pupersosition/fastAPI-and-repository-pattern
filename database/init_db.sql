-- Create the manufacturers table
CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- Create the cities table
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city_url TEXT,
    latitude DECIMAL,
    longitude DECIMAL,
    UNIQUE(name, city_url) -- Ensuring that the combination of name and city_url is unique
);

-- Create the craigslist_cars table
CREATE TABLE craigslist_cars (
    id SERIAL PRIMARY KEY,
    url TEXT,
    city_id INTEGER REFERENCES cities(id),
    price DECIMAL,
    year INTEGER,
    manufacturer_id INTEGER REFERENCES manufacturers(id),
    make TEXT,
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
    description TEXT
);
